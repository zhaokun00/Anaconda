import cv2 as cv

# https://blog.csdn.net/Shenpibaipao/article/details/82695775
# https://www.cnblogs.com/lclblack/p/6377710.html
img = cv.imread("C:/Users/Administrator/Desktop/1.png")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)

