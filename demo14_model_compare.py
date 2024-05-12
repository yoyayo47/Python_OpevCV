import torch
import torchvision
from torchvision import transforms
import time
from dataset import ImageClassificationDataset
from torch.utils.data import DataLoader

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
print(model1)
print("load model1")
start = time.time()
model1.load_state_dict(torch.load('model/two_category'))
finish1 = time.time()
print("model1 load time={}".format(finish1 - start))
print("load model2")
model2 = torch.load('model/demo13')
finish2 = time.time()
print("finish load")
print("model2 load time={}".format(finish2 - finish1))


def compare_model(model_1, model_2):
    models_differ = 0
    for key_item_1, key_item_2 in zip(model_1.state_dict().items(), model_2.state_dict().items()):
        if torch.equal(key_item_1[1], key_item_2[1]):
            # print(key_item_1[0], " is equal")
            pass
        else:
            models_differ += 1
            if key_item_1[0] == key_item_2[0]:
                print(key_item_1[0], "向量不相等")
            else:
                raise Exception
    if models_differ == 0:
        print("兩個模型是相等的")


compare_model(model1, model2)
print("load success")
file1_path = 'model/model1.txt'
file2_path = 'model/model2.txt'
with open(file1_path, 'w') as file1:
    file1.write(str(model1))
with open(file2_path, 'w') as file2:
    file2.write(str(model2))

# 驗証載入的模型效能
CATEGORIES = ['positive', 'negative']
val_dataset = ImageClassificationDataset('validate/images', CATEGORIES, TRANSFORMS)
val_loader = DataLoader(val_dataset, batch_size=1)

models = [model1, model2]

for model, message in zip(models, ["從state_dict載入", "完整載入的"]):
    print(message)
    i = 0
    error_count = 0
    for image, label in iter(val_loader):
        images = image.to(device)
        labels = label.to(device)
        output = model(images)
        error_count += len(torch.nonzero(output.argmax(1) - labels).flatten())
        count = len(labels.flatten())
        i += count
    print(message, "error_count=", error_count)
