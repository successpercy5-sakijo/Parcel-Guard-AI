import cv2
from cvzone.FaceDetectionModule import FaceDetector

import numpy as np

detector = FaceDetector()

cap1 = cv2.VideoCapture(0)
while True:
    success, image = cap1.read()
    image, bboxes = detector.findFaces(image)
    if bboxes:
        center = bboxes[0]['center']
    cv2.imshow("Face Detection", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break