import cv2
import os

# 指定输入图像文件夹和输出文件夹
input_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/resize"
output_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/rotate"

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # 读取图像
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # 旋转图像并保存
        for angle in [90, 180, 270]:
            # 旋转图像
            rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 逆时针旋转90度
            if angle == 180:
                rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)  # 再逆时针旋转90度
            if angle == 270:
                rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)  # 再逆时针旋转90度
                rotated_image = cv2.rotate(rotated_image, cv2.ROTATE_90_CLOCKWISE)  # 再逆时针旋转90度
            # 生成新文件名
            output_filename = os.path.splitext(filename)[0] + "_rotated_" + str(angle) + ".png"
            # 保存旋转后的图像
            cv2.imwrite(os.path.join(output_folder, output_filename), rotated_image)

print("图像扩容完成！")
