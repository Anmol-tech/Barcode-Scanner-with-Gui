
# Barcode Reader From Video

  
- This program is to detect the **QR CODE** and **BARCODE** in live video capturing.

- This can be used for **Raspberry Pi**. ( By changing in videostraeam and adding argument **usePiCamera=True** ).

- This will store the data in **csv** File of scanned codes.

> Command to run this program
 
 For Windows
 `python barcode-video.py -o [output file destination]`

> Output destination is not mandatory by default it is barcode.csv

For Linux and MAC OS
`python barcode-viode.py -o [outpout file destination]`

> Output destination is not mandatory by default it is barcode.csv

## Required Header File 

 - **pyzbar** `pip install pyzbar`
- **imutils**  `pip install imutils`
- **Opencv (cv2)** `pip install opencv-python`
- **argparsar** `pip install argparse`