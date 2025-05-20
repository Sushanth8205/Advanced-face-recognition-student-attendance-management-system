import os
import numpy as np
import cv2
from PIL import Image,ImageTk
from tkinter import messagebox

#def train_classifier():
data_dir=("data")
path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
faces=[]
ids=[]

for image in path:
    img=Image.open(image).convert('L')#gray scale image
    imagenp=np.array(img,'uint8')
    id=int(os.path.split(image)[1].split('.')[1])
    faces.append(imagenp)
    ids.append(id)
    cv2.imshow("traing",imagenp)
    cv2.waitKey(1)==13
ids=np.array(ids)
    #=======================tarin the classifier and save===============
clf=cv2.face.LBPHFaceRecognizer_create()
clf.train(faces,ids)
clf.write("classifier.xml")
cv2.destroyAllWindows()
messagebox.showinfo("Result","training datasets completed!!")

