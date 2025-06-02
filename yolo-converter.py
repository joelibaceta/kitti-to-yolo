import os
import cv2
from pathlib import Path
import yaml

CLASSES = ['Car', 'Van', 'Truck']

# Paths
BASE_DIR = Path("kitti")
KITTI_LABELS = BASE_DIR / "label"
KITTI_IMAGES = BASE_DIR / "training"

YOLO_IMAGES = Path("yolo_dataset/images/train")
YOLO_LABELS = Path("yolo_dataset/labels/train")
YOLO_IMAGES.mkdir(parents=True, exist_ok=True)
YOLO_LABELS.mkdir(parents=True, exist_ok=True)

def convert_kitti_to_yolo():
    for label_file in sorted(KITTI_LABELS.glob("*.txt")):
        img_id = label_file.stem
        img_path = KITTI_IMAGES / f"{img_id}.png"
        if not img_path.exists():
            continue

        img = cv2.imread(str(img_path))
        height, width = img.shape[:2]

        yolo_lines = []
        with open(label_file, "r") as f:
            for line in f:
                items = line.strip().split()
                cls_name = items[0]
                if cls_name not in CLASSES:
                    continue
                cls_id = CLASSES.index(cls_name)
                x1, y1, x2, y2 = map(float, items[4:8])
                xc = (x1 + x2) / 2 / width
                yc = (y1 + y2) / 2 / height
                w = (x2 - x1) / width
                h = (y2 - y1) / height
                yolo_lines.append(f"{cls_id} {xc:.6f} {yc:.6f} {w:.6f} {h:.6f}")

        if yolo_lines:
            yolo_label_path = YOLO_LABELS / f"{img_id}.txt"
            with open(yolo_label_path, "w") as out:
                out.write("\n".join(yolo_lines))
            dest_img = YOLO_IMAGES / f"{img_id}.png"
            os.system(f"cp '{img_path}' '{dest_img}'")

    print("✅ Conversión completada.")

def create_data_yaml():
    yaml_content = {
        'train': 'yolo_dataset/images/train',
        'val': 'yolo_dataset/images/train',
        'nc': len(CLASSES),
        'names': CLASSES
    }
    with open("yolo_dataset/data.yaml", "w") as f:
        yaml.dump(yaml_content, f)
    print("📄 data.yaml creado.")

if __name__ == "__main__":
    convert_kitti_to_yolo()
    create_data_yaml()