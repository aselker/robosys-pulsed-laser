import cv2
import numpy as np
import sys

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

diff = cv2.absdiff(img2, img1)

cv2.imwrite(sys.argv[3],diff)
