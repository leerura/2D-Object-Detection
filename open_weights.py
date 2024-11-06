import sys
sys.path.append('/root/codes/yolov5')

from models.common import DetectMultiBackend
import torch

weights_path = '/root/codes/yolov5/runs/train/my_yolo_model11/weights/best.pt'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = DetectMultiBackend(weights_path, device = device)

print(model.model)