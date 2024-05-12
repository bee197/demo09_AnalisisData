import os
import shutil
import random

# 指定包含汉字切图的文件夹
dataset_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/noisy"

# 指定划分后的训练集和测试集文件夹
train_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic\dataset\dataset2/train_dataset"
test_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic\dataset\dataset2/test_dataset"

# 设置划分比例
train_ratio = 0.8

# 获取0-19的所有图像文件
category_files = [file for file in os.listdir(dataset_folder) if int(os.path.splitext(file)[0].split("_")[0]) in range(0, 20)]
# 打乱顺序
random.shuffle(category_files)
# 计算训练集和测试集数量
train_count = int(len(category_files) * train_ratio)
test_count = int(len(category_files) - train_count)
# 将图像文件拷贝到对应的训练集和测试集文件夹中
for i, file in enumerate(category_files):
    src_path = os.path.join(dataset_folder, file)
    dest_folder = train_folder if i < train_count else test_folder
    dest_path = os.path.join(dest_folder, file)
    shutil.copy(src_path, dest_path)

# 获取20-39的所有图像文件
category_files2 = [file for file in os.listdir(dataset_folder) if int(os.path.splitext(file)[0].split("_")[0]) in range(20, 39)]
# 打乱顺序
random.shuffle(category_files2)
# 计算训练集和测试集数量
train_count = int(len(category_files2) * train_ratio)
test_count = int(len(category_files2) - train_count)
# 将图像文件拷贝到对应的训练集和测试集文件夹中
for i, file in enumerate(category_files2):
    src_path = os.path.join(dataset_folder, file)
    dest_folder = train_folder if i < train_count else test_folder
    dest_path = os.path.join(dest_folder, file)
    shutil.copy(src_path, dest_path)

print("数据集划分完成！")
