import matplotlib.pyplot as plt
import pandas as pd

# 示例1:简单的画图

"""
# 画图
plt.plot()
# 显示
plt.show()
"""

# 示例2:从文本中读取数据进行画图

"""
info = pd.read_csv("UNRATE.csv")

# 将日期进行格式化
info["DATE"] = pd.to_datetime(info["DATE"])

data = info.head(10)

# 设置x、y坐标
plt.plot(data["DATE"],data["VALUE"])

# 设置x坐标倾斜度
plt.xticks(rotation=45)
# 设置y坐标倾斜度
plt.yticks(rotation=45)

# 设置x坐标显示
plt.xlabel("date")
# 设置y坐标显示
plt.ylabel("value")

# 设置图片的主题
plt.title("show picture")

# 显示图像
plt.show()

"""

# 示例3:
"""
info = pd.read_csv("test.csv")

print(type(info))
plt.plot(info["DATE"],info["VALUE"])
plt.show()
"""

# 示例4:自己造数据,进行画图

x = [1,2,3,4]

y = [1,2,3,4]

line = plt.plot(x,y)

# 设置x轴坐标范围
plt.xlim((0,5))

# 设置y轴坐标范围
plt.ylim((0,5))

# 设置线的颜色、线的宽度
plt.setp(line, color='r', linewidth=20.0)

plt.show()