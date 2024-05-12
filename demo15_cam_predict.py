import cv2
import torch
import torchvision
from torchvision import transforms
import PIL

TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

device = torch.device('cpu')
model1 = torchvision.models.resnet18()
model1 = model1.to(device)
model1.fc = torch.nn.Linear(512, 2)
model1.load_state_dict(torch.load('model/two_category'))


def verify(f):
    images = f.to(device)
    images = torch.reshape(images, [1, 3, 224, 224])
    output = model1(images)
    if output.argmax(1) == 1:
        print("positive")
    else:
        print("negative")
    print("output vector=", output)


cap = cv2.VideoCapture(1)  # 學員填0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    cv2.imshow('detect', gray)
    k = cv2.waitKey(50)
    if k == ord('q'):
        break
    elif k == ord('v'):
        frame = PIL.Image.fromarray(frame)
        print(type(frame))
        frame = TRANSFORMS(frame)
        print(type(frame))
        verify(frame)

cap.release()
cv2.destroyAllWindows()
