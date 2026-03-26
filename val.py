import warnings  # 导入warnings模块，用来控制Python中各种警告信息的显示行为

warnings.filterwarnings('ignore')  # 忽略所有的警告信息，避免在控制台输出干扰信息

from ultralytics import YOLO  # 从ultralytics包中导入YOLO类，用于模型加载、验证等操作

if __name__ == '__main__':  # 判断当前脚本是否作为主程序执行，若是则执行下面代码
    # 创建一个YOLO模型实例，这里直接加载训练好的best.pt权重文件
    model = YOLO('runs/train/exp/weights/best.pt')

    # 使用model.val()方法进行验证，传入各项验证参数
    model.val(
        data='D:/Hyper-YOLO-main/dataset/data.yaml',  # 数据集配置文件，其中包含训练集和验证集的路径、类别等信息
        split='val',  # 指定要使用的数据划分，这里选择验证集(val)
        imgsz=640,  # 输入图像的尺寸
        batch=16,  # 验证时的批次大小
        project='runs/val',  # 保存验证结果（日志、输出文件等）的主目录
        name='exp',  # 本次验证的名称，结果将保存在runs/val/exp目录下
    )
