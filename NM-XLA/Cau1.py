import cv2
import numpy as np
import random

img = cv2.imread('a.jpg')
mean_filtered = cv2.blur(img, (5, 5))
cv2.imwrite('a_mean.jpg', mean_filtered)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
sobel = np.uint8(np.clip(sobel, 0, 255))
cv2.imwrite('a_edge.jpg', sobel)
channels = [0, 1, 2]
random.shuffle(channels)
random_color_img = img[:, :, channels]
cv2.imwrite('a_random_color.jpg', random_color_img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.imwrite('a_hue.jpg', h)
cv2.imwrite('a_saturation.jpg', s)
cv2.imwrite('a_value.jpg', v)