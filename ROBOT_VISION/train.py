import os

from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.yaml")

results = model.train(data="data_config.yaml", epochs=3)

