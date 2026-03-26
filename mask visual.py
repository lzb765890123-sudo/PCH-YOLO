import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 设置输入文件夹路径
mask_folder = r'E:\AIR-PV-ALL\AIR-PV-ALL\Mask'
# 设置输出文件夹路径
output_folder = r'E:\AIR-PV-ALL\AIR-PV-ALL\Visualized_Masks'

# 如果输出文件夹不存在，创建它
os.makedirs(output_folder, exist_ok=True)

# 获取掩码文件夹中的所有图像文件
mask_files = [f for f in os.listdir(mask_folder) if f.endswith('.png')]

# 将每个掩码图像可视化并保存
for mask_file in mask_files:
    # 构造图像的完整路径
    mask_path = os.path.join(mask_folder, mask_file)

    # 读取图像
    mask_image = Image.open(mask_path)

    # 将图像转换为 numpy array
    mask_array = np.array(mask_image)

    # 创建一个新的保存图像的路径
    output_path = os.path.join(output_folder, mask_file)

    # 使用matplotlib保存图像，应用颜色映射
    plt.figure(figsize=(6, 6))
    plt.imshow(mask_array, cmap='viridis')  # 使用 'viridis' colormap
    plt.axis('off')  # 不显示坐标轴
    plt.tight_layout()

    # 保存图像到输出文件夹
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()  # 关闭图像，释放内存

print(f"所有掩码图像已成功保存到 {output_folder} 文件夹")
