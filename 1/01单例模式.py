
# 单例模式__new__ 方法一

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls,*args,**kwargs)
        return cls._instance

class MyClass(Singleton):
    a=1
one=MyClass()
two=MyClass()
one.a=20
two.a=30
# one和two完全相同，可以用id()，==，is检查
print(one.a)    #
print (two.a)
print(id(one))  #
print(id(two))  #
print(one == two)   # True
print(one is two)   # True


# 30
# 30
# 2418859210792
# 2418859210792
# True
# True



# 单例模式装饰器 方法二
def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
@singleton
class MyClass3(object):
    a = 1
one = MyClass3()
two = MyClass3()
print(id(one))  # 2880466769232
print(id(two))  # 2880466769232
print(one == two)  # True
print(one is two)  # True

