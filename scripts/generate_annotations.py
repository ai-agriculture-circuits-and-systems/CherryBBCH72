import os
import json
import glob
from PIL import Image
import random
import time

def generate_unique_id():
    """Generate unique ten-digit ID with timestamp suffix"""
    # Generate first 7 digits randomly
    prefix = random.randint(1000000, 9999999)
    # Get last 3 digits of current timestamp
    timestamp_suffix = int(time.time() * 1000) % 1000
    # Combine into ten-digit ID
    unique_id = prefix * 1000 + timestamp_suffix
    return unique_id

def convert_yolo_to_coco_bbox(yolo_bbox, img_width, img_height):
    """Convert YOLO format bbox to COCO format"""
    x_center, y_center, w, h = yolo_bbox
    
    # YOLO format is relative coordinates, need to convert to absolute coordinates
    x = (x_center - w/2) * img_width
    y = (y_center - h/2) * img_height
    width = w * img_width
    height = h * img_height
    
    return [x, y, width, height]

def generate_annotation_file(image_path, label_path, output_path):
    """Generate annotation file for single image"""
    
    # Get image information
    img = Image.open(image_path)
    img_width, img_height = img.size
    img_filename = os.path.basename(image_path)
    
    # Generate unique image ID
    image_id = generate_unique_id()
    
    # Initialize COCO format
    coco_format = {
        "info": {
            "description": "CherryBBCH72 Dataset - Cherry fruit images captured during fruit development stage (BBCH 72-73)",
            "version": "1.0",
            "year": 2025,
            "contributor": "search engine",
            "source": "augmented",
            "license": {
                "name": "Creative Commons Attribution 4.0 International",
                "url": "https://creativecommons.org/licenses/by/4.0/"
            }
        },
        "images": [
            {
                "id": image_id,
                "width": img_width,
                "height": img_height,
                "file_name": img_filename,
                "size": os.path.getsize(image_path),
                "format": "JPEG",
                "url": "",
                "hash": "",
                "status": "success"
            }
        ],
        "annotations": [],
        "categories": [
            {
                "id": generate_unique_id(),
                "name": "CherryBBCH72",
                "supercategory": "cherry"
            }
        ]
    }
    
    # Read label file
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        annotation_id = 1
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 5:
                class_id, x_center, y_center, w, h = map(float, parts)
                
                # Convert to COCO format bbox
                bbox = convert_yolo_to_coco_bbox([x_center, y_center, w, h], img_width, img_height)
                
                # Calculate area
                area = bbox[2] * bbox[3]
                
                # Add annotation
                coco_format["annotations"].append({
                    "id": generate_unique_id(),
                    "image_id": image_id,
                    "category_id": coco_format["categories"][0]["id"],
                    "segmentation": [],
                    "area": area,
                    "bbox": bbox
                })
    
    # Save to JSON file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(coco_format, f, indent=2, ensure_ascii=False)
    
    print(f"Generated annotation file: {output_path}")

def main():
    """Main function: generate independent annotation files for all images"""
    
    images_dir = "data/images"
    labels_dir = "data/labels"
    
    # Get all image files
    image_files = glob.glob(os.path.join(images_dir, "*.jpg"))
    
    for image_path in image_files:
        # Get corresponding label file path
        img_filename = os.path.basename(image_path)
        label_filename = os.path.splitext(img_filename)[0] + ".txt"
        label_path = os.path.join(labels_dir, label_filename)
        
        # Generate output file path - save in same directory as images
        output_filename = os.path.splitext(img_filename)[0] + "_annotations.json"
        output_path = os.path.join(images_dir, output_filename)
        
        # Generate annotation file
        generate_annotation_file(image_path, label_path, output_path)

if __name__ == "__main__":
    main() 