# import os
# import json
#
#
# def yolo_to_labelme(yolo_file_path, image_name, image_width, image_height):
#     shapes = []
#
#     # 打开YOLO格式的标注文件
#     with open(yolo_file_path, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             class_id = parts[0]  # 类别ID
#             center_x = float(parts[1]) * image_width
#             center_y = float(parts[2]) * image_height
#             width = float(parts[3]) * image_width
#             height = float(parts[4]) * image_height
#
#             # 计算矩形的左上角和右下角
#             x1 = center_x - width / 2
#             y1 = center_y - height / 2
#             x2 = center_x + width / 2
#             y2 = center_y + height / 2
#
#             # 构建shapes中的条目
#             shape = {
#                 "label": class_id,
#                 "points": [[x1, y1], [x2, y2]],
#                 "group_id": None,
#                 "description": "",
#                 "shape_type": "rectangle",
#                 "flags": {},
#                 "mask": None
#             }
#             shapes.append(shape)
#
#     # 构建最终的LabelMe格式JSON
#     labelme_data = {
#         "version": "5.5.0",
#         "flags": {},
#         "shapes": shapes,
#         "imagePath": image_name,
#         "imageData": None,
#         "imageHeight": image_height,
#         "imageWidth": image_width
#     }
#
#     return labelme_data
#
#
# def convert_yolo_to_labelme(yolo_folder, output_folder, image_width, image_height):
#     # 遍历YOLO文件夹中的所有标注文件（假设每个图片对应一个标注文件）
#     for file_name in os.listdir(yolo_folder):
#         if file_name.endswith(".txt"):  # 假设标注文件是.txt文件
#             yolo_file_path = os.path.join(yolo_folder, file_name)
#             image_name = file_name.replace(".txt", ".jpg")  # 假设图片文件是.jpg格式
#             labelme_data = yolo_to_labelme(yolo_file_path, image_name, image_width, image_height)
#
#             # 输出JSON文件
#             output_json_path = os.path.join(output_folder, file_name.replace(".txt", ".json"))
#             with open(output_json_path, 'w') as json_file:
#                 json.dump(labelme_data, json_file, indent=4)
#
#
# # 示例：转换YOLO格式的标注文件夹为LabelMe格式JSON
# yolo_folder = "D:\wemap\data_yqb\labels"  # YOLO格式的标注文件夹
# output_folder = "D:\wemap\data_yqb\json"  # 输出LabelMe格式的文件夹
# image_width = 416  # 假设图像宽度
# image_height = 416  # 假设图像高度
#
# convert_yolo_to_labelme(yolo_folder, output_folder, image_width, image_height)

# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def yolo_to_bbox(center_x, center_y, width, height, image_width, image_height):
#     # 转换YOLO的标注为矩形框的坐标
#     x1 = (center_x - width / 2) * image_width
#     y1 = (center_y - height / 2) * image_height
#     x2 = (center_x + width / 2) * image_width
#     y2 = (center_y + height / 2) * image_height
#     return int(x1), int(y1), int(x2), int(y2)
#
#
# def visualize_labels(image_path, label_path, image_width, image_height):
#     # 读取图像
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 将BGR转为RGB，方便用matplotlib显示
#
#     # 读取YOLO格式标注
#     with open(label_path, 'r') as file:
#         lines = file.readlines()
#
#     for line in lines:
#         parts = line.strip().split()
#
#         # 读取YOLO数据
#         class_id = int(float(parts[0]))  # 将浮动数字转为整数
#         center_x, center_y, width, height = map(float, parts[1:5])
#
#         # 获取矩形框坐标
#         x1, y1, x2, y2 = yolo_to_bbox(center_x, center_y, width, height, image_width, image_height)
#
#         # 画矩形框
#         cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # 红色矩形框
#
#         # 读取最后三个点的坐标
#         points = list(map(float, parts[5:]))
#
#         # 绘制三个点，红色、绿色、蓝色
#         for i, (px, py) in enumerate(zip(points[::2], points[1::2])):
#             px, py = int(px * image_width), int(py * image_height)
#             if i == 0:
#                 color = (255, 0, 0)  # 红色
#             elif i == 1:
#                 color = (0, 255, 0)  # 绿色
#             elif i == 2:
#                 color = (0, 0, 255)  # 蓝色
#             cv2.circle(image, (px, py), 5, color, -1)  # 在点位置画圆
#
#     # 使用matplotlib显示图像
#     plt.imshow(image)
#     plt.axis('off')  # 不显示坐标轴
#     plt.show()
#
#
# def process_images_and_labels(images_folder, labels_folder, image_width, image_height):
#     # 遍历图像文件夹和标签文件夹
#     for file_name in os.listdir(labels_folder):
#         if file_name.endswith(".txt"):
#             label_path = os.path.join(labels_folder, file_name)
#             image_name = file_name.replace(".txt", ".jpg")  # 假设图像格式是.jpg
#             image_path = os.path.join(images_folder, image_name)
#
#             # 可视化标注
#             visualize_labels(image_path, label_path, image_width, image_height)
#
#
# # 示例使用
# images_folder = "D:\wemap\data_yqb\huitu"  # 图像文件夹路径
# labels_folder = "D:\wemap\data_yqb\huitulabel wyy"  # 标注文件夹路径
# image_width = 416  # 图像宽度
# image_height = 416  # 图像高度
#
# process_images_and_labels(images_folder, labels_folder, image_width, image_height)
# #

