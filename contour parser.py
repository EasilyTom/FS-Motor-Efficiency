import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

# HOW TO USE THIS
# This is python, not matlab.
# First, try and clean up the graph by hand.
# Remove text, and stop lines overlapping if possible
# Save as capture.PNG
# Run this, check if results are as intended
# the lines that start with img[np.all... replace a given colour with white
# change the 3 values in the first set of brackets to remove any lines on the
# graph that aren't the contours. You can copy + paste to add more
# if you need to remove more colours. You'll have to figure out
# the RGB values yourself.
# If it still isn't detecting properly, try changing the first value
# in the line ret, thresh...
# You'll need to change the del x[... lines to delete any contours you
# don't want. Good Luck! (You'll need it)



# open the contour graph (has already been cleaned up slightly by hand)
img = cv2.imread('capture.PNG', 1)

# filter out none-contour things on the graph
img[np.all(img == (0, 0, 0), axis=-1)] = (255,255,255)
img[np.all(img == (134, 134, 134), axis=-1)] = (255,255,255)

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,200,255,0)

# find contours, delete the ones we don't want
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
x = [i for i in contours if len(i)>100]
del x[1]
del x[3]
del x[4:6]
del x[5:]
contours = x

# add in the efficiency values
height, width, _ = img.shape
efficiencies = [86, 90, 94, 95, 96]
result = []
for i, y in enumerate(contours):
    for j, x in enumerate(y):
        result.append([int(6000*x[0][0]/width), int(160*(height-x[0][1])/height), efficiencies[i]])

# save        
with open('points.csv', 'w') as f:
    csv.writer(f).writerows(result)


cv2.imshow('i', img)
