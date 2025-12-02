"""
Utility functions for object detection project
"""

import cv2
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict
from ultralytics import YOLO


def get_model_info(model_path: str) -> Dict:
    """Get information about a YOLO model"""
    model = YOLO(model_path)
    return {
        'classes': model.names,
        'num_classes': len(model.names),
        'input_size': model.model.args.get('imgsz', 640)
    }


def count_objects(results, class_filter=None) -> Dict[str, int]:
    """
    Count detected objects by class
    
    Args:
        results: YOLO detection results
        class_filter: Optional list of class names to filter
    
    Returns:
        Dictionary with class names as keys and counts as values
    """
    counts = {}
    
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            
            if class_filter is None or class_name in class_filter:
                counts[class_name] = counts.get(class_name, 0) + 1
    
    return counts


def draw_detections(image, boxes, class_names, confidences, 
                   color=(0, 255, 0), thickness=2):
    """
    Draw bounding boxes on image
    
    Args:
        image: Input image (numpy array)
        boxes: List of bounding boxes [x1, y1, x2, y2]
        class_names: List of class names
        confidences: List of confidence scores
        color: Bounding box color (B, G, R)
        thickness: Line thickness
    
    Returns:
        Annotated image
    """
    annotated = image.copy()
    
    for box, class_name, conf in zip(boxes, class_names, confidences):
        x1, y1, x2, y2 = map(int, box)
        
        # Draw rectangle
        cv2.rectangle(annotated, (x1, y1), (x2, y2), color, thickness)
        
        # Draw label
        label = f"{class_name}: {conf:.2f}"
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        label_y = max(y1, label_size[1] + 10)
        
        cv2.rectangle(annotated, (x1, label_y - label_size[1] - 10),
                     (x1 + label_size[0], label_y), color, -1)
        cv2.putText(annotated, label, (x1, label_y - 5),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    return annotated


def save_detection_summary(results, output_path: str):
    """
    Save detection summary to text file
    
    Args:
        results: YOLO detection results
        output_path: Path to save summary file
    """
    with open(output_path, 'w') as f:
        f.write("Object Detection Summary\n")
        f.write("=" * 50 + "\n\n")
        
        for i, result in enumerate(results):
            f.write(f"Frame/Image {i + 1}:\n")
            f.write("-" * 30 + "\n")
            
            counts = count_objects([result])
            for class_name, count in counts.items():
                f.write(f"  {class_name}: {count}\n")
            
            f.write("\n")
    
    print(f"Summary saved to: {output_path}")


def batch_process(model, image_dir: str, output_dir: str, conf_threshold: float = 0.25):
    """
    Process multiple images in a directory
    
    Args:
        model: YOLO model instance
        image_dir: Directory containing images
        output_dir: Directory to save results
        conf_threshold: Confidence threshold
    """
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    image_dir = Path(image_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    image_files = [f for f in image_dir.iterdir() 
                   if f.suffix.lower() in image_extensions]
    
    print(f"Found {len(image_files)} images to process")
    
    for image_file in image_files:
        print(f"Processing: {image_file.name}")
        results = model(str(image_file), conf=conf_threshold)
        output_path = output_dir / f"detected_{image_file.name}"
        results[0].save(str(output_path))
    
    print(f"\nAll images processed. Results saved to: {output_dir}")

