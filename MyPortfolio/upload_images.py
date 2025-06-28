import requests
import os
import json

def upload_to_imgur(image_path, client_id):
    """Upload image to Imgur and return the URL"""
    url = "https://api.imgur.com/3/image"
    
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        headers = {'Authorization': f'Client-ID {client_id}'}
        
        response = requests.post(url, files=files, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data['data']['link']
        else:
            print(f"Error uploading {image_path}: {response.text}")
            return None

def main():
    # You'll need to get a Client ID from https://api.imgur.com/oauth2/addclient
    # For now, we'll use a placeholder
    CLIENT_ID = "YOUR_IMGUR_CLIENT_ID"  # Replace with your actual Client ID
    
    static_images_dir = "resumeApp/static/images"
    
    if not os.path.exists(static_images_dir):
        print(f"Directory {static_images_dir} not found!")
        return
    
    image_files = [f for f in os.listdir(static_images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    print("Found images:", image_files)
    print("\nTo upload these images to Imgur:")
    print("1. Go to https://api.imgur.com/oauth2/addclient")
    print("2. Register an application (you can use 'Portfolio Images' as the name)")
    print("3. Get your Client ID")
    print("4. Replace 'YOUR_IMGUR_CLIENT_ID' in this script with your actual Client ID")
    print("5. Run this script again")
    
    if CLIENT_ID == "YOUR_IMGUR_CLIENT_ID":
        print("\nPlease update the CLIENT_ID variable with your actual Imgur Client ID")
        return
    
    uploaded_urls = {}
    
    for image_file in image_files:
        image_path = os.path.join(static_images_dir, image_file)
        print(f"Uploading {image_file}...")
        
        url = upload_to_imgur(image_path, CLIENT_ID)
        if url:
            uploaded_urls[image_file] = url
            print(f"✓ {image_file} uploaded: {url}")
        else:
            print(f"✗ Failed to upload {image_file}")
    
    # Save URLs to a JSON file
    with open('image_urls.json', 'w') as f:
        json.dump(uploaded_urls, f, indent=2)
    
    print(f"\nUploaded {len(uploaded_urls)} images. URLs saved to image_urls.json")

if __name__ == "__main__":
    main() 