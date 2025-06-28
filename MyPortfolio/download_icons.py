import requests
import os

def download_icon(url, filename, directory):
    """Download an icon from URL and save it locally"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)
        
        # Save the file
        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Downloaded {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
        return False

def main():
    # Icons to download
    icons = [
        {
            'url': 'https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/linkedin.svg',
            'filename': 'linkedin.svg',
            'directory': 'resumeApp/static/images'
        },
        {
            'url': 'https://cdn.jsdelivr.net/npm/simple-icons@v5/icons/github.svg',
            'filename': 'github.svg',
            'directory': 'resumeApp/static/images'
        }
    ]
    
    print("Downloading external icons to local static files...")
    
    for icon in icons:
        download_icon(icon['url'], icon['filename'], icon['directory'])
    
    print("\nIcons downloaded! Now update your templates to use local paths:")
    print("- /static/images/linkedin.svg")
    print("- /static/images/github.svg")

if __name__ == "__main__":
    main() 