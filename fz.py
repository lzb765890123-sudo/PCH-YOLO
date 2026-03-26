import os
import shutil

# 定义文件夹路径
images_dir = 'C:/Users\lizhaobo\Desktop\data_gl'
labels_dir = 'D:\wemap\data_yqb\labels(wudian)'

# 遍历images文件夹中的每个子文件夹
for category in os.listdir(images_dir):
    category_path = os.path.join(images_dir, category)

    # 确保当前项是文件夹
    if os.path.isdir(category_path):
        # 在每个子文件夹下查找图像文件
        for image_name in os.listdir(category_path):
            # 这里假设图像文件名和label文件名相同，且图像文件是 .jpg、.png 等
            if image_name.endswith(('.jpg', '.png')):
                # 构建标签文件名
                label_name = image_name.split('.')[0] + '.txt'
                label_path = os.path.join(labels_dir, label_name)

                # 检查对应的标签文件是否存在
                if os.path.exists(label_path):
                    # 确保目标路径的labels文件夹存在
                    labels_folder_path = os.path.join(category_path, 'labels')
                    if not os.path.exists(labels_folder_path):
                        os.makedirs(labels_folder_path)

                    # 复制标签文件到目标位置
                    shutil.copy(label_path, os.path.join(labels_folder_path, label_name))
                    print(f"标签文件 {label_name} 已复制到 {labels_folder_path}")
