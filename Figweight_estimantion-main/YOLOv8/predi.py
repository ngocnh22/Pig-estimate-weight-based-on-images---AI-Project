# python main-pj.py
import cv2 
import math
from yolo_predict import YOLOSegmentation
import numpy as np


path_v = r'videos/feeding-2.mp4'
video = cv2.VideoCapture(path_v)

yd = YOLOSegmentation(r'/home/oem/ngoc/yolo/data/runs/detect/train/weights/best.pt')

if not video.isOpened():
	print('Error opening video file')

import random

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output12.mp4", fourcc, 30, (int(video.get(3)), int(video.get(4))))


while True:
    ret, img = video.read()
    bbx, score, id = yd.detect(img)
    print(bbx, score, id)
    for bbx, score, id in zip(bbx, score, id):
                (x, y, w, h) = bbx
                img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    if ret == True:
        cv2.imshow('sss', img)
        out.write(img)
    cv2.waitKey(30)
print('ge')
