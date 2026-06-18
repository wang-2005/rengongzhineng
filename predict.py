from ultralytics import YOLO

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")
imagepath = r'./image/'
# Run inference on 'bus.jpg' with arguments
model.predict(source=imagepath, save=True, imgsz=640, conf=0.5)
