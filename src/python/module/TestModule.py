"""
想使用python源文件,只需要在另一个源文件里面执行import语句,语法格式如下:
import module1[,module2[,...moduleN]]

当解释器遇到import语句,如果模块在当前的搜索路径就会被导入,搜索路径是一个解释器会先进行搜索
的所有目录的列表

一个模块只会被导入一次,不管执行多了次import,这样可以防止导入模块被一遍又一遍地执行

搜索路径是在python编译或者安装的时候确定的,安装新的库也会被修改
"""

"""
PyCharm同目录下导入模块会报错的问题
在PyCharm2017中同目录下import其他模块，会出现No model named ...的报错，但实际可以运行

这是因为PyCharm不会将当前文件目录自动加入source_path。

在当前目录右键make_directory as-->Sources Root

相同目录:
同一目录下在a.py中导入b.py
import b 或者 from b import 方法/函数

不同目录:
不同目录下在a.py中导入b.py
import sys
sys.path.append('b模块的绝对路径')
import b

"""
import sys

# 自定义的模块,模块名为python的文件名
import userModule

# 打印模块的搜索路径
print("路径:",sys.path)

# 模块中函数的访问方式,模块名.函数名
userModule.print1()

"""
    from ... import
    python的from语句让你从模块中导入一个指定的部分到当前命令空间中国
    
    语法格式如下:
    from modname import name1[, name2[, ... nameN]]
    
    采用这种方式可以直接使用函数名,而不用加模块名
    
    把一个模块中的额所有内容全部导入当当前的命名空间也是可以的,格式如下:
    from modname import *
"""

# 含义:从userModule模块中导入函数print2
from userModule import print2

print2()

"""
    内置的函数dir()可以找到模块内定义的所有名称,以一个字符串列表的形式返回
"""
print(dir(userModule))