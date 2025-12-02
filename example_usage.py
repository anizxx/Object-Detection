"""
Example usage of the object detection system
This script demonstrates various ways to use the detection functionality
"""

from ultralytics import YOLO
import cv2
from pathlib import Path


def example_image_detection():
    """Example: Detect objects in an image"""
    print("Example 1: Image Detection")
    print("-" * 40)
    
    # Load model
    model = YOLO('yolov8n.pt')
    
    # For this example, you would use an actual image path
    # image_path = "path/to/your/image.jpg"
    # results = model(image_path)
    # results[0].save("output/detected_image.jpg")
    
    print("To detect objects in an image, use:")
    print("  python detect.py --source path/to/image.jpg --output output")
    print()


def example_video_detection():
    """Example: Detect objects in a video"""
    print("Example 2: Video Detection")
    print("-" * 40)
    
    print("To detect objects in a video, use:")
    print("  python detect.py --source path/to/video.mp4 --output output")
    print()


def example_webcam_detection():
    """Example: Real-time webcam detection"""
    print("Example 3: Webcam Detection")
    print("-" * 40)
    
    print("To detect objects from webcam, use:")
    print("  python detect.py --source webcam")
    print("Press 'q' to quit")
    print()


def example_custom_model():
    """Example: Using a custom trained model"""
    print("Example 4: Custom Model")
    print("-" * 40)
    
    print("To use a custom trained model, use:")
    print("  python detect.py --source image.jpg --model runs/detect/custom_model/weights/best.pt")
    print()


def example_programmatic_usage():
    """Example: Using the model programmatically"""
    print("Example 5: Programmatic Usage")
    print("-" * 40)
    
    code_example = '''
# Load model
from ultralytics import YOLO
model = YOLO('yolov8n.pt')

# Detect objects in an image
results = model('image.jpg')

# Process results
for result in results:
    boxes = result.boxes
    for box in boxes:
        # Get class name and confidence
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]
        
        # Get bounding box coordinates
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        
        print(f"Detected: {class_name} ({confidence:.2%}) at [{x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f}]")
    
    # Save annotated image
    result.save('output.jpg')
'''
    print(code_example)
    print()


def main():
    print("=" * 50)
    print("Object Detection ML Project - Usage Examples")
    print("=" * 50)
    print()
    
    example_image_detection()
    example_video_detection()
    example_webcam_detection()
    example_custom_model()
    example_programmatic_usage()
    
    print("=" * 50)
    print("For more information, see README.md")
    print("=" * 50)


if __name__ == "__main__":
    main()

