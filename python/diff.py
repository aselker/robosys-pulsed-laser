import cv2
import numpy as np
import sys

def scale(img):

  shifted = np.int16(img) - np.min(img) 
  scaled = np.uint8(shifted * 255.0 / np.max(shifted))
  return scaled

def getLines(img, name, cannyConfig):

  #Take only the red channel
  img[:,:,0] = img[:,:,2]
  img[:,:,1] = img[:,:,2]

  scharr = cv2.Scharr(img, cv2.CV_16S, 0, 1)

  cv2.imwrite(name + "-scharr.png", scale(scharr))

  canny = cv2.Canny(scale(scharr), cannyConfig[0], cannyConfig[1])

  # cv2.imwrite(name + "-canny.png", scale(canny))

  canny_green = np.zeros(img.shape)
  canny_green[:,:,1] = canny
  cv2.imwrite(name + "-lines.png", scale(img + canny_green))

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])


diff = np.int16(img2)
diff -= img1

getLines(diff,"diff", (100,400))
getLines(img2,"on",(100,400))
