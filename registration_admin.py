from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import sqlite3
import re
import cv2


con = sqlite3.connect("student.db")
cur=con.cursor()
td = cur.execute("select * from sqlite_master where type='table' and name = 'student'").fetchall()
if td==[]:
    cur.execute("create table student(user_type varchr2,department varchr2,course varchr2,year varchr2,semester varchr2,student_id varchr2 primarykey,name varchr2,email_id varchr2,phone_no number,gender varchr2,address varchr2,password varchar2,confirm_password varchr2)")
#creating staff table
conn = sqlite3.connect("student.db")
curr=conn.cursor()
tdd = curr.execute("select * from sqlite_master where type='table' and name = 'staff'").fetchall()
if tdd==[]:
    curr.execute("create table staff(user_type varchr2,student_id varchr2 primarykey,name varchr2,email_id varchr2,phone_no number,gender varchr2,address varchr2,password varchar2,confirm_password varchr2)")
class registration:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Registration page")
        bg_img=Image.open(r"images/bg_registration_img.jpg")
        bg_img=bg_img.resize((1550,850),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=0,width=1530,height=850)
        titel_lbl=Label(bg_img,text="Registration portel",font=("times",35,'bold'),bg='darkblue',fg='yellow')
        titel_lbl.place(x=0,y=0,width=1530,height=55)
        #creating text variables
        self.user_type = tk.StringVar()
        self.user_type.set("student")
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_password=StringVar()
        self.var_confirmpassword=StringVar()
        self.email_error_shown = False
        self.phone_error_shown = False

        #creating frame for registration
        frame=Frame(self.root,bg="darkblue")
        frame.place(x=550,y=90,width=500,height=680)
        #craeting lable frame foe selectging admin and student as well as radio btn
        radio_labf=LabelFrame(frame,text="select Admin or student",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
        radio_labf.place(x=5,y=5,width=490,height=80)
        #creatin style to radio button using style class of ttk
        style=ttk.Style()
        style.configure("TRadiobutton",font=("times new roman",12,'bold'))
        style.configure("TRadiobutton",background="darkblue",foreground="yellow")
        #radio button
        student_radiobtn=ttk.Radiobutton(radio_labf, text="student", value="student",variable=self.user_type,command=self.update_fields)
        student_radiobtn.place(x=5,y=2)
        admin_radiobtn=ttk.Radiobutton(radio_labf, text="admin", value="admin",variable=self.user_type,command=self.update_fields)
        admin_radiobtn.place(x=100,y=2)
        #Course details lable frame
        self.courselblf=LabelFrame(frame,text="Course Details",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
        self.courselblf.place(x=5,y=90,width=490,height=150)
        #student details
        self.student_details_lblf=LabelFrame(frame,text="Student Details",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
        self.student_details_lblf.place(x=5,y=240,width=490,height=250)
        #craeting textbok and lable for course
        department_lbl=Label(self.courselblf,text="Department",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        department_lbl.place(x=5,y=10)
        year_lbl=Label(self.courselblf,text="Session Year",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        year_lbl.place(x=5,y=60)
        course_lbl=Label(self.courselblf,text="Course",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        course_lbl.place(x=260,y=10)
        sem_lbl=Label(self.courselblf,text="Semester",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        sem_lbl.place(x=260,y=60)
                #crearting combobox for all entry
        department_comb=ttk.Combobox(self.courselblf,state="readonly",textvariable=self.var_dep,font=("times new roman",10,'bold'))        
        department_comb["values"]=("Computer Science","Science","Arts","commerce")
        department_comb.place(x=100,y=10,width=150)
        year_comb=ttk.Combobox(self.courselblf,state="readonly",textvariable=self.var_year,font=("times new roman",10,'bold'))        
        year_comb["values"]=("2020-21","2021-22","2022-23","2022-24","2024-25","2025-26","2026-27","2027-28","2028-29","2029-30")
        year_comb.place(x=100,y=60,width=150)
        course_comb=ttk.Combobox(self.courselblf,state="readonly",textvariable=self.var_course,font=("times new roman",10,'bold'))        
        course_comb["values"]=("BCA","BCOM","BA","BSC")
        course_comb.place(x=330,y=10,width=150)
        sem_comb=ttk.Combobox(self.courselblf,state="readonly",textvariable=self.var_semester,font=("times new roman",10,'bold'))        
        sem_comb["values"]=("I","II","III","IV","V","VI")
        sem_comb.place(x=330,y=60,width=150)
        # adding place holder to combobox
        placeholder="Select Option"
        department_comb.set(placeholder)
        year_comb.set(placeholder)
        course_comb.set(placeholder)
        sem_comb.set(placeholder)
        #==============creating fildes for student details==========
        self.id_lbl=Label(self.student_details_lblf,text="Student id",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        self.id_lbl.place(x=5,y=10)
        self.name_lbl=Label(self.student_details_lblf,text="Name",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        self.name_lbl.place(x=220,y=10)
        emailid_lbl=Label(self.student_details_lblf,text="Email id",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        emailid_lbl.place(x=5,y=60)
        phone_lbl=Label(self.student_details_lblf,text="Mobile no",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        phone_lbl.place(x=220,y=60)
        gender_lbl=Label(self.student_details_lblf,text="Gender",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        gender_lbl.place(x=5,y=110)
        address_lbl=Label(self.student_details_lblf,text="Address",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        address_lbl.place(x=220,y=110)
        password_lbl=Label(self.student_details_lblf,text="password",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        password_lbl.place(x=5,y=160)
        confirm_password_lbl=Label(self.student_details_lblf,text="confirm password",font=("times new roman",12,'bold'),bg="darkblue",fg="yellow")
        confirm_password_lbl.place(x=220,y=160)
        #=====adding entry box and all to above feilds
        self.id_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_std_id,font=("times new roman",10,'bold'))
        self.id_txt.place(x=80,y=10,width=140)
        name_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_std_name,font=("times new roman",10,'bold'))
        name_txt.place(x=340,y=10,width=140)
        emailid_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_email,font=("times new roman",10,'bold'))
        emailid_txt.place(x=80,y=60,width=140)
        emailid_txt.bind("<FocusOut>",self.validate_email_and_phone)
        phone_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_phone,font=("times new roman",12,'bold'))
        phone_txt.place(x=340,y=60,width=140)
        phone_txt.bind("<FocusOut>",self.validate_email_and_phone)
        gender_cobbox=ttk.Combobox(self.student_details_lblf,textvariable=self.var_gender,font=("times new roman",10,'bold'))
        gender_cobbox["values"]=("Male","Female","Other")
        gender_cobbox.set(placeholder)
        gender_cobbox.place(x=80,y=110,width=140)
        address_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_address,font=("times new roman",10,'bold'))
        address_txt.place(x=340,y=110,width=140)
        password_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_password,font=("times new roman",10,'bold'))
        password_txt.place(x=80,y=160,width=140)
        self.confirm_password_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_confirmpassword,show="*",font=("times new roman",10,'bold'))
        self.confirm_password_txt.place(x=340,y=160,width=140)
        password_txt.bind("<FocusOut>",self.password_validation)
        self.confirm_password_txt.bind("<FocusOut>",self.password_validation)
        #icon for eyes
        open_eye_icon = Image.open(r"images/open_eyes.png") 
        open_eye_icon=open_eye_icon.resize((20,25),Image.ANTIALIAS)
        self.open_eye_icon=ImageTk.PhotoImage(open_eye_icon)
        closed_eye_icon = Image.open(r"images/closed.png")
        closed_eye_icon=closed_eye_icon.resize((25,25),Image.ANTIALIAS)
        self.closed_eye_icon=ImageTk.PhotoImage(closed_eye_icon)
        #creating button for toggle button
        self.toggle_button = tk.Button(self.student_details_lblf, image=self.open_eye_icon, command=self.toggle_password, relief="flat", borderwidth=0)
        self.toggle_button.place(x=450,y=160,width=25,height=20)
 
        
        #====adding button take photo ,reset,save
        self.take_photoButton=Button(frame,text="Take photo sample",command=self.generate_data_set,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.take_photoButton.place(x=20,y=520,width=150)
        self.saveButton=Button(frame,text="save",command=self.submit_form,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.saveButton.place(x=180,y=520,width=150)
        self.resetButton=Button(frame,text="Reset",command=self.reset,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.resetButton.place(x=340,y=520,width=150)


    def update_fields(self):
        user_type = self.user_type.get()
        if user_type == "student":
            self.name_lbl.config(text="Student Name")
            self.id_lbl.config(text="Student id")
            self.student_details_lblf.config(text="Student Details")
            self.courselblf.place(x=5,y=90,width=490,height=150)
            self.student_details_lblf.place(x=5,y=240,width=490,height=250)
            self.take_photoButton.place(x=20,y=520,width=150)
            self.saveButton.place(x=180,y=520,width=150)
            self.resetButton.place(x=340,y=520,width=150)
        elif user_type == "admin":
            self.name_lbl.config(text="Teachar Name")
            self.id_lbl.config(text="Staff Id")
            self.student_details_lblf.config(text="Staff Details")
            self.courselblf.place_forget()
            self.student_details_lblf.place(x=5,y=160,width=490,height=250)
            self.take_photoButton.place_forget()
            self.saveButton.place(x=80,y=520,width=150)
            self.resetButton.place(x=250,y=520,width=150)
   
    #here createa database and table student and staff
    def create_student_table(self):
        placeholder="Select Option"
        if self.var_dep.get()==placeholder or self.var_course.get()==placeholder or self.var_year.get()==placeholder or self.var_semester.get()==placeholder or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()==placeholder or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_password.get()=="" or self.var_confirmpassword.get()=="":
            messagebox.showinfo("Error","All Field required",parent=self.root)
        else:
            cur.execute("insert into student values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.user_type.get(),self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_email.get(),self.var_phone.get(),self.var_gender.get(),self.var_address.get(),self.var_password.get(),self.var_confirmpassword.get()))
            con.commit() 
            messagebox.showinfo("success","student details added successful ")
            self.reset()
    def create_teacher_table(self):
        placeholder="Select Option"
        if self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()==placeholder or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_password.get()=="" or self.var_confirmpassword.get()=="":
            messagebox.showinfo("Error","All Field required",parent=self.root)
        else:
            curr.execute("insert into staff values(?,?,?,?,?,?,?,?,?)",(self.user_type.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_password.get(),self.var_confirmpassword.get()))
            conn.commit() 
            messagebox.showinfo("success","Staff details added successful ")
            self.reset()
     #============this fn for save button to save data to database===
    def submit_form(self):
        user_type = self.user_type.get()
        if user_type == "student":
            self.create_student_table()
            
        elif user_type == "admin":
            self.create_teacher_table()
            
            
        
        #==============Reset the all the  fildes===================
    def reset(self):
        placeholder="Select Option"
        self.user_type.set("")
        self.var_dep.set(placeholder)
        self.var_course.set(placeholder)
        self.var_year.set(placeholder)
        self.var_semester.set(placeholder)
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_gender.set(placeholder)
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_password.set("")
        self.var_confirmpassword.set("")
    # validation for phone and email
    def validate_email_and_phone(self, event=None):
        if self.var_email.get()!="":
            email = self.var_email.get()
            # Email validation
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_regex, email):
                if not self.email_error_shown:  # Only show the error once
                    messagebox.showerror("Error", "Invalid email format!")
                    #self.email_error_shown = True
           # else:
                #self.email_error_shown = False  # Reset the flag if email is valid
        if self.var_phone.get()!="":
            phone = self.var_phone.get()
                # Phone number validation
            phone_regex = r'^[6-9]\d{9}$'  # Assumes 10-digit phone numbers starting with 6-9
            if not re.match(phone_regex, phone):
                if not self.phone_error_shown:  # Only show the error once
                    messagebox.showerror("Error", "Invalid phone number format! Enter a valid 10-digit number.")
                   # self.phone_error_shown = True
                #else:
                    #self.phone_error_shown = False  # Reset the flag if phone is valid
    

    #=====validation for password======
    def password_validation(self,event=None):
        if self.var_password.get() != self.var_confirmpassword.get():
                messagebox.showerror("Error", "Passwords do not match!")
                return
    def toggle_password(self):
    # Toggle the visibility of the password
        if self.confirm_password_txt.cget('show') == '*':
            self.confirm_password_txt.config(show='')  # Show the password
            self.toggle_button.config(image=self.closed_eye_icon)  # Switch to closed-eye icon
        else:
            self.confirm_password_txt.config(show='*')  # Hide the password
            self.toggle_button.config(image=self.open_eye_icon)  # Switch to open-eye icon

#=======================generate data set or take photo sample===========
    def generate_data_set(self):
        try:
            cur.execute("select*from student")
            myresult=cur.fetchall()
            id=0
            for x in myresult:
                id+=1
                    #curr.execute("update student set department=?,course=?,year=?,semester=?,student_id=?,name=?,email_id=?,phone_no=?,gender=?,address=?",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get()==id+1,self.var_std_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get()))

            con.commit()
                    #========================load predifiend data face frintals from opencv====
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling facter1.3
                        #minimum neighbor5
                for(x,y,w,h)in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
            cap=cv2.VideoCapture(0)
            img_id=0
            while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==30:
                            break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data set compled!!")
        except Exception as es:
            messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)
        url = "train.py"  # replace with your HTML file name
        webbrowser.open(url, new=2)
    
#===========================================================================================

root=tk.Tk()
object=registration(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
root.mainloop()
