# 导个来的文件只加载一次去临时文件pyc中取值    第二次导入没得任何意义            天生的单例

from sing import  ss,Sun #  Sun类对象
print (id(ss))


a=Sun()
print (id(a))


b=Sun()
print (id(b))


#
# ok！！！
# rrrrrrrrrrrrrrrrrrrrrrrrrr
# 1267286899120
# 1267285115232
# 1267286898784