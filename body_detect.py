import cv2
from cvzone.PoseModule import PoseDetector

import numpy as np

detector = PoseDetector()

cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    image = detector.findPose(image)
    llist, bboxes = detector.findPosition(image)
    if bboxes:
        center = bboxes['center']
    cv2.imshow("Body Detection", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break