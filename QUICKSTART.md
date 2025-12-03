# Quick Start Guide

## ✅ System Status: READY!

Your object detection system is installed and working!

## 🚀 Quick Commands

### 1. Real-time Webcam Detection
```bash
python detect.py --source webcam
```
Press 'q' to quit

### 2. Detect Objects in an Image
```bash
python detect.py --source path/to/your/image.jpg --output output
```

### 3. Detect Objects in a Video
```bash
python detect.py --source path/to/your/video.mp4 --output output
```

### 4. Adjust Confidence Threshold
```bash
python detect.py --source image.jpg --conf 0.5
```
(Lower = more detections, Higher = more confident detections)

### 5. Use Different Model Sizes
```bash
# Faster, less accurate
python detect.py --source image.jpg --model yolov8n.pt

# Slower, more accurate
python detect.py --source image.jpg --model yolov8s.pt
python detect.py --source image.jpg --model yolov8m.pt
python detect.py --source image.jpg --model yolov8l.pt
python detect.py --source image.jpg --model yolov8x.pt
```

## 📊 What Can It Detect?

The system can detect 80 different object classes including:
- People, animals (cat, dog, bird, etc.)
- Vehicles (car, bus, truck, bicycle, etc.)
- Furniture (chair, couch, bed, etc.)
- Electronics (laptop, phone, TV, etc.)
- Food items (apple, banana, pizza, etc.)
- And many more!

## 📁 Output

All detection results are saved in the `output/` folder with bounding boxes and labels drawn on them.

## 🎓 Training Custom Models

To train on your own dataset:
```bash
python train.py --data your_dataset.yaml --epochs 100
```

See `README.md` for detailed instructions.


