import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("Solar-System",img)



cv2.putText(img,"Hi I am Sun",(100,100),cv2.ACCESS_FAST,1 ,color=(255,255,255))

cv2.waitKey(0)


cv2.imwrite("Solar.jpg",img)