#!/bin/bash
# Build script for Vercel deployment

echo "Building static files..."

# Create static directory if it doesn't exist
mkdir -p static

# Copy static files from resumeApp to root static directory
cp -r resumeApp/static/* static/

# Collect static files using Django
python manage.py collectstatic --noinput

echo "Build completed!" 