import os
from tkinter import Frame
import cv2


path = "assets/"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

##sunset
for i in range (0,count - 1):
    frame = cv2.imread(images[i])
    out.write(frame)
##s unrise
#for i in range (count-1,0,-1):
#    frame1 = cv2.imread(images[i])
#    out.write(frame1)
#out.release()
#print("dome")