import os

# 设置txt文件存放的文件夹路径
folder_path = 'D:\Hyper-YOLO-main\example_dataset\labels/val'  # 请替换为你存放txt文件的文件夹路径

# 遍历文件夹中的所有txt文件
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        # 打开文件进行读取和处理
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 创建一个新的内容列表，用于保存处理后的内容
        new_lines = []

        # 遍历每行，去掉最后6个数字（关键点坐标）
        for line in lines:
            parts = line.split()
            # 只保留前面的5个数据
            new_line = ' '.join(parts[:5]) + '\n'
            new_lines.append(new_line)

        # 保存修改后的文件
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

print("批量处理完成！")
