import cv2 as cv

img = cv.imread("C:/Users/Administrator/Desktop/1.png")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)




