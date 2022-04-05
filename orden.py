import os
from pathlib import Path

arr = os.listdir('/Users/lucasargento/Development/Microcontroladores-UTN/TPFinal/Tensorflow/workspace/images/collectedimages/mover')
print(arr)

source = '/Users/lucasargento/Development/Microcontroladores-UTN/TPFinal/Tensorflow/workspace/images/collectedimages/All/'
destination = '/Users/lucasargento/Development/Microcontroladores-UTN/TPFinal/Tensorflow/workspace/images/collectedimages/abierto/'

for xml in arr:
    name = xml.split('.')[0]
    if name != "":
        Path(source+name+".jpg").rename(destination+name+".jpg")