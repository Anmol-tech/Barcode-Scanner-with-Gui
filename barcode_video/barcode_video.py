import pyzbar.pyzbar as pyzbar
from imutils.video import VideoStream, FileVideoStream
import imutils
import argparse
import cv2
import datetime

class Detector_cam:
    def scan_file(self,fname):
        vs = FileVideoStream(fname).start()

        while True:

            frame = vs.read()
            # frame = imutils.resize(frame)

            barcodes = pyzbar.decode(frame)

            for code in barcodes:
                (x,y,w,h) = code.rect
                cv2.rectangle(frame,(x,y),(x+w,x+h),(0,0,255),2)

                bar_data = code.data.decode('utf-8')
                bar_type = code.type

                text = f'{bar_data} ({bar_type})' 
                cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 2)

                
            cv2.imshow("Barcode Scanner",frame)
            key = cv2.waitKey(1) & 0xFF

            if key ==ord('q'):
                break

        cv2.destroyAllWindows()
        vs.stop()


    def scan(self):

        vs = VideoStream(src=0).start()

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

                
            cv2.imshow("Barcode Scanner",frame)
            key = cv2.waitKey(1) & 0xFF

            if key ==ord('q'):
                break

        cv2.destroyAllWindows()
        vs.stop()

if __name__ == "__main__":
    obj = Detector_cam()
    obj.scan()
    