# CherryBBCH72 Dataset

A dataset of cherry fruit images captured during the fruit development stage (BBCH 72-73) in the LatHort orchard in Dobele, Latvia.

## Dataset Description

The CherryBBCH72 dataset is designed for cherry fruit detection and yield estimation tasks. It contains high-resolution images of cherry trees captured at specific development stages, making it suitable for computer vision, object detection, and deep learning research in agricultural applications.

- **Number of images**: Original images cropped into 640x640 images
- **Image format**: YOLO format (with converted COCO-style JSON annotations)
- **Overlap**: 30% between cropped images
- **BBCH stages**: 72-73 (fruit development stage)

## Dataset Structure

The dataset includes:
- Original high-resolution images
- Cropped and annotated images (640x640, JPEG/PNG)
- YOLO format annotation files (`.txt` for each image)
- COCO-style JSON annotation files (`_annotations.json` for each image)
- Multiple views per tree

**Directory layout example:**
```
data/
  images/
    IMGP8762_9.jpg
    IMGP8762_9.txt
    IMGP8762_9_annotations.json
    ...
```

- Each image file (e.g., `IMGP8762_9.jpg`) has a corresponding YOLO annotation file (`IMGP8762_9.txt`) and a COCO-style JSON annotation file (`IMGP8762_9_annotations.json`).

## JSON Annotation File Structure

Each JSON annotation file follows a simplified COCO format, containing metadata and annotation information for a single image. Example structure:

```json
{
  "images": [
    {
      "id": 1234567890,
      "file_name": "IMGP8762_9.jpg",
      "width": 640,
      "height": 640
    }
  ],
  "annotations": [
    {
      "id": 1234567891,
      "image_id": 1234567890,
      "category_id": 1,
      "bbox": [x, y, width, height],
      "area": area,
      "iscrowd": 0
    }
    // ... more annotations for this image
  ],
  "categories": [
    {
      "id": 1,
      "name": "cherry"
    }
  ]
}
```

- `images`: List with metadata for the image (unique `id`, filename, width, height).
- `annotations`: List of bounding box annotations for detected cherries in the image.
  - `bbox`: [x, y, width, height] in COCO format (absolute pixel values, top-left origin).
  - `area`: Area of the bounding box (width × height).
  - `category_id`: Always 1 (for "cherry").
- `categories`: List of categories (only "cherry" in this dataset).

## Data Collection

- **Location**: LatHort orchard in Dobele, Latvia
- **Timing**: During fruit development (BBCH stage 72-73)
- **Annotation tool**: makesense.ai
- **Validation**: Manual validation of cropped images

## Applications

This dataset can be used for:
- Cherry fruit detection
- Yield estimation
- Object detection
- Computer vision research
- Deep learning model training
- Agricultural AI applications

## Categories

- Computer Science
- Artificial Intelligence
- Computer Vision
- Object Detection
- Machine Learning
- Agriculture
- Deep Learning
- Yield Estimation
- Precision Agriculture

## Citation

```
Kodors, S., Zarembo, I., Lācis, G., Litavniece, L., Apeināns, I., Sondors, M., & Pacejs, A. (2024). Autonomous Yield Estimation System for Small Commercial Orchards Using UAV and AI. Drones, 8(12), 734. https://doi.org/10.3390/drones8120734
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Source

The dataset is available at:
- [Kaggle Dataset](https://www.kaggle.com/datasets/projectlzp201910094/applebbch81)
- [Papers with Code](https://paperswithcode.com/dataset/applebbch81)