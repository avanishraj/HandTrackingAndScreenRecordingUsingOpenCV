import cv2
import pyautogui as p
import numpy as np

name = input("Please enter any file name or path: ")
size = p.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0
output = cv2.VideoWriter(name, fourcc, fps, size)

cv2.namedWindow("Live_Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording", (600, 400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    cv2.imshow("Live_Recording", f)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
output.release()
cv2.destroyAllWindows()