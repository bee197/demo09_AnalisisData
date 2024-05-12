import os
import json

# 指定包含汉字切图的文件夹
dataset_folder = "E:/20212333Python\demo09_AnalisisData/test4\pic/all_rotate_pics"

# 创建一个空字典用于存储标签和对应的图像文件路径
labels = {}

# 遍历文件夹中的所有图片文件
for filename in os.listdir(dataset_folder):
    if filename.endswith(".png"):
        # 提取文件名中的数字作为类别信息
        nums = int(os.path.splitext(filename)[0].split("_")[0])
        # 将每个图像文件的路径添加到标签字典中，并以类别作为标签
        category = 0
        if nums in range(0, 20):
            category = 0
        elif nums in range(20, 40):
            category = 1
        labels[filename] = category

# 打印标签字典
print(labels)


# 指定要保存标签的文件路径
labels_file = "labels1.json"

# 存储标签字典到文件
with open(labels_file, "w") as f:
    json.dump(labels, f)

print("标签已保存到文件:", labels_file)
