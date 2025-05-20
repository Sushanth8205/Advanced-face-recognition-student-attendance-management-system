from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import py_compile
import sqlite3
import re
con = sqlite3.connect("student.db")
cur=con.cursor()
td = cur.execute("select * from sqlite_master where type='table' and name = 'student'").fetchall()
if td==[]:
    cur.execute("create table student(user_type varchr2,department varchr2,course varchr2,year varchr2,semester varchr2,student_id varchr2 primary key,name varchr2,email_id varchr2,phone_no number,gender varchr2,address varchr2,password varchar2,confirm_password varchr2)")
#creating staff table
conn = sqlite3.connect("student.db")
curr=conn.cursor()
tdd = curr.execute("select * from sqlite_master where type='table' and name = 'staff'").fetchall()
if tdd==[]:
    curr.execute("create table staff(user_type varchr2,student_id varchr2 primarykey,name varchr2,email_id varchr2,phone_no number,gender varchr2,address varchr2,password varchar2,confirm_password varchr2)")

class details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Attendance portel")
        titel_lbl=Label(root,text="Student details ",font=("times",35,'bold'),bg='Dark Magenta',fg='Gold')#e75480 is color dark pink
        titel_lbl.place(x=0,y=0,width=1550,height=55)
        bg_img=Image.open(r"images\mainpage_details.jpg")
        bg_img=bg_img.resize((1550,800),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.photoimg_bg)

        bg_img.place(x=0,y=55,width=1550,height=800)
        #===================creating text variables
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
        #====================frame 2================================
        frame=Frame(self.root,bg="darkblue")
        frame.place(x=5,y=60,width=1600,height=720)
        #====================framr1 ====================================
        frame1=LabelFrame(self.root,bg="darkblue",text="student details",font=("times new roman",14,'bold'),fg="yellow")
        frame1.place(x=5,y=60,width=550,height=720)
        self.frame2=LabelFrame(self.root,bg="darkblue",text="student details",font=("times new roman",14,'bold'),fg="yellow")
        self.frame2.place(x=600,y=60,width=900,height=720)
        
        radio_labf=LabelFrame(frame1,text="select Admin or student",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
        radio_labf.place(x=5,y=5,width=490,height=80)
        #creatin style to radio button using style class of ttk
        style=ttk.Style()
        style.configure("TRadiobutton",font=("times new roman",12,'bold'))
        style.configure("TRadiobutton",background="darkblue",foreground="yellow")
        #radio button
        student_radiobtn=ttk.Radiobutton(radio_labf, text="student", value="student",variable=self.user_type,command=self.update_fields)
        student_radiobtn.place(x=5,y=2)
        #admin_radiobtn=ttk.Radiobutton(radio_labf, text="admin", value="admin",variable=self.user_type,command=self.update_fields)
        #admin_radiobtn.place(x=100,y=2)
        #Course details lable frame
        self.courselblf=LabelFrame(frame1,text="Course Details",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
        self.courselblf.place(x=5,y=90,width=490,height=150)
        #student details
        self.student_details_lblf=LabelFrame(frame1,text="Student Details",font=("times new roman",14,'bold'),bg="darkblue",fg="yellow")
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
        self.id_txt=Label(self.student_details_lblf,textvariable=self.var_std_id,font=("times new roman",10,'bold'))
        self.id_txt.place(x=80,y=10,width=140)
        name_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_std_name,font=("times new roman",10,'bold'))
        name_txt.place(x=340,y=10,width=140)
        emailid_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_email,font=("times new roman",10,'bold'))
        emailid_txt.place(x=80,y=60,width=140)
        phone_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_phone,font=("times new roman",12,'bold'))
        phone_txt.place(x=340,y=60,width=140)
        gender_cobbox=ttk.Combobox(self.student_details_lblf,textvariable=self.var_gender,font=("times new roman",10,'bold'))
        gender_cobbox["values"]=("Male","Female","Other")
        gender_cobbox.set(placeholder)
        gender_cobbox.place(x=80,y=110,width=140)
        address_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_address,font=("times new roman",10,'bold'))
        address_txt.place(x=340,y=110,width=140)
        self.password_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_password,font=("times new roman",10,'bold'))
        self.password_txt.place(x=80,y=160,width=140)
        self.confirm_password_txt=ttk.Entry(self.student_details_lblf,textvariable=self.var_confirmpassword,show="*",font=("times new roman",10,'bold'))
        self.confirm_password_txt.place(x=340,y=160,width=140)
        self.password_txt.bind("<FocusOut>",self.password_validation)
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
        updateButton=Button(frame1,text="update",command=self.update_student_table,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        updateButton.place(x=20,y=520,width=150)
        deleteButton=Button(frame1,text="delete",command=self.delete_data,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        deleteButton.place(x=180,y=520,width=150)
        resetButton=Button(frame1,text="Reset",command=self.reset,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        resetButton.place(x=340,y=520,width=150)
        #==============================================================
        bg_img1=Image.open(r"images\student studying.jpg")
        bg_img1=bg_img1.resize((870,130),Image.ANTIALIAS)
        self.photoimg_bg1=ImageTk.PhotoImage(bg_img1)
        bg_img1=Label(self.frame2,image=self.photoimg_bg1)
        bg_img1.place(x=5,y=0,width=870,height=130)
        self.searchlblf=LabelFrame(self.frame2,text="search Details",font=("times new roman",14,'bold'),bg="darkblue",fg="white")
        self.searchlblf.place(x=5,y=135,width=870,height=70)
        """searchby_lbl=Label(self.searchlblf,text="search by",font=("times new roman",12,'bold'),bg="red",fg="yellow")
        searchby_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        searchby_comb=ttk.Combobox(self.searchlblf,state="readonly",font=("times new roman",10,'bold'))        
        searchby_comb["values"]=("Id","Name")
        searchby_comb.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        searchby_comb.set("select")
        searchentry=ttk.Entry(self.searchlblf,font=("times new roman",12,'bold'))
        searchentry.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        self.searchbutton = tk.Button(self.searchlblf,  text="search",font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.searchbutton.grid(row=0,column=3,padx=4)"""
        """self.show_all_button = tk.Button(self.searchlblf,  text="show all",font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.show_all_button.grid(row=0,column=4,padx=4)"""
        #self.detailsbutton = tk.Button(self.searchlblf, command=self.student_details, text="student details",font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        #self.detailsbutton.grid(row=0,column=4,padx=4)
        self.attendencebutton = tk.Button(self.searchlblf, command=self.attendence_details, text="student attendence",font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="black",bg="yellow",activeforeground="white",activebackground="gray")
        self.attendencebutton.grid(row=0,column=5,padx=4)

        #========================table frame=============================
        tableframe=Frame(self.frame2,bd=2,bg="darkblue",relief=RIDGE)
        tableframe.place(x=5,y=210,width=870,height=480)

        Scrollbar_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.student_table=ttk.Treeview(tableframe,columns=("dep","course","year","sem","id","name","gender","email","phone","address","password"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="student id")
        self.student_table.heading("name",text="student name")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("email",text="email")
        self.student_table.heading("phone",text="phone no")
        self.student_table.heading("address",text="address")
        self.student_table.heading("password",text="password")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("password",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cur)
        self.fetch_data()
        


        #=====================================================================
    def update_fields(self):
        user_type = self.user_type.get()
        if user_type == "student":
            self.name_lbl.config(text="Student Name")
            self.id_lbl.config(text="Student id")
            self.student_details_lblf.config(text="Student Details")
            self.courselblf.place(x=5,y=90,width=490,height=150)
            self.student_details_lblf.place(x=5,y=240,width=490,height=250)
        elif user_type == "admin":
            self.name_lbl.config(text="Teachar Name")
            self.id_lbl.config(text="Staff Id")
            self.student_details_lblf.config(text="Staff Details")
            self.courselblf.place_forget()
            self.student_details_lblf.place(x=5,y=160,width=490,height=250)
   
    #here createa database and table student and staff
    def fetch_data(self):
        cur.execute("select department,course,year,semester,student_id, name,gender,email_id,phone_no,address,password from student")
        data=cur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            con.commit()
    #=======================================================
    def get_cur(self,event=""):
        cur_focuse=self.student_table.focus()
        content=self.student_table.item(cur_focuse)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_address.set(data[9]),
        self.var_password.set(data[10]),


                  
    def update_student_table(self):
        placeholder="Select Option"
        if self.var_dep.get()==placeholder or self.var_course.get()==placeholder or self.var_year.get()==placeholder or self.var_semester.get()==placeholder or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_gender.get()==placeholder or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_password.get()=="" or self.var_confirmpassword.get()=="":
            messagebox.showinfo("Error","All Field required",parent=self.root)
        else:
            cur.execute("UPDATE student SET department=?,course=?,year=?,semester=?,name=?,gender=?,email_id=?,phone_no=?,address=?,password=?,confirm_password=? where student_id=?",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_password.get(),self.var_confirmpassword.get(),self.var_std_id.get()))
            con.commit() 
            messagebox.showinfo("success","student details updateed successful ")
            self.fetch_data()
            self.reset()
    #=======================delete _data===========================
    def delete_data(self):
        placeholder="Select Option"
        if self.var_std_id.get()=="":
            messagebox.showinfo("Error","student id must be  required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student Delete page","D0 you want to delete this student",parent=self.root)
                if delete>0:
                    sql="delete from student where student_id=?"
                    val=(self.var_std_id.get(),)
                    cur.execute(sql,val)
                    con.commit() 
                    messagebox.showinfo("success","student details deleteed successful")
                    self.fetch_data()
                    self.reset()
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
     #============this fn for save button to save data to database===
    """def submit_form(self):
        user_type = self.user_type.get()
        if user_type == "student":
            self.create_student_table()
            
        elif user_type == "admin":
            self.create_teacher_table()"""
            
            
        
        #==============Reset the all the  fildes===================
    def reset(self):
        placeholder="Select Option"
        #self.user_type.set("")
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
    def attendence_details(self):
        url = "present.py"  # replace with your HTML file name
        webbrowser.open(url, new=2)


        
    
root=tk.Tk()
object=details(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
root.mainloop()