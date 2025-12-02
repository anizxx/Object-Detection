"""
Object Detection Script
Supports image, video, and webcam detection using YOLOv8
"""

import cv2
import argparse
from pathlib import Path
from ultralytics import YOLO
import os


def detect_image(model, image_path, output_dir="output", conf_threshold=0.25):
    """Detect objects in an image"""
    print(f"Processing image: {image_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Run detection
    results = model(image_path, conf=conf_threshold)
    
    # Save results
    output_path = os.path.join(output_dir, f"detected_{Path(image_path).name}")
    results[0].save(output_path)
    
    # Print detected objects
    print("\nDetected Objects:")
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]
        print(f"  - {class_name}: {confidence:.2%}")
    
    print(f"\nResult saved to: {output_path}")
    return results


def detect_video(model, video_path, output_dir="output", conf_threshold=0.25):
    """Detect objects in a video"""
    print(f"Processing video: {video_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Run detection
    output_path = os.path.join(output_dir, f"detected_{Path(video_path).name}")
    results = model(video_path, conf=conf_threshold, save=True, project=output_dir)
    
    print(f"\nResult saved to: {output_path}")
    return results


def detect_webcam(model, conf_threshold=0.25, camera_index=0):
    """Detect objects from webcam feed"""
    print("Starting webcam detection... Press 'q' to quit")
    
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_index}")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
        
        # Run detection
        results = model(frame, conf=conf_threshold, verbose=False)
        
        # Draw results on frame
        annotated_frame = results[0].plot()
        
        # Display frame
        cv2.imshow('Object Detection', annotated_frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Webcam detection stopped")


def main():
    parser = argparse.ArgumentParser(description='Object Detection using YOLOv8')
    parser.add_argument('--model', type=str, default='yolov8n.pt',
                        help='Path to model file (default: yolov8n.pt)')
    parser.add_argument('--source', type=str, required=True,
                        help='Path to image/video or "webcam" for webcam detection')
    parser.add_argument('--output', type=str, default='output',
                        help='Output directory (default: output)')
    parser.add_argument('--conf', type=float, default=0.25,
                        help='Confidence threshold (default: 0.25)')
    parser.add_argument('--camera', type=int, default=0,
                        help='Camera index for webcam (default: 0)')
    
    args = parser.parse_args()
    
    # Load model
    print(f"Loading model: {args.model}")
    model = YOLO(args.model)
    print("Model loaded successfully!\n")
    
    # Process based on source type
    if args.source.lower() == 'webcam':
        detect_webcam(model, args.conf, args.camera)
    else:
        source_path = Path(args.source)
        if not source_path.exists():
            print(f"Error: Source path does not exist: {args.source}")
            return
        
        # Check if it's an image or video
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
        video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'}
        
        if source_path.suffix.lower() in image_extensions:
            detect_image(model, args.source, args.output, args.conf)
        elif source_path.suffix.lower() in video_extensions:
            detect_video(model, args.source, args.output, args.conf)
        else:
            print(f"Error: Unsupported file format: {source_path.suffix}")
            print(f"Supported image formats: {image_extensions}")
            print(f"Supported video formats: {video_extensions}")


if __name__ == "__main__":
    main()

