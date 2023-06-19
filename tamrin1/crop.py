

import cv2

img = cv2.imread("mnist.png")

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
print(img2.shape)

#number = img2 [20:40 , 0:20] 

#img2[0:20 , 20:40] = number

#cv2.imshow("",number)
#cv2.waitKey()
#cv2.imwrite("numberss",number)

a =0
b =0

for i in range(0,1000,20):
    for j in range(0,2000,20):
        name = img2[i:i+20, j:j+20]
        path = "dataset" + str(a) + "a" + str(a) + str(b) + ".png"
        b = b +1
        cv2.imwrite(path, name)
    if a ==500:
        b = b+1
        a = 0    
        
         