YOLO11 复现项目
项目简介
本项目基于 Ultralytics YOLO11 框架实现目标检测模型的训练与推理。项目支持对预训练模型进行二次训练（微调），适用于自定义数据集的目标检测任务。

环境配置
硬件要求
GPU: NVIDIA GPU，支持CUDA 11.0+
显存: 至少8GB（训练时batch=8，imgsz=640）
内存: 至少16GB
存储空间: 至少50GB可用空间（包含数据集和模型）
软件要求
操作系统: Windows 11 或 Linux（Ubuntu 18.04+）
Python: 3.8 - 3.11
PyTorch: >= 1.8.0（推荐使用最新稳定版）
CUDA: >= 11.0（GPU训练必需）
依赖安装
方法一：使用 pip 安装
# 安装基础依赖
pip install -r requirements.txt

# 或直接安装 ultralytics（包含所有依赖）
pip install ultralytics>=8.2.34
方法二：安装 PyTorch（可选）
如需手动安装特定版本的 PyTorch，请参考 PyTorch 官方网站

# CUDA 12.1 版本示例
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
数据准备
2.0.zip下包含部分数据集

数据集结构
本项目使用 YOLO 格式的数据集，结构如下：

dataset/
├── images/
│   ├── train/          # 训练集图像
│   ├── val/            # 验证集图像
│   └── test/           # 测试集图像
└── labels/
    ├── train/          # 训练集标注文件
    └── val/            # 验证集标注文件
标注格式
YOLO 格式标注文件为 .txt 文件，每行格式如下：

<class_id> <x_center> <y_center> <width> <height>
class_id: 类别索引（从0开始）
x_center, y_center: 边界框中心坐标（归一化到0-1）
width, height: 边界框宽度和高度（归一化到0-1）
数据集配置文件
项目包含多个数据集配置文件：

文件	描述
z1.yaml	古文数据集配置（62个类别）
配置文件格式示例：	
train: C:/Users/lenovo/Desktop/guwen/images/train
val: C:/Users/lenovo/Desktop/guwen/images/val
test: C:/Users/lenovo/Desktop/guwen/images/test

names:
  0: B_R1
  1: R_R1
  # ... 更多类别
运行步骤
1. 训练模型
二次训练（微调）
使用预训练模型进行二次训练：

python train(2).py
训练脚本 train(2).py 关键参数说明：

参数	默认值	说明
data	z1.yaml	数据集配置文件路径
imgsz	640	输入图像尺寸
epochs	300	训练轮数
batch	8	批次大小
device	0	使用的GPU设备ID
optimizer	SGD	优化器类型
lr0	0.001	初始学习率
amp	True	是否启用混合精度训练
2. 模型推理
使用训练好的模型进行预测：

python predict.py
推理脚本说明：

from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolo11n.pt")
# 或加载自定义训练的模型
# model = YOLO("runs/train/exp/weights/best.pt")
# 运行推理
model.predict(source='./image/', save=True, imgsz=640, conf=0.5)
3. 模型验证
# 使用 CLI 验证
yolo val model=runs/train/exp/weights/best.pt data=z1.yaml

# 使用 Python API
from ultralytics import YOLO
model = YOLO("runs/train/exp/weights/best.pt")
metrics = model.val(data="z1.yaml")
项目结构
├── .github/              # GitHub 配置文件
│   ├── ISSUE_TEMPLATE/   # Issue 模板
│   └── workflows/        # CI/CD 工作流
├── docker/               # Docker 配置
├── docs/                 # 项目文档
├── examples/             # 使用示例
├── runs/                 # 运行结果
│   └── train/           # 检测结果
├── DOTA_devkit-master/   # DOTA 数据集工具包
├── train(2).py           # 训练脚本（二次训练）
├── predict.py            # 推理脚本
├── 11.py                 # YOLO11 相关脚本
├── z1.yaml               # 数据集配置1
├── 2.0.zip               # 部分数据集
├── requirements.txt      # 依赖列表
└── README_YOLO11.md      # 项目说明
文件说明
文件/目录	说明
train(2).py	二次训练脚本，加载预训练模型进行微调
predict.py	推理脚本，对图像进行目标检测
z1.yaml	古文数据集配置，包含62个类别
runs/	训练日志、权重文件和预测结果
DOTA_devkit-master/	DOTA 倾斜目标检测数据集工具包
代码注释说明
训练脚本 train(2).py
# 将已经训练完的pt文件进行二次训练
from ultralytics import YOLO

# 数据集配置文件
data_yaml_path = r'z1.yaml'

# 预训练模型路径
pre_model_name = 'D:/1/best (2).pt'

if __name__ == '__main__':
    # 加载预训练模型
    model = YOLO(pre_model_name)
    
    # 开始训练
    model.train(data=data_yaml_path,
                imgsz=640,        # 输入图像大小
                epochs=300,       # 训练轮数
                batch=8,          # 批次大小
                optimizer='SGD',  # 优化器选择
                device='0',       # GPU设备
                lr0=0.001         # 初始学习率
                )
关键参数说明
参数	说明
data	数据集配置文件路径（必需）
imgsz	输入图像尺寸，如 640、1280
epochs	训练轮数，建议根据数据集大小调整
batch	批次大小，受限于GPU显存
device	指定GPU设备，'0' 表示第一块GPU
optimizer	优化器，可选 SGD、Adam、AdamW
lr0	初始学习率，SGD建议0.01，Adam建议0.001
amp	混合精度训练，加速训练并减少显存占用
resume	续训模式，设置为 True 或上次训练的最后权重路径
常见问题
Q1: 训练时出现 "CUDA out of memory"
解决方案:

减小 batch 大小（如从8改为4）
减小 imgsz（如从640改为416）
关闭 amp（设置为 False）
使用更小的模型（如 yolo11n 代替 yolo11x）
Q2: 训练损失为 NaN
解决方案:

降低初始学习率 lr0（如从0.01改为0.001）
关闭混合精度训练 amp=False
检查数据集标注是否正确
Q3: 模型加载失败
解决方案:

检查预训练模型路径是否正确
确保模型文件存在且未损坏
尝试使用官方预训练模型 yolo11n.pt
参考资料
Ultralytics YOLO11 官方文档
YOLO11 GitHub 仓库
PyTorch 官方文档
许可证
本项目基于 Ultralytics YOLO11，遵循 AGPL-3.0 开源许可证。

