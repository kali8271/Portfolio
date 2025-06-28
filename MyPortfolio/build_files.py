#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

def main():
    print("Building static files for Vercel...")
    
    # Create static directory if it doesn't exist
    static_dir = "static"
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # Copy static files from resumeApp to root static directory
    source_dir = "resumeApp/static"
    if os.path.exists(source_dir):
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(static_dir, item)
            
            if os.path.isdir(source_path):
                if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)
        
        print(f"✓ Copied static files from {source_dir} to {static_dir}")
    else:
        print(f"⚠ Source directory {source_dir} not found")
    
    # Collect static files using Django
    try:
        subprocess.run([sys.executable, "manage.py", "collectstatic", "--noinput"], check=True)
        print("✓ Django collectstatic completed")
    except subprocess.CalledProcessError as e:
        print(f"⚠ Django collectstatic failed: {e}")
    
    print("Build completed!")

if __name__ == "__main__":
    main() 