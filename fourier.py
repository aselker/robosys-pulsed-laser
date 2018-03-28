import cv2
import numpy as np
import sys

v = []

print("Loading video...")

cap = cv2.VideoCapture(sys.argv[1])

while cap.isOpened():
  ret, frame = cap.read()
  if ret:
    v += [frame[:,:,2]] #Extract the red channel
  else:
    break

cap.release()

print("Processing video...")


vf = np.array(v) #video frames

vs = vf.transpose((1,2,0)) # s for series, as in time-series
                           # at this point, s is a list (rows) of lists (columns) of numbers (red amplitudes @ times)

fs = np.array( [ [ np.real(np.fft.rfft(pixel,norm="ortho")) for pixel in column ] for column in vs ] ) # take the fft of each time-series

ff = fs.transpose((2,0,1)) * 255.0 / np.max(fs) # back from time-series to frames, and scaled so it's from 0 to 255.

# print(ff[0][int(len(ff[0])/2)])   #print the center row, because the first row is all black (fisheye lens)

ff_bgr = np.uint8( [ [ [ [pixel,pixel,pixel] for pixel in row ] for row in frame ] for frame in ff ] )

print("Writing video...")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(sys.argv[2], fourcc, 10.0, (640, 480))

for frame in ff_bgr:
  out.write(frame)

out.release()

