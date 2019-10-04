# 导个来的文件只加载一次去临时文件pyc中取值    第二次导入没得任何意义            天生的单例

from sing import  ss  # 这个ss是Sun类的实例对象
print (id(ss))


from sing import  ss   # 这个ss是Sun类的实例对象
print (id(ss))


from  fun import *
foo()

# 这三个文件都是一个程序      只要属于这一个程序 其他他地方导入都都是一个对象

# ok！！！
# rrrrrrrrrrrrrrrrrrrrrrrrrr
# 2241649670520
# 2241649670520
# 2241649670520 ok11111111