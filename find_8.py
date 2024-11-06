import os

# 라벨 파일들이 있는 디렉토리 경로를 설정합니다.
labels_dir = '/root/data/labels/train'  # 실제 라벨 디렉토리 경로로 수정하세요

# 클래스 ID 8이 있는 파일을 저장할 리스트
files_with_class_8 = []

# 모든 라벨 파일을 확인하여 클래스 ID가 8인 항목이 있는지 검사
for label_file in os.listdir(labels_dir):
    if label_file.endswith('.txt'):
        file_path = os.path.join(labels_dir, label_file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                class_id = int(line.split()[0])  # 클래스 ID 추출
                if class_id == 8:  # 클래스 ID가 8이면
                    files_with_class_8.append(file_path)
                    break  # 파일 내에 하나라도 찾으면 더 이상 검사하지 않고 다음 파일로

# 결과 출력
if files_with_class_8:
    print("Files with class ID 8:")
    for file in files_with_class_8:
        print(file)
else:
    print("No files with class ID 8 found.")