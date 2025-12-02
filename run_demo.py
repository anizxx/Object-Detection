"""
Interactive demo of the object detection system
"""

import sys
from ultralytics import YOLO
import os

def main():
    print("=" * 60)
    print("OBJECT DETECTION ML PROJECT - DEMO")
    print("=" * 60)
    print()
    
    # Check if test image exists
    if os.path.exists('test_image.jpg'):
        print("✓ Test image found")
        image_path = 'test_image.jpg'
    else:
        print("Creating test image...")
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (640, 480), color='lightblue')
        draw = ImageDraw.Draw(img)
        draw.rectangle([100, 100, 300, 300], fill='red', outline='black', width=3)
        draw.ellipse([350, 150, 550, 350], fill='green', outline='black', width=3)
        img.save('test_image.jpg')
        image_path = 'test_image.jpg'
        print("✓ Test image created")
    
    print()
    print("Loading YOLOv8 model...")
    try:
        model = YOLO('yolov8n.pt')
        print("✓ Model loaded successfully!")
        print()
    except Exception as e:
        print(f"✗ Error: {e}")
        return
    
    print(f"Running detection on: {image_path}")
    print("-" * 60)
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Run detection
    results = model(image_path, conf=0.25)
    
    # Save results
    output_path = 'output/demo_result.jpg'
    results[0].save(output_path)
    
    print()
    print("Detection Results:")
    print("-" * 60)
    
    detections = []
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]
        detections.append((class_name, confidence))
    
    if detections:
        for i, (class_name, confidence) in enumerate(detections, 1):
            print(f"{i}. {class_name}: {confidence:.2%}")
    else:
        print("No objects detected (this is normal for a simple test image)")
    
    print()
    print("-" * 60)
    print(f"✓ Result saved to: {output_path}")
    print()
    print("=" * 60)
    print("SYSTEM IS READY TO USE!")
    print("=" * 60)
    print()
    print("Try these commands:")
    print()
    print("1. Detect objects in an image:")
    print("   python detect.py --source path/to/image.jpg --output output")
    print()
    print("2. Real-time webcam detection:")
    print("   python detect.py --source webcam")
    print()
    print("3. Detect objects in a video:")
    print("   python detect.py --source path/to/video.mp4 --output output")
    print()
    print("4. Use different model sizes:")
    print("   python detect.py --source image.jpg --model yolov8s.pt")
    print()

if __name__ == "__main__":
    main()

