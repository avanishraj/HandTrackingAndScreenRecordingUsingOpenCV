import cv2
import mediapipe as mp
# import time

cam = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cam.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # as mediapipe hands only detect RGB colour wo we have to change from bgr to rgb
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLandMarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLandMarks, mpHands.HAND_CONNECTIONS)
    cv2.imshow("Image2", img)
    key = cv2.waitKey(1)
    if key == ord("q"): 
        break

cam.release()
cv2.destroyAllWindows()