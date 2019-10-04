# 导个来的文件只加载一次去临时文件pyc中取值    第二次导入没得任何意义            天生的单例

from  sing import  ss
ss.run()
print (id(ss.run()))


# from  sing import  ss
ss.run()
print (id(ss.run()))


# ok！！！
# rrrrrrrrrrrrrrrrrrrrrrrrrr
# 100
# 100
# 1720755408
# 100
# 100
# 1720755408
