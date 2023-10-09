import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv


# open the contour graph (has already been cleaned up slightly by hand)
img = cv2.imread('capture.PNG', 1)

# filter out none-contour things on the graph
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,255,255])#[30,150,50])
upper_red = np.array([255,255,255])#[255,255,180])
mask = cv2.inRange(hsv, lower_red, upper_red)


ret = ''
for i, row in enumerate(mask):
    for j, col in enumerate(row):
        if col == 255:
            ret += str((j/(len(row)-1))*7000) + ', ' + str((((len(mask)-1)-i)/(len(mask)-1))*175) + '\n'

ret = ret[::-1]
print(ret[0])

with open('torque_map.csv', 'w') as f:
    f.write(ret)
