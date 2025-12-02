"""
Setup script for Object Detection ML Project
"""

import subprocess
import sys
from pathlib import Path


def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False


def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['ultralytics', 'cv2', 'numpy', 'PIL']
    missing = []
    
    for package in required_packages:
        try:
            if package == 'cv2':
                __import__('cv2')
            elif package == 'PIL':
                __import__('PIL')
            else:
                __import__(package)
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            missing.append(package)
    
    return len(missing) == 0


def create_directories():
    """Create necessary directories"""
    directories = ['output', 'dataset/images/train', 'dataset/images/val', 'dataset/labels/train', 'dataset/labels/val']
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")


def main():
    print("=" * 50)
    print("Object Detection ML Project - Setup")
    print("=" * 50)
    print()
    
    # Check dependencies
    print("Checking dependencies...")
    if not check_dependencies():
        print("\nSome packages are missing. Installing...")
        if not install_requirements():
            print("\nSetup failed. Please install packages manually:")
            print("  pip install -r requirements.txt")
            return
    else:
        print("\nAll dependencies are installed!")
    
    print("\nCreating directories...")
    create_directories()
    
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("=" * 50)
    print("\nYou can now use the detection system:")
    print("  python detect.py --source webcam")
    print("  python detect.py --source path/to/image.jpg")
    print("\nFor more information, see README.md")


if __name__ == "__main__":
    main()

