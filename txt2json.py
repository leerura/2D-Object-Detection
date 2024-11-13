import os
import json

results_dir = "/root/codes/yolov5/runs/detect/exp2/labels"
output_json_path = "/root/codes/yolov5/runs/detect/detect_results_exp2.json"

result = []

for txt_file in os.listdir(results_dir):
    if txt_file.endswith('.txt'):
        img_id = os.path.splitext(txt_file)[0]

        with open(os.path.join(results_dir, txt_file), 'r') as file:
            annotations = []
            for index, line in enumerate(file):
                parts = line.strip().split()
                lbl_id = int(parts[0])+1
                x_center,y_center, width, height, confidence = map(float, parts[1:])

                img_width, img_height = 1920,1200
                x_min = (x_center - width / 2) * img_width
                y_min = (y_center - height / 2) * img_height
                width = width * img_width
                height = height * img_height

                annotation_info = [x_min, y_min, width, height]

                label_mapping = {
                    1: "bus",
                    2: "car",
                    3: "sign",
                    4: "truck",
                    5: "human",
                    6: "special_vehicles",
                    7: "taxi",
                    8: "motorcycle"
                }

                lbl_nm = label_mapping.get(lbl_id, "unknown")

                annotations.append({
                    "annotations_id": f"{img_id}_{index}",
                    "lbl_id": lbl_id,
                    "lbl_nm": lbl_nm,
                    "annotations_info": str(annotation_info),
                    "confidence": confidence

                })

        result.append({
            "images": {
                "img_id": img_id,
                "img_width": img_width,
                "img_height": img_height
            },
            "anootations": annotations
        })

with open(output_json_path, 'w') as json_file:
    json.dump(result, json_file, indent=4)



                