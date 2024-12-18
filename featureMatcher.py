# Building on the foundation of the feature visualizer POC, this program contains a flushed-out pipeline for using feature detection to match a tile given as an image to its numerical counterpart
# This essentially mimics the behaviour of an image recognition pipeline, but using a threshold for the number of features detected as the classifier for what tile is shown in the image

import cv2
import numpy
import os

path = 'tiles'
orb = cv2.ORB_create(nfeatures = 1000)
hand = cv2.imread("./tiles/suits/sozu.png",0)

images = []
classNames = []
unique_tiles = 0
myList = os.listdir(path)
# print(myList)
for cl in myList:
    imgCurrent = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCurrent)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findDescriptor (imgs):
    desList = []
    for img in imgs:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

desList = findDescriptor(images)
# print(len(desList))

def findID(img, desList):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalList = []
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2,k=2)
            good_match = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good_match.append([m])
            matchList.append(len(good_match))
    except:
        pass
    return matchList

findDescriptor(images)
tileList = findID(hand, desList)
print(tileList)
for i in range(0, len(tileList)):
    if tileList[i] >= 5:
        print(classNames[i] + " detected, features detected: " + str(tileList[i]))
        unique_tiles += 1
print("Number of unique tiles detected: " + str(unique_tiles) + "/13")