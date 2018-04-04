import cv2
import numpy as np
import sys

def scale(img):

  shifted = np.int16(img) - np.min(img) 
  scaled = np.uint8(shifted * 255.0 / np.max(shifted))
  return scaled


img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])


diff = np.int16(img2)
diff -= img1

cv2.imwrite("diff.png", scale(diff))

scharr = cv2.Scharr(diff, cv2.CV_16S, 0, 1)

cv2.imwrite("scharr.png", scale(scharr))

canny = cv2.Canny(scale(scharr), 100, 200)

cv2.imwrite("canny.png", scale(canny))
