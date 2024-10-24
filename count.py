#데이터에서 각 차 종류 별로 몇 개의 데이터가 있는지 확인 
import json
from collections import defaultdict
import matplotlib.pyplot as plt

json_file_path = "../data/train.json"

try:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        
    vehicle_count = defaultdict(int)

    for image_data in data:
        for annotation in image_data["annotations"]:
            label = annotation["lbl_nm"]
            if label in ["bus", "car", "sign", "truck", "human", "special_vehicles", "taxi", "motocycle"]:  # 차 종류가 있을 경우에만 카운팅
                vehicle_count[label] += 1

        
    for vehicle, count in vehicle_count.items():
        print(f"{vehicle}: {count}")
    
    labels = list(vehicle_count.keys())
    counts = list(vehicle_count.values())

    plt.figure(figsize=(8,6))
    plt.bar(labels, counts)
    plt.title('Vehicle Count by Type')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Count')

    plt.savefig('vehicle_count.png')
    
    

except FileNotFoundError:
    print(f"File {json_file_path} not found.")
except json.JSONDecodeError as e:

    print(f"JSON Decode Error: {e}")