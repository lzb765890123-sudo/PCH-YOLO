import warnings  # 导入warnings模块，用来控制Python中各种警告信息的显示行为

warnings.filterwarnings('ignore')  # 忽略所有的警告信息，避免在控制台输出干扰信息

from ultralytics import YOLO  # 从ultralytics包中导入YOLO类，用于模型创建、训练等操作

if __name__ == '__main__':  # 判断当前脚本是否作为主程序执行，若是则执行下面代码
    # 创建一个YOLO模型实例，使用配置文件hyper-yolo.yaml
    # 配置文件中包含了模型结构、超参数等内容
    model = YOLO(r'D:\Hyper-YOLO-main\ultralytics\cfg\models\hyper-yolo\hyper-yolo.yaml')

    # 如果需要在训练前加载预训练模型权重，可以解除下面的注释
    model.load('D:\Hyper-YOLO-main\yolo11n.pt')  # 加载预训练权重yolo11n.pt

    # 调用model.train()方法开始训练，传入各种训练相关的参数
    model.train(
        data=r'D:\Hyper-YOLO-main\dataset\data.yaml',  # 数据集配置文件，其中包含训练和验证集的路径、类别信息等
        cache=False,  # 是否对数据进行缓存，False表示不进行缓存
        imgsz=416,  # 输入图像的尺寸
        epochs=300,  # 训练的总轮数
        batch=16,  # 批次大小(Batch Size)
        close_mosaic=0,  # 是否关闭mosaic数据增强，0表示默认开启
        workers=1,  # 数据加载的线程/进程数
        device='cuda:0',  # 指定计算设备，如果有GPU可以改为'cuda'或者'cuda:0'
        optimizer='SGD',  # 优化器类型，这里采用SGD
        project='runs/train',  # 保存训练结果（日志、权重等）的主目录
        name='exp',  # 本次训练的名称，结果将保存在runs/train/exp目录下
    )
