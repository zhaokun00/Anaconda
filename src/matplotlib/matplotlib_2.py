import matplotlib.pyplot as plt
import pandas as pd

# 示例1: 画多个子图

"""
figure = plt.figure()

# 221:代表的意思是2行2列的第1幅图像,其他以此类推
# pic1 = figure.add_subplot(2,2,1)
pic1 = figure.add_subplot(221)
pic2 = figure.add_subplot(222)
pic3 = figure.add_subplot(223)
pic4 = figure.add_subplot(224)

plt.show()
"""

# 示例2: 在子图中画图
"""
figure = plt.figure()

pic1 = figure.add_subplot(221)
pic2 = figure.add_subplot(222)
pic3 = figure.add_subplot(223)
pic4 = figure.add_subplot(224)

x = [1,2,3,4]
y = [10.3,6,9,4]

pic1.plot(x,y)

plt.show()
"""

# 示例3: 在一张图中画多幅图像

# figsize设置显示图像的大小

"""
fig = plt.figure(figsize=(6,3))

# label = ["red","yellow"]
label = "picture"

x1 = [1,2,3,4]
y1 = [1,2,3,4]

x2 = [5,6,7,8]
y2 = [5,6,7,8]

# 设置显示的图标
plt.plot(x1,y1,c='red',label = label)

plt.plot(x2,y2,c='yellow',label = label)

# 设置显示图标的位置,如果该参数不设置,在显示图像时图标则不会显示出来
plt.legend(loc='best')

plt.show()

"""

# 示例4:画散点图

"""
x1 = [1,2,3,4]
y1 = [1,2,3,4]

# 画散点图
plt.scatter(x1,y1)

plt.show()

"""

# 示例5:画直方图
x1 = [1-0.25,2-0.25,3-0.25,4-0.25]
y1 = [1,2,3,4]

# plt.bar(x1,y1)

print(x1)
# 0.1表示显示的宽度
plt.bar(x1,y1,0.5)
plt.show()