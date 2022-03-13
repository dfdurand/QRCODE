import cv2
import numpy as np
from pyzbar.pyzbar import decode


#image

# img = cv2.imread('photos/yt.png')
#
# code = decode(img)
#
# print(code)

cap = cv2.VideoCapture(0)
cap.set(3, 640) #largeur
cap.set(4, 480) #hauteur

while True:

    ret, img = cap.read()

    for barcode in decode(img):
        # print(barcode.data)
        data = barcode.data.decode('utf-8')
        print(data)

        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        print(pts)
        cv2.polylines(img, [pts], True, (255,0,255), 5)
        pts2 = barcode.rect

        cv2.putText(img, data, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)


    cv2.imshow("show qr", img)
    cv2.waitKey(1)


