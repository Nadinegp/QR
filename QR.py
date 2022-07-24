import cv2
import webbrowser

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()
img = cv2.imread("QRCode.jpg")

# while True:
# img = cap.read()

data= detector.detectAndDecode(img)
if data:
    a=data
    # break
cv2.imshow("QRCODEscanner", img)
# if cv2.waitKey(1) == ord("q"):
#     break
b=webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()