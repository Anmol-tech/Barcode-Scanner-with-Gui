import pyzbar.pyzbar as pyzbar
from imutils.video import VideoStream
import imutils
import argparse
import cv2
import datetime


ap = argparse.ArgumentParser()
ap.add_argument('-o','--output',default='barcode.csv',type=str,help='output')
args = vars(ap.parse_args())

vs = VideoStream(src=0,usePiCamera=).start()

found = set()

csv = open(args['output'],'w')

while True:

    frame = vs.read()
    frame = imutils.resize(frame,width=400)

    barcodes = pyzbar.decode(frame)

    for code in barcodes:
        (x,y,w,h) = code.rect
        cv2.rectangle(frame,(x,y),(x+w,x+h),(0,0,255),2)

        bar_data = code.data.decode('utf-8')
        bar_type = code.type

        text = f'{bar_data} ({bar_type})' 
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 2)

        if bar_data not in found:
            csv.write(f'{datetime.datetime.now()} {bar_data} \n')
            csv.flush()
            found.add(bar_data)
        
    cv2.imshow("Barcode Scanner",frame)
    key = cv2.waitKey(1) & 0xFF

    if key ==ord('q'):
        break

csv.close()
cv2.destroyAllWindows()
vs.stop()