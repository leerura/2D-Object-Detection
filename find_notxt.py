import os

# 이미지 폴더와 라벨 폴더 경로 설정
val_images_path = "/root/data/images/val"
val_labels_path = "/root/data/labels/val"

# 이미지 파일 확장자
image_extensions = [".jpg"]

# 이미지 파일 목록 불러오기
image_files = [f for f in os.listdir(val_images_path) if os.path.splitext(f)[1].lower() in image_extensions]

# 라벨 파일 목록 불러오기
label_files = os.listdir(val_labels_path)

# 이미지 파일에 대응되는 라벨 파일이 있는지 확인
missing_labels = []

for image_file in image_files:
    image_name, _ = os.path.splitext(image_file)
    label_file = f"{image_name}.txt"
    if label_file not in label_files:
        missing_labels.append(image_file)

# 결과 출력
if missing_labels:
    print("다음 이미지 파일에 해당하는 라벨 파일이 없습니다:")
    for missing in missing_labels:
        print(missing)
else:
    print("모든 이미지 파일에 대응되는 라벨 파일이 있습니다.")