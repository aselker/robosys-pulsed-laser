import cv2
import numpy as np
import sys
import os

def scale(img):

  shifted = np.int16(img) - np.min(img) 
  scaled = np.uint8(shifted * 255.0 / np.max(shifted))
  return scaled

def getLines(img, name, gaussSize, cannyConfig):

  if cannyConfig == None: # If there's no config, we figure it out automatically.
    sigma = 3

    median = np.median(img)
    variance = np.var(img)
    print("Variance: " + str(median))
    lower = -sigma * variance
    upper = sigma * variance
    cannyConfig = (lower,upper)
    print("Auto config: " + str(cannyConfig))
    # Credit for this function: https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/

  #Take only the red channel
  img[:,:,0] = img[:,:,2]
  img[:,:,1] = img[:,:,2]


  if (gaussSize%2 == 0):
    raise ValueError("Gauss kernel size must be odd!")
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

  #getLines(diff, os.path.join(name,"diff"), 19, (160,230))
  getLines(diff, os.path.join(name,"diff"), 19, None)
#  getLines(on, os.path.join(name,"on"), 15, (120,170))
