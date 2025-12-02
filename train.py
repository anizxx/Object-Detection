"""
Training Script for Custom Object Detection Model
Supports training YOLOv8 on custom datasets
"""

import argparse
from ultralytics import YOLO
from pathlib import Path


def train_model(model_size='n', data_config=None, epochs=100, imgsz=640, batch=16, 
                device='cpu', project='runs/detect', name='custom_model'):
    """
    Train a YOLOv8 model on custom dataset
    
    Args:
        model_size: Model size - 'n' (nano), 's' (small), 'm' (medium), 'l' (large), 'x' (xlarge)
        data_config: Path to dataset YAML config file
        epochs: Number of training epochs
        imgsz: Image size for training
        batch: Batch size
        device: Device to use ('cpu', 'cuda', or device number)
        project: Project directory
        name: Experiment name
    """
    
    # Load model
    model_name = f'yolov8{model_size}.pt'
    print(f"Loading model: {model_name}")
    model = YOLO(model_name)
    
    if data_config is None:
        print("Error: Dataset configuration file is required!")
        print("Create a YAML file with dataset paths. See dataset_example.yaml")
        return
    
    # Check if data config exists
    if not Path(data_config).exists():
        print(f"Error: Dataset config file not found: {data_config}")
        return
    
    print(f"Training on dataset: {data_config}")
    print(f"Epochs: {epochs}, Image size: {imgsz}, Batch size: {batch}")
    print(f"Device: {device}\n")
    
    # Train the model
    results = model.train(
        data=data_config,
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        device=device,
        project=project,
        name=name,
        save=True,
        plots=True
    )
    
    print("\nTraining completed!")
    print(f"Best model saved to: {model.trainer.best}")
    print(f"Results saved to: {Path(project) / name}")
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Train YOLOv8 Object Detection Model')
    parser.add_argument('--model', type=str, default='n',
                        choices=['n', 's', 'm', 'l', 'x'],
                        help='Model size: n (nano), s (small), m (medium), l (large), x (xlarge)')
    parser.add_argument('--data', type=str, required=True,
                        help='Path to dataset YAML configuration file')
    parser.add_argument('--epochs', type=int, default=100,
                        help='Number of training epochs (default: 100)')
    parser.add_argument('--imgsz', type=int, default=640,
                        help='Image size for training (default: 640)')
    parser.add_argument('--batch', type=int, default=16,
                        help='Batch size (default: 16)')
    parser.add_argument('--device', type=str, default='cpu',
                        help='Device to use: cpu, cuda, or device number (default: cpu)')
    parser.add_argument('--project', type=str, default='runs/detect',
                        help='Project directory (default: runs/detect)')
    parser.add_argument('--name', type=str, default='custom_model',
                        help='Experiment name (default: custom_model)')
    
    args = parser.parse_args()
    
    train_model(
        model_size=args.model,
        data_config=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=args.project,
        name=args.name
    )


if __name__ == "__main__":
    main()

