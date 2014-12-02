# -*- coding: utf-8 -*-
class Field(object):
      #__init__创建实例要传入字段名和字段类型
      def __init__(self,name,column_type):
            self.name = name
            self.column_type = column_type
      #__str__定义打印实例时的输出
      #__name__使用自身就是'__main__'，如果是别人调用，就是文件名
      #__class__隐式调用，这个待解释：：：
      def __str__(self):
            return '<%s:%s>' % (self.__class__.__name__,self.name)
class StringField(Field):
      #创建StringField的实例，调用StringField自身的父类的构造方法
      def __init__(self,name):
            super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(Field):
      #创建IntegerField的实例，调用IntegerField自身的父类的构造方法
      def __init__(self,name):
            super(IntegerField,self).__init__(name,'bigint')
class ModelMetaclass(type):
      def __new__(cls,name,bases,attrs):
            if name=='Model':
                  return type.__new__(cls,name,bases,attrs)
            mappings = dict()
            for k,v in attrs.iteritems():
                  if isinstance(v,Field):
                        print('Found mapping: %s==>%s' % (k,v))
                        mappings[k] = v
            for k in mappings.iterkeys():
                  attrs.pop(k)
            attrs['__table__'] = name # 假设表名和类名一致
            attrs['__mappings__'] = mappings # 保存属性和列的映射关系
            return type.__new__(cls,name,bases,attrs)

class Model(dict):
      __metaclass__ = ModelMetaclass
      def __init__(self,**kw):
            super(Model,self).__init__(**kw)

      def __getattr__(self,key):
            try:
                  return self[key]
            except KeyError:
                  raise AttributeError(r"'model' object has no attribute '%s'" % key)
      def __setattr__(self,key,value):
            self[key] = value
      def save(self):
            field = []
            params = []
            args = []
            for k,v in self.__mappings__.iteritems():
                  field.append(v.name)
                  params.append('?')
                  args.append(getattr(self,k,None))
            sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(field),','.join(params))
            print('SQL:%s' % sql)
            print('ARGS:%s' % str(args))

