"""
python中的变量不需要声明,每个变量在使用前都必须赋值,变量赋值以后该变量才会被创建
在python中,变量就是变量,它没有类型,我们所所的类型是变量所指的内存中对象的类型
等号(=)用来给变量赋值
等号(=)运算符左边是一个变量名,等号(=)运算符右边是存储在变量中的值
"""

"""
python3中有6个标准的数据类型
Number(数字)
String(字符串)
List(列表)
Tuple(元组)
Set(集合)
Dictionary(字典)

在python3中的6个标准数据类型中:
不可变数据类型3个:Number、String、Tuple
可变数据类类型3个:List、Dictionary、Set
"""

"""
python3支持int、float、bool、complex
"""
# 从以下测试中可以看到两次赋值时,变量number的内存地址发生了变化
# type函数用来计算变量的类型,type()不会认为子类是一种父类类型,isinstance()会认为子类是父类类型
#
# id函数用来计算变量的内存地址

number=11
print("type1:",type(number))
print("id1:",id(number))

number = 22
print("type2:",type(number))
print("id2:",id(number))