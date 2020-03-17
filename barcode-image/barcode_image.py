import pyzbar.pyzbar as pyzbar
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help="path of image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

bars = pyzbar.decode(image)

for bar in bars:
    (x,y,w,h) = bar.rect
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)


    bardata = bar.data.decode('utf-8')
    bartype = bar.type

    text = '{} ({})'.format(bardata,bartype)
    cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

    print(f'[INFO] found {bartype} barcode:{bardata}')

cv2.imshow("Image",image)
cv2.waitKey(0)