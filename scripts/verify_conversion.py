import os
import json
from PIL import Image

def convert_yolo_to_coco_bbox(yolo_bbox, img_width, img_height):
    """Convert YOLO format bbox to COCO format"""
    x_center, y_center, w, h = yolo_bbox
    
    # YOLO format is relative coordinates, need to convert to absolute coordinates
    x = (x_center - w/2) * img_width
    y = (y_center - h/2) * img_height
    width = w * img_width
    height = h * img_height
    
    return [x, y, width, height]

def verify_conversion():
    """Verify coordinate conversion is correct"""
    
    # Image dimensions
    img_width, img_height = 640, 640
    
    # First YOLO annotation
    yolo_bbox = [0.415268, 0.917969, 0.045308, 0.032812]
    
    # Convert to COCO format
    coco_bbox = convert_yolo_to_coco_bbox(yolo_bbox, img_width, img_height)
    
    print("YOLO format:", yolo_bbox)
    print("COCO format:", coco_bbox)
    
    # Verify calculation
    x_center, y_center, w, h = yolo_bbox
    expected_x = (x_center - w/2) * img_width
    expected_y = (y_center - h/2) * img_height
    expected_width = w * img_width
    expected_height = h * img_height
    
    print(f"\nManual verification:")
    print(f"x = ({x_center} - {w/2}) * {img_width} = {expected_x}")
    print(f"y = ({y_center} - {h/2}) * {img_height} = {expected_y}")
    print(f"width = {w} * {img_width} = {expected_width}")
    print(f"height = {h} * {img_height} = {expected_height}")
    
    # Check first annotation in generated JSON file
    json_file = "data/images/IMGP8762_9_annotations.json"
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        if data["annotations"]:
            first_annotation = data["annotations"][0]
            print(f"\nFirst annotation in JSON file:")
            print(f"bbox: {first_annotation['bbox']}")
            print(f"area: {first_annotation['area']}")
            
            # Verify area calculation
            expected_area = expected_width * expected_height
            print(f"Expected area: {expected_area}")
            print(f"Actual area: {first_annotation['area']}")
            print(f"Area matches: {abs(expected_area - first_annotation['area']) < 0.01}")

if __name__ == "__main__":
    verify_conversion() 