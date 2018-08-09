"""
定义一个函数,以下是简单的规则:

1.函数代码块以def关键词开头,后接函数标识符名称和圆括号()
2.任何传入参数和自变量必须放在圆括号中间,圆括号之间可以用于定义参数
3.函数的第一行语句可以选择性地使用文档字符串,用于存放函数说明
4.函数内容以冒号起始,并且缩进
5.return [表达式]结束函数,选择性地返回一个值给调用方,不带表达式的return相当于放回None
"""
# 函数的定义
def printStr():
    "打印字符串函数"
    print("printStr")
    return;

"""
函数的调用:
定义一个函数只给了函数一个名称,指定了函数里面包含的参数和代码结构
这个函数的基本结构完成以后,你可以通过 另一个函数调用执行,调用格式如下:

函数名()
"""
# 函数的调用,
printStr()

# 传递不可变参数
def trans1(a):
    print("1.id(a) = ",id(a))
    a = 10
    print("2.id(a) = ", id(a))

b = 2

print("1.id(b) = ",id(b))
trans1(b)

print("b = ",b)

# 传递可变参数
def trans2(a):
    print("1.id(a) = ",id(a))
    a.append(3)
    print("2.id(a) = ", id(a))

b = [1,2]

print("1.id(b) = ",id(b))
trans2(b)

print("b = ",b)

# 传递多个参数,并且包含了默认参数
def trans3(name,age=20):
    print("name",name)
    print("age", age)

# 可以传递2个参数
trans3("zhaokun",30)

# 可以传递1个参数,另一个没有传递的使用默认参数
trans3("zhaokun")

# 通过return返回参数
def sum(a,b):

    return a + b

total = sum(1,2)

print("total = ",total)

"""
全局变量和局部变量
定义在函数内部的变量拥有一个局部变量作用域,定义在函数外的拥有全局作用域
局部变量只能在其被声明的函数内部访问,而全局变量可以在整个程序范围内访问,调用函数时,所有在函数内声明的变量名称都将被加入到作用域中
"""

# 全局变量
total = 10

def trans4():

    # 局部变量,直接使用时是局部变量
    total = 100

trans4()

print("total = ",total)

def trans5():

    # 使用全局变量
    global total
    total = 100

trans5()

print("total = ",total)