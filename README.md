# KITTI to YOLO Dataset Converter 🛠️

This Python script converts the KITTI dataset format into the YOLOv5/YOLOv8 compatible format (images + annotations in `.txt`, plus a `data.yaml`).

## 📁 Expected Directory Structure

Before running the script, make sure your KITTI data is organized like this:

```
kitti/
├── training/
│   └── image_2/
│       ├── 000000.png
│       ├── 000001.png
│       └── …
├── testing/
│   └── image_2/
│       ├── 000100.png
│       ├── 000101.png
│       └── …
└── label/
├── 000000.txt
├── 000001.txt
└── …
```

- `training/image_2/`: training images  
- `testing/image_2/`: test images (no labels needed)  
- `label/`: KITTI label files corresponding to `training/image_2/`

> 📌 Only objects labeled as `"Car"`, `"Van"`, or `"Truck"` are converted to YOLO format by default. You can customize this in the script.

---

## 🚀 What the Script Does

- Converts KITTI bounding boxes to YOLO normalized format
- Filters only relevant object classes
- Creates the required YOLO directory structure:

```
yolo_dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

- Automatically splits training images into `train` and `val` (default: 80/20)

---

## 🧪 How to Use

1. Make sure your KITTI data is organized as described above.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3.	Run the script:

   ```
   python kitti_to_yolo.py --kitti_dir path/to/kitti --output_dir yolo_dataset
   ```
## 📦 Output

You will get a ready-to-train YOLO dataset with:

- Image splits in images/train/ and images/val/
- YOLO annotation .txt files in labels/train/ and labels/val/
- A data.yaml file for training

## 📝 License

MIT License — feel free to modify, contribute or adapt for your own experiments.

---

Let me know if you'd like to add multi-class support, automatic download of KITTI, or YOLOv8-specific training instructions too.