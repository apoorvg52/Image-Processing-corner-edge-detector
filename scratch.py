import cv2
import numpy as np
import sys
import getopt
import operator
import matplotlib.pyplot as plt


def readImage(filename):
    img = cv2.imread(filename, 0)
    if img is None:
        print('Invalid image:' + filename)
        return None
    else:
        print('Image successfully read...')
        return img


def findCorners(img, window_size, k, thresh):
    dy, dx = np.gradient(img)
    Ixx = dx ** 2
    Ixy = dy * dx
    Iyy = dy ** 2
    height = img.shape[0]
    width = img.shape[1]

    cornerList = []
    newImg = img.copy()
    color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
    offset = window_size // 2

    for y in range(offset, height - offset):
        for x in range(offset, width - offset):

            windowIxx = Ixx[y - offset:y + offset + 1, x - offset:x + offset + 1]
            windowIxy = Ixy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            windowIyy = Iyy[y - offset:y + offset + 1, x - offset:x + offset + 1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            det = (Sxx * Syy) - (Sxy ** 2)
            trace = Sxx + Syy
            r = det - k * (trace ** 2)

            if r > thresh:
                #print(x, y, r)
                cornerList.append([x, y, r])
                color_img.itemset((y, x, 0), 0)
                color_img.itemset((y, x, 1), 0)
                color_img.itemset((y, x, 2), 255)
    return color_img, cornerList


#img = cv2.imread("C:/Users/Apoorv/Desktop/ip project/Capture.JPG", 0)
img = cv2.imread("C:/Users/Apoorv/Desktop/ip project/Viceroy 2.jpg", 0)
#img = cv2.imread("C:/Users/Apoorv/Desktop/ip project/checkerboard.png", 0)

#1.EDGE DETECTION
#1.1 VARAIABLE APERTURE
#CONSTANT THRESHOLD
edges = edges = cv2.Canny(img, 50, 100, apertureSize=3)
cv2.imshow('1.t1=50 t2=150 aS=3', edges)

edges = edges = cv2.Canny(img, 50, 100, apertureSize=5)
cv2.imshow('2.t1=50, t2=150 aS=5', edges)

edges = edges = cv2.Canny(img, 50, 100, apertureSize=7)
cv2.imshow('3.t1=50 t2=150 aS=7', edges)


#1.2 CONSTANT APERTURE
#CHANGE IN THRESHOLD
edges = edges = cv2.Canny(img, 50, 100, apertureSize=3)
cv2.imshow('4.t1=50 t2=150 aS=3', edges)

edges = edges = cv2.Canny(img, 25, 400, apertureSize=3)
cv2.imshow('5.t1=25 t2=150 aS=3', edges)

edges = edges = cv2.Canny(img, 70, 100, apertureSize=3)
cv2.imshow('6.t1=50 t2=150 aS=3', edges)



#2 Corner detection
#change in window size
col, listing = findCorners(img, 4, 0.21, 100)
cv2.imshow('7.T=100 W=4', col)

col, listing = findCorners(img, 2, 0.21, 100)
cv2.imshow('8.T=100 W=2', col)



#change in threshold
col, listing = findCorners(img, 3, 0.21, 75)
cv2.imshow('9.T=75 W=3', col)

col, listing = findCorners(img, 3, 0.21, 20)
cv2.imshow('10.T=20 W=3', col)



#3.finally
#both edge and corner detection.
col, listing = findCorners(edges, 3, 0.15, 0)
cv2.imshow('k1', col)

col, listing = findCorners(edges, 4, 0.15, 0)
cv2.imshow('k2', col)

col, listing = findCorners(edges, 3, 0.09, 400)
cv2.imshow('k3', col)

cv2.waitKey(0)
cv2.destroyAllWindows()