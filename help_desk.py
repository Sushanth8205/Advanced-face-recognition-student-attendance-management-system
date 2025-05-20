from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import py_compile
class help_desk:
    def __init__(self,root):
        # background
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("Attendance System ")
        bg_img=Image.open(r"images/bg_helpdisk.jpg")
        bg_img=bg_img.resize((1530,1530),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=0,width=1530,height=1530)
        #label
         
        titel_lbl=Label(bg_img,text="sushanthpoojary8205@gmail.com",font=("times",35,'bold'),fg="red")
        titel_lbl.place(x=0,y=250,width=1530,height=55)
        titel_lbl1=Label(bg_img,text="poojarygoutham7@gmail.com",font=("times",35,'bold'),fg="red")
        titel_lbl1.place(x=0,y=320,width=1530,height=55)
root=tk.Tk()
object=help_desk(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
root.mainloop()
