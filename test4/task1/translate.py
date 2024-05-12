import cv2
import os

import numpy as np

# 指定输入图像文件夹和输出文件夹
input_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/cut"
output_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/translated"


# 定义平移参数（单位：像素）
translations = [(0, -10), (0, 10), (-10, 0), (10, 0)]  # 分别表示上、下、左、右移动的像素数

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # 读取图像
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # 获取图像高度和宽度
        height, width = image.shape[:2]

        # 循环应用平移变换
        for dx, dy in translations:
            # 定义平移矩阵
            M = np.float32([[1, 0, dx], [0, 1, dy]])

            # 应用平移变换
            translated_image = cv2.warpAffine(image, M, (width, height))

            # 根据平移方向和大小动态确定裁剪区域
            if dx < 0:
                left = 0
                right = width - abs(dx)
            else:
                left = abs(dx)
                right = width
            if dy < 0:
                top = 0
                bottom = height - abs(dy)
            else:
                top = abs(dy)
                bottom = height

            # 裁剪图像
            cropped_image = translated_image[top:bottom, left:right]

            # 调整大小为30x30像素
            resized_image = cv2.resize(cropped_image, (30, 30))

            # 生成新文件名
            output_filename = os.path.splitext(filename)[0] + f"_translated_{dx}_{dy}.png"

            # 保存平移后的图像
            cv2.imwrite(os.path.join(output_folder, output_filename), resized_image)

print("图像扩容完成！")
