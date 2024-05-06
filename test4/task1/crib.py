import os

# 重命名test4/pic/cut中带数字图片
path = 'E:/20212333Python\demo09_AnalisisData/test4\pic\cut'
for root, dirs, files in os.walk(path):
    for i, filename in enumerate(files):
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, f'{i}.png')
        try:
            os.rename(old_file, new_file)
            print(f"已重命名: {old_file} 到 {new_file}")
        except OSError as e:
            print(f"无法重命名文件 {filename}: {e}")

