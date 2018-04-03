import cv2
import numpy as np
import sys


def scaleAndSave(img, name):

  scaled = np.int16(img + np.min(img))
  scaled = (scaled * 255.0 / np.max(scaled))

  cv2.imwrite(name, img)



img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])


diff = np.int16(img2)
diff -= img1

scharr = cv2.Scharr(diff, cv2.CV_16S, 0, 1)
# canny = cv2.Canny(scharr, 40, 350, 3) # Parameters taken from the c++ program, TODO: tune them

scaleAndSave(scharr, "scharr.png")

clip = np.vectorize(lambda x: max(x,0)) 
clipped = clip(scharr)

scaled = np.uint8( clipped * 255.0 / np.max(clipped) )

cv2.imwrite("diff.png",scaled)


