from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import py_compile
import sys
from time import strftime



class attendance_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Attendance System ")
        img=Image.open(r"images\image1.jpg")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        a_lal=Label(self.root,image=self.photoimg)
        a_lal.place(x=0,y=0,width=1530,height=130)
        # bg image
        bg_img=Image.open(r"images\bg imag1.jpg")
        bg_img=bg_img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=130,width=1530,height=710)
        #title
        titel_lbl=Label(bg_img,text="Attendance of portal",font=("times",35,'bold'),bg='red',fg='yellow')
        titel_lbl.place(x=0,y=0,width=1530,height=65)
        self.time_label = tk.Label(bg_img, font=("Arial", 40), bg="red", fg="yellow")
        self.time_label.place(x=50,y=0)

        self.update_time()
        #creating buttons for attendence
        
        img2=Image.open(r"images\attendance img.jpg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(bg_img,image=self.photoimg2,cursor="hand2",command=attendance)
        b1.place(x=150,y=220,width=220,height=220)

        b1_lb1=Button(bg_img,text="Attendance",command=attendance,font=("times",15,'bold'),bg='blue',fg='white',cursor="hand1")
        b1_lb1.place(x=150,y=410,width=220,height=35)
        #creating button for login
        img3=Image.open(r"images\login img.jpg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b2=Button(bg_img,image=self.photoimg3,cursor="hand2",command=login_page)
        b2.place(x=650,y=220,width=220,height=220)

        b2_lb1=Button(bg_img,text="Login",font=("times",15,'bold'),bg='blue',fg='white',cursor="hand1", command=login_page)
        b2_lb1.place(x=650,y=410,width=220,height=35)
        #creating button for help desk
        img4=Image.open(r"images\help disk img.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b3=Button(bg_img,image=self.photoimg4,cursor="hand2",command=help_desk)
        b3.place(x=1150,y=220,width=220,height=220)

        b3_lb1=Button(bg_img,text="Help Desk",font=("times",15,'bold'),bg='blue',fg='white',cursor="hand1",command=help_desk)
        b3_lb1.place(x=1150,y=410,width=220,height=35)
    def update_time(self):
        current_time = strftime("%H:%M:%S")  # Get current time
        self.time_label.config(text=current_time)  # Update label text
        self.time_label.after(1000,self. update_time)  # Schedule update after 1 second



    


def login_page():
    url = "login.py"  # replace with your HTML file name
    webbrowser.open(url, new=2)  # open in new tab
def help_desk():
    url = "help_desk.py"  # replace with your HTML file name
    webbrowser.open(url, new=2)  # open in new tab
"""def login_page(self):
        self.new_window=Toplevel(self.root)
        self.app=login_page(self.new_window)"""
def attendance():
    url = "attendance.py"  # replace with your HTML file name
    webbrowser.open(url, new=2)
    
    
    
root=tk.Tk()
object=attendance_system(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
root.mainloop()

