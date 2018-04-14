import cv2
import numpy as np
import sys
import os

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


off = cv2.imread(sys.argv[1])

for i in sys.argv[2:]:

  print(i)

  on = cv2.imread(i)

  if not os.path.exists(i):
    os.makedirs(i)
 
  diff = np.int16(on)
  diff -= off

  getLines(diff,os.path.join(i,"diff"), (60,450))
  getLines(on,os.path.join(i,"on"),(100,450))
