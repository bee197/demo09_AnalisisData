import cv2
import os

import numpy as np

# 指定输入图像文件夹和输出文件夹
input_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/all_rotate_pics"
output_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/noisy"

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # 读取图像
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # 添加高斯噪声
        mean = 0  # 均值
        sigma = 5  # 方差
        noisy_image = np.clip(image.astype(np.float32) + np.random.normal(mean, sigma, image.shape), 0, 255).astype(
            np.uint8)

        # 生成新文件名
        output_filename = os.path.splitext(filename)[0] + "_noisy.png"
        # 保存带有高斯噪声的图像
        cv2.imwrite(os.path.join(output_folder, output_filename), noisy_image)
