from ultralytics import YOLO

model = YOLO("yolo11m.pt")

model.train(
    data="dataset_custom.yaml", epochs=50,
    batch=8, imgsz=640, workers=0, device="cuda"
)
