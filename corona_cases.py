# It is highly recommended to run the file via index.py otherwise there will be difference in size of window size if you open it directly due to import of pywhatkit in another file of python.

import requests
import bs4
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class CovidNo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Covid Cases")

        img_top = Image.open(r"C:\Face_Recognition_System\Image\music.jpg")
        img_top = img_top.resize((2000,1000), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=2000, height=1000)

        title_lbl=Label(self.root,text="Covid Cases",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=2000,height=60)

        btn_frame = Button(self.root, text="Detect Covid Cases",command=self.Test, bd=2,font=("times new roman",28,"bold"), relief=RIDGE, bg="gray")
        btn_frame.place(x=0, y=380, width=2000, height=60)

        btn_frame = Button(self.root, text="Wait for some minutes", bd=2,font=("times new roman",15,"bold"), relief=RIDGE, bg="white")
        btn_frame.place(x=850, y=580, width=300, height=60)

       

    def Test(self):


        def get_html_data(url):
            data =requests.get(url)
            return data
            

        def get_covid_data():
            
            url="https://www.worldometers.info/coronavirus/"

            html_data=get_html_data(url)
            bs=bs4.BeautifulSoup(html_data.text,'html.parser')
            info_div =bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
            all_data=" "

            for i in range(3):
                text =info_div[i].find("h1",class_=None).get_text()
                count=info_div[i].find("span",class_=None).get_text()
                all_data=all_data+text+" "+count+"\n"

            return all_data

        def get_country_data():
            name=textfield.get()
            url="https://www.worldometers.info/coronavirus/country/"+name
            html_data=get_html_data(url)
            bs=bs4.BeautifulSoup(html_data.text,'html.parser')
            info_div =bs.find("div",class_="content-inner").findAll("div",id="maincounter-wrap")
            all_data=" "

            for i in range(3):
                text =info_div[i].find("h1",class_=None).get_text()

                count=info_div[i].find("span",class_=None).get_text()

                all_data=all_data+ text +" "+ count +"\n"

            mainlabel['text']=all_data


        def reload():
            new_data=get_covid_data()
            mainlabel['text']=new_data


        get_covid_data()


        root=tk.Tk()
        root.geometry("2000x1000")
        root.title("Covid Tracker")
        root['background']='Grey'
        f=("poppins",25,"bold")
        
        main1label=tk.Label(root,text="SEARCH COUNTRIES",font=f,bg="black",fg="red")
        main1label.pack(pady=40)

        textfield=tk.Entry(root,width=20,font=f)
        textfield.pack(pady=60)
        
        mainlabel=tk.Label(root,text=get_covid_data(),font=f)
        mainlabel.pack(pady=40)


        gbtn=tk.Button(root,text="Get Data",font=f,relief='solid',command=get_country_data,fg="red")
        gbtn.pack(pady=40)

        rbtn=tk.Button(root,text="Reload",font=f,relief='solid',command=reload,fg="red")
        rbtn.pack(pady=40)

        root.mainloop()

if __name__=="__main__":
    root=Tk()
    obj=CovidNo(root)
    root.mainloop()
