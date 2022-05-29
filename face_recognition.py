from ctypes.wintypes import _COORD
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from cv2 import VideoCapture, putText
from matplotlib.pyplot import gray
import mysql.connector
from tkinter import messagebox
import cv2
import os
import numpy as npf5
from sklearn.preprocessing import scale

class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=2000,height=60)

        img_top = Image.open(r"C:\Face_Recognition_System\Image\maskcovid.jpg")
        img_top = img_top.resize((2000, 1000), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=2000, height=1000)


        btn_frame = Button(self.root, text="Recognize The Face",command=self.face_recog, bd=2,font=("times new roman",28,"bold"), relief=RIDGE, bg="gray")
        btn_frame.place(x=0, y=380, width=2000, height=60)


        btn_frame = Button(self.root, text="Wait for some seconds", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=600, y=580, width=300, height=60)

        btn_frame = Button(self.root, text="Press Q for Exit", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=1000, y=580, width=300, height=60)




    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                

                conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from covid where Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                

                my_cursor.execute("select Age from covid where Id="+str(id))
                a=my_cursor.fetchone()
                a="+".join(a)

                my_cursor.execute("select Profession from covid where Id="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)
                



                if confidence>82:
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Age:{a}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Profession:{p}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
        
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
                
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Recognition started",img)
                
            if cv2.waitKey(1)==ord("q"):
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
