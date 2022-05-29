#  It is highly recommended to run the file via index.py otherwise there will be difference in size of window size if you open it directly due to import of pywhatkit in another file of python.

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Train Data")


        title_lbl=Label(self.root,text="Train Data",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=2000,height=60)

        img_top = Image.open(r"C:\Face_Recognition_System\Image\train2.jpg")
        img_top = img_top.resize((2000, 1000), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=2000, height=1000)


        btn_frame = Button(self.root, text="Train Data",command=self.train_classifier, bd=2,font=("times new roman",28,"bold"), relief=RIDGE, bg="gray")
        btn_frame.place(x=0, y=380, width=2000, height=60)


    def train_classifier(self):
        data_dir=("data1")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # Train the classifier And save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")







if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
