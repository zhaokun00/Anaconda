"""
python中一个class只能有一个用于构造对象的__init__函数
但python中的变量是无类型的,因此传给__init__的参数可以是任何类型
python中的函数参数在定义时可以有默认值,可以让__init__函数接受多个参数,在后面的一些参数给出默认值得
方法是让__init__接收不同个数的参数,并且执行类型检测执行不同的代码,用上述方法实现类的构造函数的多态性
"""
# 定义类
class MyCalss:

    """
    self代表类的实例,而非类
    类的方法与普通的函数只有一个特别的区别,他们必须有一个额外的第一个参数名称,按照惯例它的名称是self
    """
    # 对象创建时会调用
    # def __init__(self):
    #     print("构造函数")

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    # 对象销毁时会调用
    def __del__(self):
        print("析构函数")

    # 定义成员变量,属性为公有属性,外面可以直接访问
    name = "zhaokun"

    """
        类的私有属性:
        __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs
    """
    # 定义私有变量,私有变量外面不能直接访问
    __age = 10;

    # 定义方法,属性为公有属性,外面可以直接访问
    def getName(self):
        return self.name

    def getAge(self):
        return self.__age

    def setAge(self,age):
        self.__age = age;

    """
        类的私有方法
        __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods
    """
    # 定义私有方法,外部不能直接访问
    def __privateMethon(self):

        print("privateMethon")

    def printf(self):
        print("调用父类方法")
# 实例化一个对象
# x = MyCalss()
#
# print("name = ",x.getName())
#
# x.setAge(100)
# print("age = ",x.getAge())

# y = MyCalss("ycl","30")
# print("name = ",y.getName())
# print("age = ",y.getAge())

class SubClass(MyCalss):

    def __init__(self,name,age):
        MyCalss.__init__(self,name,age)

    def speak(self):
        print("speak")

    # 方法的重写
    def printf(self):
        # 调用父类的方法
        MyCalss.printf(self)
        print("调用子类方法")

sub = SubClass("aimi",1);

print("name = ",sub.getName())
print("age = ",sub.getAge())

sub.speak()

sub.printf()
