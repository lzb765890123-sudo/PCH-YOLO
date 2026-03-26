import os
import xml.etree.ElementTree as ET


# 转换YOLO格式到VOC格式的函数
def convert_yolo_to_voc(yolo_data, image_width, image_height, image_filename, class_names, output_dir):
    # 创建XML根元素
    annotation = ET.Element('annotation')

    # 添加文件名和图像大小信息
    folder = ET.SubElement(annotation, 'folder')
    folder.text = 'VOC'

    filename = ET.SubElement(annotation, 'filename')
    filename.text = image_filename

    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(image_width)

    height = ET.SubElement(size, 'height')
    height.text = str(image_height)

    depth = ET.SubElement(size, 'depth')
    depth.text = '3'  # assuming RGB images

    # YOLO数据转换为VOC数据
    for obj in yolo_data:
        class_id, x_center, y_center, width, height = obj

        # 转换为像素坐标
        xmin = int((x_center - width / 2) * image_width)
        ymin = int((y_center - height / 2) * image_height)
        xmax = int((x_center + width / 2) * image_width)
        ymax = int((y_center + height / 2) * image_height)

        # 创建对象元素
        object_elem = ET.SubElement(annotation, 'object')

        # 类别名称
        name = ET.SubElement(object_elem, 'name')
        name.text = class_names[int(class_id)]  # 使用class_id获取类别名

        # 边界框
        bndbox = ET.SubElement(object_elem, 'bndbox')
        xmin_elem = ET.SubElement(bndbox, 'xmin')
        xmin_elem.text = str(xmin)
        ymin_elem = ET.SubElement(bndbox, 'ymin')
        ymin_elem.text = str(ymin)
        xmax_elem = ET.SubElement(bndbox, 'xmax')
        xmax_elem.text = str(xmax)
        ymax_elem = ET.SubElement(bndbox, 'ymax')
        ymax_elem.text = str(ymax)

    # 保存XML文件
    tree = ET.ElementTree(annotation)
    output_path = os.path.join(output_dir, f"{os.path.splitext(image_filename)[0]}.xml")
    tree.write(output_path)


# 遍历文件夹，转换所有YOLO格式的txt文件为VOC格式
def convert_yolo_folder(yolo_folder, output_folder, image_width, image_height, class_names):
    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(yolo_folder):
        if filename.endswith(".txt"):
            # 获取文件路径
            yolo_filepath = os.path.join(yolo_folder, filename)

            # 读取YOLO格式数据
            with open(yolo_filepath, "r") as file:
                yolo_data = []
                for line in file:
                    line = line.strip().split()
                    class_id = int(line[0])
                    x_center = float(line[1])
                    y_center = float(line[2])
                    width = float(line[3])
                    height = float(line[4])
                    yolo_data.append((class_id, x_center, y_center, width, height))

            # 假设图像文件名与txt文件名相同，且在同一文件夹中
            image_filename = f"{os.path.splitext(filename)[0]}.jpg"  # 这里假设是jpg格式的图像
            convert_yolo_to_voc(yolo_data, image_width, image_height, image_filename, class_names, output_folder)


# 示例数据
yolo_folder = "D:\wemap\data_yqb\labels(wudian)"  # YOLO格式txt文件所在的文件夹
output_folder = "D:\wemap\data_yqb/voc"  # 输出VOC格式xml文件的文件夹
image_width = 416  # 图像宽度
image_height = 416  # 图像高度
class_names = ["0"]  # 类别名称

# 调用函数进行转换
convert_yolo_folder(yolo_folder, output_folder, image_width, image_height, class_names)
