import argparse
import cv2 

from ultralytics import YOLO 

model = YOLO

model.predict(source = 'images\input.png', show=True, save=True, show_labels=True, show_conf=False, conf=0.5, save_txt=False, save_crop=False, line_width=2)


