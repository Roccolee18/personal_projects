# Image pre-processing/cleanup pipeline testing to see if applying these techniques would yield clearer features
# Testing results prove that image pre-processing has no benefit in adding to feature detection accuracy
import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread("./tiles/1p.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = numpy.ones((5,5))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5), 5)
imgCanny = cv2.Canny(imgBlur, 100, 100)
imgDial = cv2.dilate(imgCanny, kernel, iterations=3)
imgErode = cv2.erode(imgDial, kernel, iterations=2)

titles = ["Original", "Grayscale", "Gaussian Blur", "Canny edge detection", "Dilated", "Eroded (final product)"]
images = [img, imgGray, imgBlur, imgCanny, imgDial, imgErode]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()