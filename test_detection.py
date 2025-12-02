"""
Quick test script to verify object detection is working
"""

import numpy as np
from PIL import Image
from pathlib import Path
from ultralytics import YOLO
import os

def create_test_image():
    """Create a simple test image"""
    # Create a simple colored image
    img = Image.new('RGB', (640, 480), color='lightblue')
    
    # Add some shapes that might be detected
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Draw a rectangle (might be detected as various objects)
    draw.rectangle([100, 100, 300, 300], fill='red', outline='black', width=3)
    draw.ellipse([350, 150, 550, 350], fill='green', outline='black', width=3)
    
    test_image_path = 'test_image.jpg'
    img.save(test_image_path)
    print(f"Created test image: {test_image_path}")
    return test_image_path

def test_detection():
    """Test the object detection"""
    print("=" * 50)
    print("Testing Object Detection System")
    print("=" * 50)
    print()
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Load model (will download on first use)
    print("Loading YOLOv8 model (this may download on first use)...")
    try:
        model = YOLO('yolov8n.pt')
        print("✓ Model loaded successfully!")
        print()
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        return
    
    # Create test image
    print("Creating test image...")
    test_image = create_test_image()
    
    # Run detection
    print(f"Running detection on {test_image}...")
    try:
        results = model(test_image, conf=0.25)
        print("✓ Detection completed!")
        print()
        
        # Save results
        output_path = 'output/test_detection_result.jpg'
        results[0].save(output_path)
        print(f"✓ Results saved to: {output_path}")
        print()
        
        # Print detected objects
        print("Detected Objects:")
        print("-" * 30)
        detections = []
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]
            detections.append((class_name, confidence))
        
        if detections:
            for class_name, confidence in detections:
                print(f"  - {class_name}: {confidence:.2%}")
        else:
            print("  No objects detected (this is normal for a simple test image)")
        
        print()
        print("=" * 50)
        print("Test completed successfully!")
        print("=" * 50)
        print()
        print("You can now use the detection system:")
        print("  python detect.py --source webcam")
        print("  python detect.py --source path/to/image.jpg")
        
    except Exception as e:
        print(f"✗ Error during detection: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_detection()

