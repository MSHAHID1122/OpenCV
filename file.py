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


def rgb_into_rg(image):
    img = cv2.imread(image)
    img[:,:,0]=0
    cv2.imshow("window",img)
    cv2.waitKey(0)

def rbg_into_rb(image):
    img = cv2.imread(image)
    img[:,:,1]=0
    cv2.imshow("window",img)
    cv2.waitKey(0)   
def rbg_into_bg(image):
    img = cv2.imread(image)
    img[:,:,2]=0 
    cv2.imshow("window",img)
    cv2.waitKey(0)    


def resize_img(image,p1,p2):
    img =cv2.imread(image)
    myimg= cv2.resize(img,(p1,p2))
    cv2.imshow("window",myimg)
    cv2.waitKey(0)


def flip_img(image):
    img = cv2.imread(image)
    #Horizontal  flip
    flip_img = cv2.flip(img,1)
    cv2.imshow("window",flip_img)
    cv2.waitKey(0)
    #Horizontal  flip

    img2 = cv2.flip(img,0)
    cv2.imshow("window",img2)
    cv2.waitKey(0)
    #horizontal flip

def crop_img(image):
    img = cv2.imread(image)
    crop = img[100:400,100:300]
    cv2.imshow("window",crop)
    cv2.waitKey(0)

def save_img(img,name:str):
    cv2.imwrite(name,img)
    
def draw_rectangle(img,p1,p2,color,thickness):
    i = cv2.imread(img)
    r=cv2.rectangle(i,p1,p2,color,thickness)
    cv2.imshow("window",r)
    cv2.waitKey(0)
def draw_circle(img,center,color,radius,thickness):
    i = cv2.imread(img)
    circle = cv2.circle(i,center,radius,color,thickness)
    cv2.imshow("window",circle)
    cv2.waitKey(0)

def interText(img,text,org,color,thickness,fontface,fontsize):
    i = cv2.imread(img)
    
    img1 = cv2.putText(i, text, org, fontface, fontsize, color, thickness)
    cv2.imshow("window",img1)
    cv2.waitKey(0)


def event_create():
    while(True):
        cv2.imshow("window",img)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
   cv2.destroyAllWindows()     




image = r"nature.jpg"
# read_image(image)
# convert_img(image)
# rbg_into_rb(image)
# rbg_into_bg(image)
# resize_img(image,40,40)
# flip_img(image)
# crop_img(image)
# draw_rectangle(image,(100,100),(300,300),(255,0,0),3)
# draw_circle(image,(400,400),(0,255,0),50,3)
font = cv2.LINE_AA
interText(img=image,text = "hello",org = (300,300),color = (255,255,0),thickness=2,fontface=font,fontsize=1)