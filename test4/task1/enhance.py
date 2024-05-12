import cv2
import numpy as np

# 读取图像
image = cv2.imread('E:/20212333Python\demo09_AnalisisData/test4\pic\words3.jpg')

# 对比度增强
alpha = 1.5  # 对比度增强参数，可根据需要调整
image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)

# 亮度增强
beta = 30  # 亮度增强参数，可根据需要调整
image = cv2.convertScaleAbs(image, alpha=1, beta=beta)

# 灰度化
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 锐化
sharpening_filter = np.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])  # 锐化滤波器
sharpened_image = cv2.filter2D(binary_image, -1, sharpening_filter)

# 显示原始图像和增强后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('E:/20212333Python\demo09_AnalisisData/test4\pic/'+ "enhance3" +'.png', binary_image)
