import warnings  # 导入warnings模块，用来控制Python中各种警告信息的显示行为

warnings.filterwarnings('ignore')  # 忽略所有的警告信息，避免在控制台输出干扰信息

from ultralytics import YOLO  # 从ultralytics包中导入YOLO类，用于模型加载、推理等操作

if __name__ == '__main__':  # 判断当前脚本是否作为主程序执行，若是则执行下面代码
    # 1. 创建一个YOLO模型实例，加载训练好的best.pt权重文件
    model = YOLO('D:\Hyper-YOLO-main/runs/train\exp3\weights/best.pt')  # 这里可根据实际路径修改为自己的模型权重文件

    # 2. 调用model.predict()方法，对指定的图片或文件夹进行推理（检测）
    model.predict(
        source='D:\Hyper-YOLO-main\dataset\images/test',  # 待检测的数据所在的路径，可以是单张图片、视频或文件夹
        imgsz=640,  # 推理时的图像输入尺寸
        project='runs/detect',  # 推理结果保存的根目录
        name='exp',  # 本次推理的名称，结果将保存在runs/detect/exp目录下
        save=True,  # 是否保存检测后的结果图像或视频
    )
