import cv2
import mediapipe as mp

mpHands=mp.solutions.hands      #Integrate Hand Tracking
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

video=cv2.VideoCapture(0)

while True:
    ret,img=video.read()
    img=cv2.flip(img,1)
    rgbimg=cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)         #Convert the BGR into RGB
    result=hands.process(rgbimg)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            for id, lm in enumerate(hand.landmark):
                h,w,c=img.shape
                coorx, coory= int (lm.x*w), int(lm.y*h)
                print(coorx)
                print(coory)
                cv2.circle(img, (coorx, coory),6,(50,50,255),-1)
            #mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
    print(result)
    cv2.imshow("Image",img)
    k=cv2.waitKey(1)         #Shut the Camera off
    if k == 27:               #Press ESC key to exit
        break
video.release()
cv2.destroyAllWindows()


