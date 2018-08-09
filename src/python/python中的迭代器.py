
"""
迭代器
迭代器是python中访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象,迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问结束,迭代器智能往前不会后退
迭代器有两个基本的方法:iter和next
"""
list = [1,2,3,4]

# 遍历的第一种方式
it = iter(list) #获取迭代器,获取列表的迭代器
for item in it:
    print(item)

# 访问的第2种方式
it = iter(list)
print(next(it)) #输出迭代器的指向的元素,并移动
print(next(it))