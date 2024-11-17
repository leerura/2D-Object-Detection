# 현재 경로 설정
data_dir = '/root/data'
images_dir = os.path.join(data_dir, 'images', 'train')
labels_dir = os.path.join(data_dir, 'labels', 'train')

# 데이터를 나눌 경로 설정
train_images_dir = os.path.join(data_dir, 'images', 'train')
val_images_dir = os.path.join(data_dir, 'images', 'val')
train_labels_dir = os.path.join(data_dir, 'labels', 'train')
val_labels_dir = os.path.join(data_dir, 'labels', 'val')

# 폴더가 없다면 생성
for folder in [val_images_dir, val_labels_dir]:
    os.makedirs(folder, exist_ok=True)

# 모든 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

# 셔플 후 데이터 나누기
random.seed(42)  # 재현성을 위한 랜덤 시드 고정
random.shuffle(image_files)

train_split = int(0.7 * len(image_files))

train_files = image_files[:train_split]
val_files = image_files[train_split:]

# 파일 이동 함수 정의
def move_files(file_list, source_image_dir, source_label_dir, target_image_dir, target_label_dir):
    for file_name in file_list:
        # 이미지 파일 이동
        shutil.move(os.path.join(source_image_dir, file_name), os.path.join(target_image_dir, file_name))
        
        # 라벨 파일 이름 추출 및 이동
        label_file = file_name.replace('.jpg', '.txt')
        if os.path.exists(os.path.join(source_label_dir, label_file)):
            shutil.move(os.path.join(source_label_dir, label_file), os.path.join(target_label_dir, label_file))

# 파일 이동
move_files(val_files, images_dir, labels_dir, val_images_dir, val_labels_dir)

print("데이터 분할이 완료되었습니다.")

