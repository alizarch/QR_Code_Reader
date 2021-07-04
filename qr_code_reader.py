import cv2
from pyzbar.pyzbar import decode
import time

def qr_read_from_image(img):
    qr_code = decode(img)
    if qr_code == None:
        print("Unvalid QR Code")
    else:
        for code in qr_code:
            print("------------------------------------------------")
            print("Code Type:\t",code.type)
            print("Code Data:\t",code.data.decode('utf-8'))
            print("------------------------------------------------")


def live_qr_read():
    try:
        cap = cv2.VideoCapture(0)
        cap.set(3 , 640)
        cap.set(4 , 480)
        used_codes=[]
        camera =True
        while camera == True:
            syccess, frame = cap.read()
            qr_code = decode(frame)
            if qr_code == None:
                print("Unvalid QR Code")
            for code in qr_code:
                if code.data.decode('utf-8') not in used_codes:
                    print("------------------------------------------------")
                    print("Approved. You can enter!")
                    print("Code Type:\t", code.type)
                    print("Code Data:\t", code.data.decode('utf-8'))
                    print("------------------------------------------------")

                    used_codes.append(code.data.decode('utf-8'))
                    time.sleep(5)
                elif code.data.decode('utf-8') in used_codes:
                    print("Sorry, this code has been already used! ")
                    time.sleep(5)
                else:
                    pass
            cv2.imshow('Testing-Code-Scan', frame)
            cv2.waitKey(1)
    except:
        print("Unvalid QR Code")

def main():
    while True:
        print("\nEnter 1: Read QR Code from image")
        print("Enter 2: Read QR Code from live camera")
        choice = int(input("Choose your Choise: "))
        
        if choice ==1:
            img = cv2.imread('img6.jpeg')
            qr_read_from_image(img)
        if choice == 2:
            live_qr_read()
        else:
            pass

if __name__ =="__main__":
    main()
