import os
import json

json_file_path = '../data/train.json'
output_dir = '../data/train_txt'
os.makedirs(output_dir, exist_ok=True)

with open(json_file_path, 'r') as file:
    data = json.load(file)

for image_data in data:
    img_id = image_data['images']['img_id']
    img_width = image_data['images']['img_width']
    img_height = image_data['images']['img_height']

    img_id = str(img_id).zfill(10)

    yolo_label_path = os.path.join(output_dir, f"{img_id}.txt")

    with open(yolo_label_path, 'w') as yolo_file:
        for annotation in image_data['annotations']:
            class_id = annotation['lbl_id'] - 1
            bbox = json.loads(annotation['annotations_info'])

            x_min, y_min, width, height = bbox

            x_center = x_min + width/2
            y_center = y_min + height/2

            x_center = x_center/img_width
            y_center = y_center/img_
            width = width/img_width
            height = height/img_height

            yolo_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")


 

        
    