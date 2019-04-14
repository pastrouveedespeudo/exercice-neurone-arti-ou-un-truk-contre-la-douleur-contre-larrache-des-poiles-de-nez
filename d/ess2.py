import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

# read in your image


##
##
##raw_image = cv2.imread('rond2.png')
##
##
##bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
##
##
##edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
##
##
##_, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##
##contour_list = []
##for contour in contours:
##    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
##    area = cv2.contourArea(contour)
##    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
##        contour_list.append(contour)
##
##cv2.drawContours(raw_image, contour_list,  -1, (0,0,0), 100)
##
##cv2.imwrite("yo.png", raw_image)
##













##listeee = []
##imageee = cv2.imread('yo.png')
##for x in range(imageee.shape[0]):
##    for y in range(imageee.shape[1]):
##  
##        if imageee[x,y][0] <= 10 and\
##           imageee[x,y][1] <= 10 and\
##           imageee[x,y][2] <= 10:
##            listeee.append((x,y))
##
##
##
##
##
##
##image2 = cv2.imread('ya.png')
##
##
##for i in listeee:
##    image2[i[0], i[1]] = 0,0,0
##
##cv2.imshow('dzad.png', image2)
##cv2.imwrite("dzad.png", image2)














img = cv2.imread('dzad.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,80,
                        param1=50,param2=20,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()






















	
