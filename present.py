from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import py_compile
import sqlite3
import re
class present:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Attendance portel")
        titel_lbl=Label(root,text="Attendens details ",font=("times",35,'bold'),bg='Dark Magenta',fg='Gold')#e75480 is color dark pink
        titel_lbl.place(x=0,y=0,width=1550,height=55)
        bg_img=Image.open(r"images\mainpage_details.jpg")
        bg_img=bg_img.resize((1550,800),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bg_img)
        bg_img=Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=55,width=1550,height=800)
       
        frame=LabelFrame(self.root,bd=2,bg="darkblue",text="student details",font=("times new roman",14,'bold'),fg="yellow")
        frame.place(x=5,y=60,width=1510,height=720)
        self.var_dep=StringVar()
        self.student_id=StringVar()
        self.name=StringVar()
        self.date=StringVar()
        self.time=StringVar()
        self.status=StringVar()
        

         #===============================================
        bg_img1=Image.open(r"images\present.jpg")
        bg_img1=bg_img1.resize((1500,130),Image.ANTIALIAS)
        self.photoimg_bg1=ImageTk.PhotoImage(bg_img1)
        bg_img1=Label(frame,image=self.photoimg_bg1)
        bg_img1.place(x=5,y=0,width=1500,height=130)
        #=====================================================
        tableframe=Frame(frame,bd=2,bg="darkblue",relief=RIDGE)
        tableframe.place(x=5,y=130,width=1500,height=550)

        Scrollbar_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.student_table=ttk.Treeview(tableframe,columns=("id","name","dep","time","date","status"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        Scrollbar_x.config(command=self.student_table.xview)
        Scrollbar_y.config(command=self.student_table.yview)
        self.student_table.heading("id",text="student id")
        self.student_table.heading("name",text="student name")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("time",text="time")
        self.student_table.heading("date",text="date")
        self.student_table.heading("status",text="status")
        self.student_table["show"]="headings"
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("time")
        self.student_table.column("date")
        self.student_table.column("status")
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cur)
        self.fetch_data()
    def fetch_data(self):
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        cur.execute("select student_id,name,department,time,date,status from attendence")
        data=cur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            con.commit()
    def get_cur(self,event=""):
        cur_focuse=self.student_table.focus()
        content=self.student_table.item(cur_focuse)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.student_id.set(data[1]),
        self.name.set(data[2]),
        self.date.set(data[3]),
        self.time.set(data[4]),
        self.status.set(data[5]),
        
        


root=tk.Tk()
object=present(root)
try:
    image = Image.open(r"images\attendence.jpg")  # Replace with your JPG path
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo) 
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")
root.mainloop()