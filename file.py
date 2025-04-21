import cv2


image = r"C:\Users\User\Pictures\nature.jpg"
img = cv2.imread(image)
if img is None:
    print("now image found")
cv2.imshow("window",img)
cv2.waitkey(0)