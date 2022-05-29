# It is highly recommended to run the file via index.py otherwise there will be difference in size of window size if you open it directly due to import of pywhatkit in another file of python.

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Covid:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x1000+0+0")
        self.root.title("Face Recognition System")

        # Variable
        self.var_profession = StringVar()
        self.var_place = StringVar()
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_id=StringVar()
        self.var_age = StringVar()
        self.var_place_of_death = StringVar()

        img2 = Image.open(r"C:\Face_Recognition_System\Image\maskcovid.jpg")
        img2 = img2.resize((2000, 1000), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg = Label(self.root, image=self.photoimg2)
        bg.place(x=0, y=0, width=2000, height=1000)

        main_frame = Frame(bg, bd=2, bg="white")
        main_frame.place(x=30, y=55, width=1980, height=900)

        Left_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE, text="COVID PATIENT DETAILS")
        Left_frame.place(x=10, y=10, width=930, height=870)

        img_left = Image.open(r"C:\Face_Recognition_System\Image\corona.jpg")
        img_left = img_left.resize((930, 330), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=45, y=105, width=930, height=130)

        # Profession
        Profession_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Information", font=(
            "times new roman", 13, "bold"), fg="red")
        Profession_frame.place(x=10, y=160, width=900, height=190)

        dep_label = Label(Profession_frame, text="Profession", font=(
            "times new roman", 13, "bold"), bg="white", fg="blue")
        dep_label.grid(row=0, column=0, padx=15)

        dep_combo = ttk.Combobox(Profession_frame, textvariable=self.var_profession, font=(
            "times new roman", 13, "bold"), width=22, state="read only")
        dep_combo["values"] = ("Select Profession", "Politician",
                               "Engineer", "Singer", "Actor", "Doctor", "Unknown", "Labour")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=3, pady=30, sticky=W)

        # Place
        place_label = Label(Profession_frame, text="Place", font=(
            "times new roman", 13, "bold"), bg="white", fg="blue")
        place_label.grid(row=0, column=2, padx=30, sticky=W)

        place_combo = ttk.Combobox(Profession_frame, textvariable=self.var_place, font=(
            "times new roman", 13, "bold"), width=22, state="read only")
        place_combo["values"] = ("Select Place", "USA", "Italy",
                                 "India", "Germany", "France", "South KOrea", "China")
        place_combo.current(0)
        place_combo.grid(row=0, column=3, padx=3, pady=30, sticky=W)

        # Month
        Month_label = Label(Profession_frame, text="Month", font=(
            "times new roman", 13, "bold"), bg="white", fg="blue")
        Month_label.grid(row=1, column=0, padx=30, sticky=W)

        Month_combo = ttk.Combobox(Profession_frame, textvariable=self.var_month, font=(
            "times new roman", 13, "bold"), width=22, state="read only")
        Month_combo["values"] = ("Select Month", "January", "Feburary", "March", "April",
                                 "May", "June", "July", "August", "September", "October", "November", "December")
        Month_combo.current(0)
        Month_combo.grid(row=1, column=1, padx=3, pady=30, sticky=W)

        # Year
        Year_label = Label(Profession_frame, text="Year", font=(
            "times new roman", 13, "bold"), bg="white", fg="blue")
        Year_label.grid(row=1, column=2, padx=30, sticky=W)

        Year_combo = ttk.Combobox(Profession_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), width=22, state="read only")
        Year_combo["values"] = ("Select Year", "2019", "2020", "2021", "2022")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=3, padx=3, pady=30, sticky=W)

        # Information about Patients
        Patient_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                   text="Information of Covid Patient", font=("times new roman", 13, "bold"), fg="blue")
        Patient_frame.place(x=5, y=350, width=910, height=600)


        # Names
        Patient_name = Label(Patient_frame, text="Patient Name",
                             font=("times new roman", 13, "bold"))
        Patient_name.grid(row=0, column=0, padx=10,pady=20, sticky=W)

        Patient_name_entry = ttk.Entry(
            Patient_frame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        Patient_name_entry.grid(row=0, column=1, padx=10, pady=20, sticky=W)

        # Gender
        Patient_gender = Label(Patient_frame, text="Patient Gender", font=(
            "times new roman", 13, "bold"))
        Patient_gender.grid(row=1, column=0,pady=20,sticky=W)

        gender_combo=ttk.Combobox(Patient_frame,textvariable=self.var_gender,font=("times new roman", 13, "bold"))
        gender_combo["values"]=("Male","female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,sticky=W)


        # Age
        Patient_age = Label(Patient_frame, text="Patient Age",
                            font=("times new roman", 13, "bold"))
        Patient_age.grid(row=0, column=2, padx=10, pady=20, sticky=W)

        Patient_age_entry = ttk.Entry(
            Patient_frame, textvariable=self.var_age, width=18, font=("times new roman", 13, "bold"))
        Patient_age_entry.grid(row=0, column=3, padx=10, pady=20, sticky=W)

        # Place of Death

        Patient_death = Label(Patient_frame, text="Patient Place of Death", font=(
            "times new roman", 13, "bold"))
        Patient_death.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        Patient_death_entry = ttk.Entry(
            Patient_frame, textvariable=self.var_place_of_death, width=18, font=("times new roman", 13, "bold"))
        Patient_death_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # Id
        Patient_id = Label(Patient_frame, text="Patient Id",
                             font=("times new roman", 13, "bold"))
        Patient_id.grid(row=2, column=0,sticky=W)

        Patient_id_entry = ttk.Entry(
            Patient_frame, textvariable=self.var_id, width=20, font=("times new roman", 13, "bold"))
        Patient_id_entry.grid(row=2, column=1,pady=5, sticky=W)


        self.var_radio1 = StringVar()
        radio_button1 = ttk.Radiobutton(
            Patient_frame, variable=self.var_radio1, text="Take Photo As Sample", value="Yes")
        radio_button1.grid(row=4, column=0,padx=4,pady=30)

        self.var_radio2 = StringVar()
        radio_button2 = ttk.Radiobutton(
            Patient_frame, variable=self.var_radio1, text="No Photo As Sample", value="No")
        radio_button2.grid(row=4, column=1,padx=4,pady=30)

        # buttons frame
        btn_frame = Frame(Patient_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=320, width=930, height=100)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=(
            "times new roman", 12, "bold"), bg="white", fg="red",)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=18, font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        update_btn.grid(row=0,column=1)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        reset_btn.grid(row=0, column=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data,width=18, font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        delete_btn.grid(row=0, column=3)

        btn_frame1 = Frame(Patient_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=400, width=920, height=75)

        take_btn = Button(btn_frame1, text="Take Photo Sample",command=self.generate_dataset,width=38, font=(
            "times new roman", 13, "bold"), bg="blue", fg="red")
        take_btn.grid(row=1, column=1)

        update_btn = Button(btn_frame1, text="Update the Photo",width=38,font=(
            "times new roman", 13, "bold"), bg="blue", fg="red")
        update_btn.grid(row=1, column=2)

        Right_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE, text="COVID PATIENT DETAILS")
        Right_frame.place(x=950, y=10, width=930, height=880)

        img_right = Image.open(r"C:\Face_Recognition_System\Image\maskcovid.jpg")
        img_right = img_right.resize((930, 330), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=985, y=95, width=916, height=130)

        # Search
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search Results", font=("times new roman", 13, "bold"))
        Search_frame.place(x=5, y=135, width=910, height=520)

        Search_label = Label(Search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="white", fg="blue")
        Search_label.grid(row=0, column=0, padx=20, pady=15, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 13, "bold"), width=17, state="read only")
        search_combo["values"] = (
            "Select", "Profession", "Month", "Year", "Place")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=3, pady=10, sticky=W)

        search_entry = ttk.Entry(
            Search_frame, width=18, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=12, font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        search_btn.grid(row=0, column=3)

        showAll_btn = Button(Search_frame, text="Show All", width=11, font=(
            "times new roman", 12, "bold"), bg="white", fg="red")
        showAll_btn.grid(row=0, column=4)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=260, width=900, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Covid_Patient_Table = ttk.Treeview(table_frame, column=(
            "profession", "place", "month", "year", "name", "gender","id", "age","place of death","photo"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Covid_Patient_Table.xview)
        scroll_y.config(command=self.Covid_Patient_Table.yview)

        self.Covid_Patient_Table.heading("profession", text="Profession")
        self.Covid_Patient_Table.heading("place", text="Place")
        self.Covid_Patient_Table.heading("month", text="Month")
        self.Covid_Patient_Table.heading("year", text="Year")
        self.Covid_Patient_Table.heading(
            "name", text="Name")
        self.Covid_Patient_Table.heading("gender", text="Gender")
        self.Covid_Patient_Table.heading("id", text="Id")
        self.Covid_Patient_Table.heading("age",text="Age")
        self.Covid_Patient_Table.heading("place of death",text="Place of death")
        self.Covid_Patient_Table.heading("photo", text="Photo")
        self.Covid_Patient_Table["show"] = "headings"

        self.Covid_Patient_Table.column("profession", width=100)
        self.Covid_Patient_Table.column("place",width=100)
        self.Covid_Patient_Table.column("month", width=100)
        self.Covid_Patient_Table.column("year", width=100)
        self.Covid_Patient_Table.column("name", width=100)
        self.Covid_Patient_Table.column("gender", width=100)
        self.Covid_Patient_Table.column("id", width=100)
        self.Covid_Patient_Table.column("age", width=100)
        self.Covid_Patient_Table.column("place of death",width=100)
        self.Covid_Patient_Table.column("photo", width=100)

        self.Covid_Patient_Table.pack(fill=BOTH, expand=1)


        self.Covid_Patient_Table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# function

    def add_data(self):
        if self.var_profession.get() == "" or self.var_month.get() == "" or self.var_place.get() == "" or self.var_year.get() == "":
            messagebox.showerror(
                "Error", "Fill information for better results", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into covid values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_profession.get(),
                    self.var_place.get(),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_id.get(),
                    self.var_age.get(),
                    self.var_place_of_death.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Information added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

# Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from covid")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.Covid_Patient_Table.delete(*self.Covid_Patient_Table.get_children())
            for i in data:
                self.Covid_Patient_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

# Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.Covid_Patient_Table.focus()
        content=self.Covid_Patient_Table.item(cursor_focus)
        data=content["values"]

        self.var_profession.set(data[0]),
        self.var_place.set(data[1]),
        self.var_month.set(data[2]),
        self.var_year.set(data[3]),
        self.var_name.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_id.set(data[6]),
        self.var_age.set(data[7]),
        self.var_place_of_death.set(data[8]),
        self.var_radio1.set(data[9]),



# update function
    def update_data(self):
        if self.var_profession.get()=="" or self.var_place.get()=="" or self.var_month.get()=="" or self.var_year.get()=="":
            messagebox.showerror("Error","All Fields are required for best results",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you Want to Update",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update covid set Profession=%s,Place=%s,Month=%s,Year=%s,Name=%s,Gender=%s,Age=%s,`Place of death`=%s,Photo=%s where Id=%s",(
                    self.var_profession.get(),
                    self.var_place.get(),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_age.get(),
                    self.var_place_of_death.get(),
                    self.var_radio1.get(), 
                    self.var_id.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            

# Delete
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Name is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you Want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from covid where Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     

# Reset
    def reset_data(self):
        self.var_profession.set("Select Profession")
        self.var_place.set("Select Place")
        self.var_month.set("Select Month")
        self.var_year.set("Select Year")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_id.set("")
        self.var_age.set("")
        self.var_place_of_death.set("")
        self.var_radio1.set("")
    


# Generate data
    def generate_dataset(self):
        if self.var_profession.get()=="" or self.var_place.get()=="" or self.var_month.get()=="" or self.var_year.get()=="":
            messagebox.showerror("Error","All Fields are required for best results",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Ayushi1730@",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from covid")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                my_cursor.execute("update covid set Profession=%s,Place=%s,Month=%s,Year=%s,Name=%s,Gender=%s,Age=%s,`Place of death`=%s,Photo=%s where Id=%s",(
                        self.var_profession.get(),
                        self.var_place.get(),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_name.get() ,   
                        self.var_gender.get(),
                        self.var_age.get(),
                        self.var_place_of_death.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                        ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load data on frontals

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame=cap.read()
                    if face_cropped(frame) is None:
                        break
                    else:
                        img_id+=1
                    face=cv2.resize(face_cropped(frame),(350,350))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data1/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped face",face)
                    
                    if cv2.waitKey(1)==ord("q")  or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set")

            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Covid(root)
    root.mainloop()
