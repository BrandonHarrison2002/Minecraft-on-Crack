# import cv2
# import numpy as np
# from PIL import ImageGrab
# from ctypes import windll
# import win32api

# user32 = windll.user32
# user32.SetProcessDPIAware()

# # brown = [212, 42, 42]  # RGB
# diff = 30
# boundaries = [([12, 12, 282],
#              [72, 72, 252])]
# while (True):
#     x = win32api.GetSystemMetrics(0) - win32api.GetSystemMetrics(0)*0.605
#     y = win32api.GetSystemMetrics(1) - win32api.GetSystemMetrics(1)*0.11
#     img = ImageGrab.grab(bbox=(x,y,240 + x,5 +y))
#     img = np.array(img)
#     frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     for (lower, upper) in boundaries:
#         lower = np.array(lower, dtype=np.uint8)
#         upper = np.array(upper, dtype=np.uint8)
#         mask = cv2.inRange(frame, lower, upper)
#         output = cv2.bitwise_and(frame, frame, mask=mask)

#         ratio_brown = cv2.countNonZero(mask)/(frame.size/3)
#         print('red pixel percentage:', np.round(ratio_brown*100, 2))

#         cv2.imshow("Recorder", np.hstack([frame, output]))
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np
from PIL import ImageGrab
x = 760
y = 968

offx = 50
offy = 22
img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        
img = np.array(img)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break






# import numpy as np
# import cv2

# img = cv2.imread('Health.png')

# brown = [212, 42, 42]  # RGB
# diff = 30
# boundaries = [([brown[2]-diff, brown[1]-diff, brown[0]-diff],
#                [brown[2]+diff, brown[1]+diff, brown[0]+diff])]
# # in order BGR as opencv represents images as numpy arrays in reverse order

# for (lower, upper) in boundaries:
#     lower = np.array(lower, dtype=np.uint8)
#     upper = np.array(upper, dtype=np.uint8)
#     mask = cv2.inRange(img, lower, upper)
#     output = cv2.bitwise_and(img, img, mask=mask)

#     ratio_brown = cv2.countNonZero(mask)/(img.size/3)
#     print('red pixel percentage:', np.round(ratio_brown*100, 2))

#     cv2.imshow("images", np.hstack([img, output]))
#     cv2.waitKey(0)