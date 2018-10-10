"""
字典(dictionary)是pythonn中另一个非常有用的内置数据类型
列表是有序的对象集合,字典是无序的对象集合,两者之间的区别在于:字典当中的元素是通过键值来存取的,而不是通过偏移来存取
字典是一种映射类型,字典用{}标识,它是一个无序的键值对集合
键必须死样不可变类型,在同一字典中key必须是唯一的
"""

# 示例1
dict1 = {}

print("type(dict1):",type(dict1))

# 往字典中放入数据
dict1["name"] = "zhaokun"
dict1["age"] = 30

print("name:",dict1["name"]);

# 示例2,初始化时往字典中放入数据
dict2 = {"name":"ycl","age":30}
print("name:",dict2["name"])
print("age:",dict2["age"])



