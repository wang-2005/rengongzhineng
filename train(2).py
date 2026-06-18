# 将已经训练完的pt文件进行二次训练
from ultralytics import YOLO
# 模型配置文件
# model_yaml_path = r'z1.yaml'
# 数据集配置文件
data_yaml_path = r'z1.yaml'
# 预训练模型
pre_model_name = 'D:/1/best (2).pt'

import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(pre_model_name)
    # model = YOLO(model_yaml_path)
    # 如何切换模型版本, 上面的ymal文件可以改为 yolo11s.yaml就是使用的11s,
    # 类似某个改进的yaml文件名称为yolov11-XXX.yaml那么如果想使用其它版本就把上面的名称改为yolov11l-XXX.yaml即可（改的是上面YOLO中间的名字不是配置文件的）！
    # model.load('yolo11n.pt')  # 是否加载预训练权重
    model.train(data=data_yaml_path,
                # 如果大家任务是其它的'ultralytics/cfg/default.yaml'找到这里修改task可以改成detect, segment, classify, pose
                # cache=False,
                imgsz=640,
                epochs=300,
                single_cls=False,  # 是否是单类别检测
                batch=8,
                close_mosaic=0,
                workers=1,
                device='0',
                optimizer='SGD',  # using SGD 优化器 默认为auto建议大家使用固定的.
                # resume=, # 续训的话这里填写True, yaml文件的地方改为lats.pt的地址,需要注意的是如果你设置训练200轮次模型训练了200轮次是没有办法进行续训的.
                amp=True,  # 如果出现训练损失为Nan可以关闭amp
                project='runs/train',
                name='exp',
                lr0=0.001,
                )




























