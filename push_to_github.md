# Push to GitHub - Instructions

## Option 1: Install Git and Push (Recommended)

### Step 1: Install Git
1. Download Git for Windows from: https://git-scm.com/download/win
2. Run the installer with default settings
3. Restart your terminal/PowerShell after installation

### Step 2: Configure Git (if first time)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Initialize and Push
Run these commands in your project directory:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Object Detection ML Project"

# Add remote repository
git remote add origin https://github.com/anizxx/Object-Detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Option 2: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. File → Add Local Repository → Select this folder
4. Commit all changes
5. Publish repository to GitHub

## Option 3: Use GitHub Web Interface

1. Go to https://github.com/anizxx/Object-Detection
2. Click "uploading an existing file"
3. Drag and drop all project files
4. Commit changes

## Files to Include

Make sure these files are included:
- ✅ detect.py
- ✅ train.py
- ✅ utils.py
- ✅ requirements.txt
- ✅ README.md
- ✅ dataset_example.yaml
- ✅ setup.py
- ✅ example_usage.py
- ✅ .gitignore

## Files to Exclude (already in .gitignore)

- ❌ output/ (detection results)
- ❌ yolov8n.pt (model file - too large, will download automatically)
- ❌ test_image.jpg (test files)
- ❌ __pycache__/
- ❌ venv/





