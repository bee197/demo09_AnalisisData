import os

# 指定包含汉字切图的文件夹
dataset_folder = "chinese_characters_dataset"

# 获取所有汉字类别文件夹
character_folders = [folder for folder in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, folder))]

# 创建一个空字典用于存储标签和对应的图像文件路径
labels = {}

# 遍历每个汉字类别文件夹
for character_folder in character_folders:
    character_path = os.path.join(dataset_folder, character_folder)
    # 获取该类别文件夹中的所有图像文件
    image_files = [file for file in os.listdir(character_path) if file.endswith(".jpg") or file.endswith(".png")]
    # 将每个图像文件的路径添加到标签字典中，并以文件名作为标签
    for image_file in image_files:
        image_path = os.path.join(character_path, image_file)
        labels[image_file] = character_folder

# 打印标签字典
print(labels)