# import json
# import os
# from PIL import Image
#
#
# # 读取和转换JSON数据为YOLO格式
# def convert_to_yolo_format(json_data, image_width, image_height):
#     yolo_data = []
#
#     # 获取目标框和关键点的坐标
#     rectangles = []
#     points = []
#
#     # 提取矩形框
#     for shape in json_data['shapes']:
#         if shape['shape_type'] == 'rectangle':
#             label = int(shape['label'])  # 类别
#             points_rect = shape['points']
#             x_min, y_min = points_rect[0]
#             x_max, y_max = points_rect[1]
#
#             # 计算矩形框的中心点和宽高
#             x_center = (x_min + x_max) / 2 / image_width
#             y_center = (y_min + y_max) / 2 / image_height
#             width = (x_max - x_min) / image_width
#             height = (y_max - y_min) / image_height
#
#             rectangles.append((label, x_center, y_center, width, height, (x_min, y_min, x_max, y_max)))
#
#         elif shape['shape_type'] == 'point':
#             label = int(shape['label'])  # 关键点的类别
#             points.append((label, shape['points'][0]))
#
#     # 确保每个关键点属于相应的矩形框
#     for rectangle in rectangles:
#         label, x_center, y_center, width, height, rect_coords = rectangle
#         keypoints_normalized = []
#
#         for point in points:
#             p_label, (x, y) = point
#             if rect_coords[0] <= x <= rect_coords[2] and rect_coords[1] <= y <= rect_coords[3]:
#                 # 归一化关键点坐标
#                 x_key = x / image_width
#                 y_key = y / image_height
#                 keypoints_normalized.extend([x_key, y_key])
#
#         # 拼接YOLO格式字符串
#         yolo_line = f"{label} {x_center} {y_center} {width} {height} " + " ".join(map(str, keypoints_normalized))
#         yolo_data.append(yolo_line)
#
#     return yolo_data
#
#
# # 主函数：遍历JSON文件夹并进行转换
# def process_json_to_yolo(json_folder, images_folder, output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # 遍历json文件夹中的所有JSON文件
#     for json_filename in os.listdir(json_folder):
#         if json_filename.endswith('.json'):
#             json_path = os.path.join(json_folder, json_filename)
#
#             # 读取对应的json文件
#             with open(json_path, 'r') as f:
#                 json_data = json.load(f)
#
#             # 获取图片的尺寸
#             image_filename = json_filename.replace('.json', '.jpg')  # 假设图像文件是jpg格式，与你的图像文件命名一致
#             image_path = os.path.join(images_folder, image_filename)
#
#             # 获取图像的宽高
#             with Image.open(image_path) as img:
#                 image_width, image_height = img.size
#
#             # 转换成YOLO格式
#             yolo_data = convert_to_yolo_format(json_data, image_width, image_height)
#
#             # 保存YOLO格式的标注文件
#             yolo_filename = os.path.join(output_folder, json_filename.replace('.json', '.txt'))
#             with open(yolo_filename, 'w') as f:
#                 for line in yolo_data:
#                     f.write(line + '\n')
#             print(f"Processed {json_filename}, saved to {yolo_filename}")
#
#
# # 设置路径
# json_folder = 'D:\wemap\data_yqb\json'  # JSON文件夹路径
# images_folder = 'D:\wemap\data_yqb\images'  # 图片文件夹路径
# output_folder = 'D:\wemap\data_yqb\labels(youdian)'  # YOLO格式输出文件夹
#
# process_json_to_yolo(json_folder, images_folder, output_folder)


import os
import json
from pathlib import Path
from PIL import Image

def yolo_to_coco(images_dir, labels_dir, output_json, class_names):
    # 初始化COCO格式的字典
    coco = {
        "images": [],
        "annotations": [],
        "categories": [{"id": i, "name": name} for i, name in enumerate(class_names, start=1)]
    }

    image_id = 1
    annotation_id = 1

    # 获取所有图片文件
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]

    for image_file in image_files:
        # 获取图像的尺寸
        image_path = os.path.join(images_dir, image_file)
        image = Image.open(image_path)
        width, height = image.size

        # 添加图像信息到COCO格式
        coco["images"].append({
            "id": image_id,
            "file_name": image_file,
            "width": width,
            "height": height
        })

        # 处理标注文件
        label_file = os.path.join(labels_dir, Path(image_file).stem + '.txt')
        if os.path.exists(label_file):
            with open(label_file, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    class_id = int(parts[0])  # YOLO类标签
                    x_center = float(parts[1])  # 中心点的x坐标（归一化）
                    y_center = float(parts[2])  # 中心点的y坐标（归一化）
                    bbox_width = float(parts[3])  # 物体的宽度（归一化）
                    bbox_height = float(parts[4])  # 物体的高度（归一化）

                    # 计算真实的坐标（将归一化的坐标转换为像素坐标）
                    x_min = (x_center - bbox_width / 2) * width
                    y_min = (y_center - bbox_height / 2) * height
                    bbox_width = bbox_width * width
                    bbox_height = bbox_height * height

                    # 添加标注信息到COCO格式
                    coco["annotations"].append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": class_id + 1,  # YOLO class_id 从0开始，COCO从1开始
                        "bbox": [x_min, y_min, bbox_width, bbox_height],
                        "area": bbox_width * bbox_height,
                        "iscrowd": 0
                    })
                    annotation_id += 1

        image_id += 1

    # 将COCO格式的字典写入JSON文件
    with open(output_json, 'w') as json_file:
        json.dump(coco, json_file, indent=4)

# 定义类名称（根据你的标注，确保类名称正确）
class_names = ["wind_tubine"]  # 这里只是示例，替换为你实际的类别名称

# 输入路径和输出路径
images_dir = 'D:\wemap\data_yqb\images'
labels_dir = 'D:\wemap\data_yqb\labels(wudian)'
output_json = 'D:\wemap\data_yqb\coco/coco_annotations.json'

# 转换YOLO标注为COCO格式
yolo_to_coco(images_dir, labels_dir, output_json, class_names)

