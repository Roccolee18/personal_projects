# Visualizing the ORB feature detector results from detecting a specific tile from a hand of tiles
import cv2
import numpy

img1 = cv2.imread("./tiles/2s.png")
# img1_color = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# kernel = numpy.ones((5,5))
# img1_Gray = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
# img1_Blur = cv2.GaussianBlur(img1_Gray, (5,5), 1)
# img1_Canny = cv2.Canny(img1_Blur, 100, 100)
img2 = cv2.imread("./tiles/suits/sozu.png")
# img2_color = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# img2_Gray = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)
# img2_Blur = cv2.GaussianBlur(img2_Gray, (5,5), 1)
# img2_Canny = cv2.Canny(img2_Blur, 100, 100)

orb = cv2.ORB_create(nfeatures=1000)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2,k=2)

good_match = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good_match.append([m])
print("Number of good feature matches: " + str(len(good_match)))

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_match, None, flags = 2)

# cv2.imshow("imgKp1", imgKp1)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.waitKey(0)

cv2.destroyAllWindows()