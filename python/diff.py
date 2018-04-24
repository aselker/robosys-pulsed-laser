import cv2
import numpy as np
import sys
import os

def scale(img):

  shifted = np.int16(img) - np.min(img) 
  scaled = np.uint8(shifted * 255.0 / np.max(shifted))
  return scaled

def getLines(img, name, gaussSize, cannyConfig):

  #Take only the red channel
  img[:,:,0] = img[:,:,2]
  img[:,:,1] = img[:,:,2]

  """
  scharr = cv2.Scharr(img, cv2.CV_16S, 0, 1)
  cv2.imwrite(name + "-scharr.png", scale(scharr))
  scharr_blurred = cv2.GaussianBlur(scharr,(gaussSize,gaussSize),0)
  """

  blurred = cv2.GaussianBlur(img,(gaussSize,gaussSize),0)
  scharr = cv2.Scharr(blurred, cv2.CV_16S, 0, 1)
  cv2.imwrite(name + "-scharr.png", scale(scharr))

  canny = cv2.Canny(scale(scharr), cannyConfig[0], cannyConfig[1])

  canny_green = np.zeros(img.shape)
  canny_green[:,:,1] = canny
  cv2.imwrite(name + "-lines.png", scale(img + canny_green))


off = cv2.imread(sys.argv[1])
print("Baseline image: " + sys.argv[1])

for i in sys.argv[2:]:

  on = cv2.imread(i)

  print(i)
  name = os.path.splitext(os.path.basename(i))[0] # "here/there/pic.png" -> "pic"

  if not os.path.exists(name):
    os.mkdir(name)
 
  diff = np.int16(on)
  diff -= off

  getLines(diff, os.path.join(name,"diff"), 51, (10,50))
  getLines(on, os.path.join(name,"on"), 51, (10,50))
