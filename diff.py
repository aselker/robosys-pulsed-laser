import cv2
import numpy as np
import sys


def scaleAndSave(img, name):

  shifted = np.int16(img) - np.min(img) 
  scaled = (shifted * 255.0 / np.max(shifted))

  cv2.imwrite(name, img)



img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])


diff = np.int16(img2)
diff -= img1

scaleAndSave(diff, "diff.png")

scharr = cv2.Scharr(diff, cv2.CV_16S, 0, 1)

scaleAndSave(scharr, "scharr.png")

diff_u8 = np.uint8(diff)

canny = cv2.Canny(diff_u8, 100, 200) # Parameters taken from the c++ program, TODO: tune them

scaleAndSave(canny, "canny.png")
