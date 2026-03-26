import os


def list_image_files(directory):
    # 允许的图片扩展名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

    try:
        # 获取指定目录中的所有文件和文件夹
        files = os.listdir(directory)

        # 过滤并输出图片文件名
        for file in files:
            if file.lower().endswith(image_extensions):
                print(file)

    except FileNotFoundError:
        print(f"The directory '{directory}' was not found.")


# 你可以在这里指定文件夹路径
folder_path = 'E:\AIR-PV-ALL\AIR-PV-ALL\Visualized_Masks'
list_image_files(folder_path)
