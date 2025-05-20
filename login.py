from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import sqlite3
con = sqlite3.connect("student.db")
cur=con.cursor()
td = cur.execute("select * from sqlite_master where type='table' and name = 'student'").fetchall()
conn = sqlite3.connect("student.db")
curr=conn.cursor()
tdd = curr.execute("select * from sqlite_master where type='table' and name = 'staff'").fetchall()
class login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("login page")
        self.bg=ImageTk.PhotoImage(file=r"images/bg_login.jpg")
        lal_bg=Label(self.root,image=self.bg)
        lal_bg.place(x=0,y=0,relwidth=1,relheight=1)
         #====craeting variables for usserid and password
        self.var_user_id=StringVar()
        self.var_password=StringVar()
        #creating inner frame 
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=500)

        img1=Image.open(r"images/login.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lal_bg=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lal_bg.place(x=730,y=175,width=100,height=100)
       
        

        self.loginlbl=Label(frame,text="Login",font=("time",20,"bold"),fg="white",bg="black")
        self.loginlbl.place(x=130,y=100)
        # label and text box user name 
        self.userid=lbl=Label(frame,text="USER ID",font=("times new roman",15,"bold"),fg="white",bg="black")
        self.userid.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",12,"bold"),textvariable= self.var_user_id)
        self.txtuser.place(x=40,y=200,width=250)
        # label andf text box for 
        self.password=lbl=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="black")
        self.password.place(x=40,y=250)

        self.txtpassword=ttk.Entry(frame,font=("time",12,"bold"),show="*",textvariable=self.var_password)
        self.txtpassword.place(x=40,y=300,width=250)
        #icon for eyes
        open_eye_icon = Image.open(r"images/open_eyes.png") 
        open_eye_icon=open_eye_icon.resize((20,25),Image.ANTIALIAS)
        self.open_eye_icon=ImageTk.PhotoImage(open_eye_icon)
        closed_eye_icon = Image.open(r"images/closed.png")
        closed_eye_icon=closed_eye_icon.resize((20,25),Image.ANTIALIAS)
        self.closed_eye_icon=ImageTk.PhotoImage(closed_eye_icon)
        #creating button for toggle button
        self.toggle_button = tk.Button(frame, image=self.open_eye_icon, command=self.toggle_password, relief="flat", borderwidth=0)
        self.toggle_button.place(x=280,y=300,width=25,height=25)
 
        #====icon for password and login
        img2=Image.open(r"images/login.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lal_icon1=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lal_icon1.place(x=620,y=323,width=25,height=25)
        

            #password
        img3=Image.open(r"images/password_ico.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lal_icon2=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lal_icon2.place(x=620,y=420,width=25,height=25)
        
        #login button
        self.loginButton=Button(frame,text="Login",command=self.login,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="white",bg="darkblue",activeforeground="white",activebackground="gray")
        self.loginButton.place(x=140,y=350)
        #Register button
        self.registerButton=Button(frame,text="New User Register",command=self.registration,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        self.registerButton.place(x=10,y=400,width=160)
        #forgetbutton
        self.forgetButton=Button(frame,text="forget password",command=self.update_fields,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        self.forgetButton.place(x=10,y=420,width=160)
  
    def login(self):
    # Fetch the student ID and password from the database
        userid = cur.execute("select student_id from student where student_id=?", (self.var_user_id.get(),)).fetchone()
        passwordid = cur.execute("select password from student where student_id=?", (self.var_user_id.get(),)).fetchone()  # Use student_id to find the matching password
        userid1 = curr.execute("select staff_id from staff where staff_id=?", (self.var_user_id.get(),)).fetchone()
        passwordid1 = curr.execute("select password from staff where staff_id=?", (self.var_user_id.get(),)).fetchone()
    
    # Debugging print statements to see the fetched values
        print(userid, passwordid)
        
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif userid1 and passwordid1 and self.txtuser.get() == str(userid1[0]) and self.txtpassword.get() == str(passwordid1[0]):
            messagebox.showinfo("Success", "Login successful")
            self.details()
        elif userid and passwordid and self.txtuser.get() == str(userid[0]) and self.txtpassword.get() == str(passwordid[0]):
            messagebox.showinfo("Success", "Login successful")
            url = "present.py"  # replace with your HTML file name
            webbrowser.open(url, new=2) 

            
        else:
            messagebox.showerror("Invalid", "Invalid User name and Password")
        
        # Commit changes to the database
        con.commit()
            
    def registration(self):
        url= "registration_admin.py"  # replace with your HTML file name
        webbrowser.open(url, new=2) 
#==========================================================================
    def toggle_password(self):
    # Toggle the visibility of the password
        if self.txtpassword.cget('show') == '*':
            self.txtpassword.config(show='')  # Show the password
            self.toggle_button.config(image=self.closed_eye_icon)  # Switch to closed-eye icon
        else:
            self.txtpassword.config(show='*')  # Hide the password
            self.toggle_button.config(image=self.open_eye_icon)  # Switch to open-eye icon
    def update_fields(self):
        self.userid.config(text="User id")
        self.password.config(text="New password")
        self.loginlbl.config(text="Forget password",font=("times new roman",11,"bold"))
        self.loginButton.place_configure(x=140,y=420)
        self.loginButton.config(text="save")
        self.registerButton.place_forget()
        self.forgetButton.place_forget()
        #self.loginButton.config(command=update_table)
        def update_table():
                cur.execute("UPDATE student SET password=? WHERE student_id= ?", (self.txtpassword.get(),self.txtuser.get()))
                cur.execute("UPDATE student SET  confirm_password=? WHERE student_id= ?", (self.txtpassword.get(),self.txtuser.get()))
                con.commit() 
                messagebox.showinfo("success","student password updated successful ")
                print(self.txtpassword.get())
                self.password.config(text="password")
                self.loginlbl.config(text="Login",font=("time",20,"bold"))
                self.loginButton.place_configure(x=140,y=350)
                self.registerButton.place_configure(x=10,y=400,width=160)
                self.forgetButton.place_configure(x=10,y=420,width=160)
                self.loginButton.config(text="login")
                self.loginButton.config(command=self.login)
        self.loginButton.config(command=update_table)
    def details(self):
        url = "details.py"  # replace with your HTML file name
        webbrowser.open(url, new=2) 





root=tk.Tk()
object=login_page(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
  
root.mainloop()
       