import cv2


# Reading the  image and printing it onto the screen
def read_image(image):
    
    img = cv2.imread(image)
    if img is None:
        print( "no image found")
    cv2.imshow("window",img)
    cv2.waitKey(0)


def convert_img(image):
    img = cv2.imread(image)
    if img is None:
        return None
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("window",gray_img)
    cv2.waitKey(0)

    
image = r"nature.jpg"
read_image(image)
convert_img(image)