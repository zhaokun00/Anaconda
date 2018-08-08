"""
python标识符
在python里,标识符由字母、数字、下划线组成
在python中,所有标识符可以包括英文、数字以及下划线,但不能以数字开头
在python中的标识符是区分大小写的
在下划线开头的标识符是有特殊意义的,以单下划线开头_foo的代表不能直接访问的类属性,需要通过提供的接口进行访问,不能用from xxx import *而导入
在双下划线开头的__foo代表类的私有成员
以双下划线开头和结尾的__foo__代表python里特殊方法专用的标识,例如__init__()代表类的构造函数

"""

# python中可以同一行显示多条语句,方法是用分号;分开
# 示例1
print("zhaokun");print("ycl")

"""
行和缩进
学习python与其他语言最大的区别就是,python的代码块不用使用大括号{}来控制类、函数以及其他逻辑判断,python最具有特色就是用缩进来写模块
缩进的空白数量是可变的,但是所有代码语句必须包含相同的缩进空白数量,这个必须严格执行
"""
# 示例2
if True:
    print("true")
else:
    print("false")
   #  没有随进将会报错
   #print("执行if")

# 多行语句:python通常是一行写完一条语句,但如果语句很长,我们可以使用反斜杠(\)来实现多行语句
# 在(),[],{}中的多条语句,不需要使用反斜杠(\)
# 示例3
print("多行" + \
      "语句")

"""
空行
函数之间或类的方法之间用空行分割,表示一段新的代码的开始,类和函数入口之间也用一行空行分割,以突出函数的入口的开始
"""

"""
print输出
print默认输出是换行的,如果要实现不换行需要在变量末尾加上end=""
"""
# 示例4
print("不换行",end="")
print("输出")

"""
在python用import或者from...import来导入相应的模块

将整个模块导入,格式为:import somemodule
从某个模块中导入某个函数,格式为:from somemodule import somefunction
从某个模块中导入多个函数,格式为:from somemodule import firstfunc, secondfunc, thirdfunc
从某个模块中将全部函数导入:from somemodule import *
"""