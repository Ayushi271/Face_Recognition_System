from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import cv2
import numpy as np
from keras.models import load_model
import pywhatkit  
import os


class Music:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Music")

        img_top = Image.open(r"C:\Face_Recognition_System\Image\music.jpg")
        img_top = img_top.resize((2000,1000), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=2000, height=1000)

        title_lbl=Label(self.root,text="Music with emotion",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=2000,height=60)

        btn_frame = Button(self.root, text="Heal Your Soul",command=self.Music, bd=2,font=("times new roman",28,"bold"), relief=RIDGE, bg="gray")
        btn_frame.place(x=0, y=380, width=2000, height=60)

        btn_frame = Button(self.root, text="Wait for some minutes", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=600, y=580, width=300, height=60)

        btn_frame = Button(self.root, text="Press A for clicking Photos", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=1000, y=580, width=300, height=60)

        btn_frame = Button(self.root, text="Press Q for Exit", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=800, y=780, width=300, height=60)


    def Music(self):
        model=load_model('model_file_30epochs.h5')


        video=cv2.VideoCapture(0)

        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        labels_dict={0:'Angry',1:'Disgust', 2:'Fear', 3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}

        img_counter=0
        while True:
            ret,frame=video.read()
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces= faceDetect.detectMultiScale(gray, 1.3, 3)
            for x,y,w,h in faces:
                sub_face_img=gray[y:y+h, x:x+w]
                resized=cv2.resize(sub_face_img,(48,48))
                normalize=resized/255.0
                reshaped=np.reshape(normalize, (1, 48, 48, 1))
                result=model.predict(reshaped)
                label=np.argmax(result, axis=1)[0]
                print(label)

            cv2.imshow("Frame",frame)
            k=cv2.waitKey(1)
            if k==ord('q'):
                break
            
            elif k== ord('a'): 
                global img_name
                img_name="{}.jpg".format(img_counter)
                paths='C:/Face_Recognition_System'
                cv2.imwrite(os.path.join(paths,img_name),frame)
                print("{}written!".format(img_name))
                img_counter+=1
                
        video.release()
        cv2.destroyAllWindows()


        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        labels_dict={0:'Angry',1:'Disgust', 2:'Fear', 3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}

        # len(number_of_image), image_height, image_width, channel

        frame=cv2.imread(img_name)
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces= faceDetect.detectMultiScale(gray, 1.3, 3)

        for x,y,w,h in faces:
            sub_face_img=gray[y:y+h, x:x+w]
            resized=cv2.resize(sub_face_img,(48,48))
            normalize=resized/255.0
            reshaped=np.reshape(normalize, (1, 48, 48, 1))
            result=model.predict(reshaped)
            label=np.argmax(result, axis=1)[0]
            print(label)
            if label ==0:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=saesY1Ld9nU")
            elif label ==1:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=7XBS-hu6Agg")
            elif label ==2:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=iW16WWmWZL4")
            elif label ==3:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=BPaYNAXsNmE")
            elif label ==4:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=5mFTXbZzOAE")
            elif label ==5:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=zgh4W4FMYtE")
            else:
                pywhatkit.playonyt("https://www.youtube.com/watch?v=0Vhe72NMZJc")

            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
            cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
            cv2.putText(frame, labels_dict[label], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

                
        cv2.imshow("Frame",frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Music(root)
    root.mainloop()