# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10])
y=x**2
plt.style.show("seaborn")
plt.title("growth chat")
plt.plot(x,y)
plt.show()

plt.scatter(x,y,color="red")
plt.show()

np.sin(10)

arr=np.linspace(1,10,2000)
y=np.sin(arr)
plt.plot(arr,y)
plt.plot(arr,np.cos(arr),color="red")
plt.show()

import cv2



img=plt.imread("wq.jpg")

plt.imshow(img)

plt.axis("off")
plt.show()

print(img)

plt.imshow(img)
plt.axis("off")
plt.show()

import cv2
model = cv2.CascadeClassifier('pattern.xml')

input = img
output = model.detectMultiScale(input,minSize=(50,50))

print(output)
for face in output:
    x,y,w,h = face
    green = (255,255,0)
    cv2.rectangle(img,(x,y),(x+w,y+h),green,5)

plt.imshow(img)
plt.axis("off")
plt.show()

