import requests
import torch
from prepair import prepair
# Model
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/best.pt')

img = "https://media.discordapp.net/attachments/922560384051851285/1031326787675885658/wickCaptcha.png"
img = Image.open(requests.get(img,stream=True).raw)
img = prepair(img)

result = model(img)
a = result.pandas().xyxy[0].sort_values('xmin')
while len(a)>6:
    lines = a.confidence
    linev = min(a.confidence)
    for line in lines.keys():
        if lines[line] == linev:
            a = a.drop(line)
result = ""
for _,key in a.name.items():
    result = result+key
print(result)
