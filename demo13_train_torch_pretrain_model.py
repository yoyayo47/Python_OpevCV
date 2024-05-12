import sys
from pprint import pprint
from dataset import ImageClassificationDataset
from torchvision import transforms
from torch.utils.data import DataLoader
import torch
import torchvision
from torchvision.models import ResNet18_Weights
from torch.nn import functional as F

# pprint(sys.path)
DATASETS = ['input/images']
CATEGORIES = ['positive', 'negative']
TRANSFORMS = transforms.Compose([
    transforms.ColorJitter(0.2, 0.2, 0.2, 0.2),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
datasets = {}
for name in DATASETS:
    datasets[name] = ImageClassificationDataset(name, CATEGORIES, TRANSFORMS)
dataset = datasets[DATASETS[0]]
print("*****************")
# dataset._refresh()
train_loader = DataLoader(dataset, batch_size=1, shuffle=True)
print(type(train_loader))
# enable torch
device = torch.device('cpu')
# model = torchvision.models.resnet18(pretrained=True)
model = torchvision.models.resnet18(weights=ResNet18_Weights.DEFAULT)
model.fc = torch.nn.Linear(512, len(dataset.categories))
model = model.to(device)
model.train()
print(model)

epochs = 20
optimizer = torch.optim.Adam(model.parameters())
while epochs > 0:
    i = 0
    sum_loss = 0.0
    error_count = 0.0
    for images, labels in iter(train_loader):
        images = images.to(device)
        labels = labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = F.cross_entropy(outputs, labels)
        loss.backward()
        optimizer.step()
        error_count += len(torch.nonzero(outputs.argmax(1) - labels, as_tuple=False).flatten())
        count = len(labels.flatten())
        i += count
        sum_loss += float(loss)
    print("[{}],loss={},accuracy={}".format(epochs, sum_loss / i, (1.0 - error_count / i)))
    epochs = epochs - 1

# 手動建model子目錄
torch.save(model.state_dict(), 'model/two_category')
torch.save(model, 'model/demo13')

# sanity check
val_dataset = ImageClassificationDataset('validate/images', CATEGORIES, TRANSFORMS)
val_loader = DataLoader(val_dataset, batch_size=1)

i = 0
error_count = 0

for image, label in iter(val_loader):
    images = image.to(device)
    labels = label.to(device)
    output = model(images)
    error_count += len(torch.nonzero(output.argmax(1) - labels).flatten())
    count = len(labels.flatten())
    i += count
print("error_count=", error_count)
