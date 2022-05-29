from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from covid import Covid
from train_face import Train
from face_recognition import Face_recognition
from detect_mask_video import Detect_mask
from test_emotion import Music
from corona_cases import CovidNo

class face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2000x1000+0+0")
        self.root.title("face Recognition System")

        img1=Image.open(r"C:\Face_Recognition_System\Image\covid2.jpg")
        img1=img1.resize((2000,1000),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=2000,height=1000)

        title_lbl=Label(f_lbl,text="FIGHT BY TECH",font=("times new roman",35,"bold"),bg="black",fg="red")
        title_lbl.place(x=0,y=0,width=2000,height=45)

        img2=Image.open(r"C:\Face_Recognition_System\Image\corona.jpg")
        img2=img2.resize((320,320),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(f_lbl,image=self.photoimg2,command=self.covid_patient_details,cursor="hand2")
        b1.place(x=200,y=100,width=320,height=320)

        b1_1=Button(f_lbl,text="Covid Patient Details",command=self.covid_patient_details,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b1_1.place(x=200,y=400,width=320,height=40)

        img3=Image.open(r"C:\Face_Recognition_System\Image\train1.jpg")
        img3=img3.resize((320,320),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(f_lbl,image=self.photoimg3,command=self.train_data,cursor="hand2")
        b2.place(x=800,y=100,width=320,height=320)

        b2_1=Button(f_lbl,text="Train Data",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b2_1.place(x=800,y=400,width=320,height=40)


        img4=Image.open(r"C:\Face_Recognition_System\Image\face.jpg")
        img4=img4.resize((320,320),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(f_lbl,image=self.photoimg4,command=self.face_recognition,cursor="hand2")
        b3.place(x=1400,y=100,width=320,height=320)

        b3_1=Button(f_lbl,text="Search Faces",command=self.face_recognition,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b3_1.place(x=1400,y=400,width=320,height=40)


        img5=Image.open(r"C:\Face_Recognition_System\Image\woman.jpg")
        img5=img5.resize((320,320),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4=Button(f_lbl,image=self.photoimg5,command=self.detect_mask,cursor="hand2")
        b4.place(x=200,y=480,width=320,height=320)

        b4_1=Button(f_lbl,text="Mask Detection",command=self.detect_mask,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b4_1.place(x=200,y=780,width=320,height=40)

        img6=Image.open(r"C:\Face_Recognition_System\Image\covid1.jpg")
        img6=img6.resize((320,320),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(f_lbl,image=self.photoimg6,command=self.emotion_with_music,cursor="hand2")
        b5.place(x=800,y=480,width=320,height=320)

        b5_1=Button(f_lbl,text="Heal Your Soul",command=self.emotion_with_music,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b5_1.place(x=800,y=780,width=320,height=40)

        img7=Image.open(r"C:\Face_Recognition_System\Image\facemask.jpg")
        img7=img7.resize((320,320),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b6=Button(f_lbl,image=self.photoimg7,command=self.corona_cases,cursor="hand2")
        b6.place(x=1400,y=480,width=320,height=320)

        b6_1=Button(f_lbl,text="Covid Cases",command=self.corona_cases,font=("times new roman",15,"bold"),bg="black",fg="red",cursor="hand2")
        b6_1.place(x=1400,y=780,width=320,height=40)
        

    # function buttons

    def covid_patient_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Covid(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def detect_mask(self):
        self.new_window=Toplevel(self.root)
        self.app=Detect_mask(self.new_window)
    
    def emotion_with_music(self):
        self.new_window=Toplevel(self.root)
        self.app=Music(self.new_window)

    def corona_cases(self):
        self.new_window=Toplevel(self.root)
        self.app=CovidNo(self.new_window)

    



if __name__=="__main__":
    root=Tk()
    obj=face_Recognition_System(root)
    root.mainloop()