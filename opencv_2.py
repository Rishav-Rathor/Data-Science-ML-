import cv2

img = cv2.imread('dog.png')

cv2.imshow('Dog Image', img)
cv2.waitKey(0)# Zero h to infinte time k liye window open rhega but in 250 krenge to mili seconds k liye hoga
cv2.destroyAllWindows()
