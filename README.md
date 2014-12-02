python-ORM
==========

Just for practice.That's a simple ORM framework by python.

感谢@廖雪峰
开始学习走路。
这种方法很好，在编写框架或者方法以前，先预定好用户的调用方法，如本例，
虚拟一个网购的场景，最近雾霾严重，买口罩，至少得买10个先。
我们期待用户如此操作即可调用：

calss Order(Model):
    #对应数据库表，创建映射关联属性
    orderId = IntegerField('orderId')
    productName = StringField('productName')
    amount = IntegerField('amount')
    userName = StringField('userName')
#新增一条数据，new一个实例
o = Order(orderId=201411281048001, productName='respirator',amount=10,userName='evsward')
#保存到数据库
u.save()