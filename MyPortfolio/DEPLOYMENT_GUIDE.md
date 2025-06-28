# Vercel Deployment Guide

## Static Files Setup

Your static files are now properly configured for Vercel deployment. Here's what we've set up:

### 1. Build Process
- `build_files.py` - Copies static files to the correct location
- `vercel.json` - Configures Vercel to handle static files properly

### 2. Static Files Location
Your static files are located in:
- `resumeApp/static/images/` - Contains k2.jpeg and k3.jpeg
- `resumeApp/static/css/` - Contains style.css

### 3. Deployment Steps

1. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Configure static files for Vercel"
   git push
   ```

2. **Deploy to Vercel:**
   - Connect your GitHub repository to Vercel
   - Vercel will automatically run the build script
   - Static files will be available at `/static/`

### 4. Static File URLs
After deployment, your images will be available at:
- `https://your-domain.vercel.app/static/images/k3.jpeg`
- `https://your-domain.vercel.app/static/images/k2.jpeg`

### 5. Alternative: External Image Hosting

If you prefer to use external image hosting:

1. **Upload to Imgur:**
   - Go to https://imgur.com
   - Upload your images
   - Copy the direct links
   - Update templates to use external URLs

2. **Upload to Cloudinary:**
   - Sign up at https://cloudinary.com
   - Upload images
   - Use their CDN URLs

3. **Upload to AWS S3:**
   - Create an S3 bucket
   - Upload images
   - Make them public
   - Use S3 URLs

### 6. Current Configuration

The current setup uses:
- Local static files for development
- Vercel's static file serving for production
- Build script to copy files to the correct location

### 7. Testing

To test locally:
```bash
python build_files.py
python manage.py runserver
```

Visit: `http://localhost:8000/static/images/k3.jpeg`

### 8. Troubleshooting

If static files don't load on Vercel:
1. Check the build logs in Vercel dashboard
2. Ensure `build_files.py` runs successfully
3. Verify the static files are in the correct location
4. Check the `vercel.json` configuration

### 9. Next Steps

1. Deploy to Vercel
2. Test static file loading
3. If issues persist, consider external image hosting
4. Update any remaining static file references in templates 