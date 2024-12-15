from ultralytics import YOLO

model = YOLO('<path to model.pt>')
folder_path = "<path to folder containing images>"
model.predict(
    source=folder_path, save_txt=False, save_conf=True,
    save_crop=False, show_boxes=True, save=True, conf=0.5
)
