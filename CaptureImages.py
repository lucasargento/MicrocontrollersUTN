import cv2
import os
import time
import uuid

'''Queremos capturar las imagenes para entrenar
al modelo que va a reconocer los dedos.'''


IMAGES_PATH = "/Users/lucasargento/Development/Microcontroladores - UTN/TP Final/Tensorflow/workspace/images/collectedimages"

#labels = ["pulgar","indice","mayor","anular","menique"]
# me habia olvidado de estas dos labels, asique corro de vuelta:
labels = ["cerrado", "abierto"]
numb_imgs = 15

for label in labels:
    os.mkdir(IMAGES_PATH + "/" + label)
    cap = cv2.VideoCapture(0)
    print("Capturando imagenes para " + label)
    time.sleep(5)
    for imagenum in range(numb_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, str(uuid.uuid4()) + ".jpg")
        cv2.imwrite(imagename, frame)
        cv2.imshow("frame", frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

