import os
import shutil
import random

# 文件夹路径
images_dir = 'C:/Users\lizhaobo\Desktop\data_cs\w_forest\images/train'
labels_dir = 'C:/Users\lizhaobo\Desktop\data_cs\w_forest\labels/train'
val_images_dir = 'C:/Users\lizhaobo\Desktop\data_cs\w_forest\images/val'
val_labels_dir = 'C:/Users\lizhaobo\Desktop\data_cs\w_forest\labels/val'

# 确保验证集文件夹存在，如果没有则创建
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 获取所有图像文件
image_files = os.listdir(images_dir)

# 随机选择 30% 的文件作为验证集
val_size = int(len(image_files) * 0.3)
val_files = random.sample(image_files, val_size)

# 遍历选择的验证集文件
for file_name in val_files:
    # 图像文件路径
    image_path = os.path.join(images_dir, file_name)
    label_file_name = file_name.replace('.jpg', '.txt')  # 假设标签文件是 .txt 格式，根据实际情况调整
    label_path = os.path.join(labels_dir, label_file_name)

    # 移动图像和标签文件到验证集目录
    shutil.move(image_path, os.path.join(val_images_dir, file_name))
    shutil.move(label_path, os.path.join(val_labels_dir, label_file_name))

print("训练集和验证集划分完成！")
