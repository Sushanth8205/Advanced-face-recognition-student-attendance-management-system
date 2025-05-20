from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
import cv2
import os
import numpy as np
import sqlite3
from time import strftime
from datetime import datetime
import sys

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Attendance Portal")

        # Title Label
        titel_lbl = Label(root, text="Face Recognition", font=("times", 35, 'bold'), bg='#E75480', fg='Gold')
        titel_lbl.place(x=0, y=0, width=1550, height=55)

        # Background Image
        try:
            bg_img = Image.open(r"images/face_img1.jpg")
            bg_img = bg_img.resize((785, 800), Image.Resampling.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(bg_img)
            bg_img_label = Label(self.root, image=self.photoimg_bg)
            bg_img_label.place(x=765, y=55, width=785, height=800)

            bg_img1 = Image.open(r"images/face_image2.jpg")
            bg_img1 = bg_img1.resize((765, 800), Image.Resampling.LANCZOS)
            self.photoimg_bg1 = ImageTk.PhotoImage(bg_img1)
            bg_img_label1 = Label(self.root, image=self.photoimg_bg1)
            bg_img_label1.place(x=0, y=55, width=765, height=800)
        except FileNotFoundError:
            print("Error: Background image file not found.")

        # Attendance Button
        self.loginButton = Button(bg_img_label, text="Give Attendance", command=self.face_recog,
                                  font=("times new roman", 12, "bold"), bd=4, relief=GROOVE,
                                  fg="white", bg="darkblue", activeforeground="Gold", activebackground="#E75480")
        self.loginButton.place(x=320, y=650)
    #=====================attendance==========================
    """def mark_attendance(self,student_id,name,department):
        with open("attend.csv","r+",newline="\n")as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((student_id not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%m:%S")
                f.writelines(f"\n{student_id},{name},{department},{dtString},{d1},present")"""
    

    def mark_attendance(self, student_id, name, department):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%y")  # Get today's date
        dtString = now.strftime("%H:%M:%S")  # Current time

        con = sqlite3.connect("student.db")
        cur = con.cursor()

        # Ensure table exists
        cur.execute("""CREATE TABLE IF NOT EXISTS attendence (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id VARCHAR(25),
            name VARCHAR(25),
            department VARCHAR(25),
            time TIME,
            date DATE,
            status VARCHAR(25)
        )""")

        # Check if attendance is already marked for today
        cur.execute("SELECT * FROM attendence WHERE student_id = ? AND date = ?", (str(student_id), d1))
        existing_record = cur.fetchone()

        if existing_record is None:  # Insert new attendance
            cur.execute("INSERT INTO attendence (student_id, name, department, time, date, status) VALUES (?, ?, ?, ?, ?, ?)", 
                        (str(student_id), str(name), str(department), dtString, d1, "present"))
            con.commit()
            
            messagebox.showinfo("Success", "Student details added successfully")
            con.close()
            return True  # Return True when attendance is newly marked

        else:
        # Show OK/Cancel message box
            user_response = messagebox.askokcancel("Info", "Attendance already marked for this student today.\nClick OK to exit.")
            
            if user_response:  # If "OK" is clicked
                sys.exit()  # Exit program
            
            con.close()
            return False

        

    # ==================================Face Recognition Function======================
    def face_recog(self):
        def draw_boundary(img, classifier, scalefactor, minneighbors, color, text, clf):
            if img is None:
                print("Error: No frame captured.")
                return img, False

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minneighbors)

            con = sqlite3.connect("student.db")
            cur = con.cursor()

            attendance_marked = False  # Track if attendance is recorded

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                student_id = cur.execute(f"SELECT student_id FROM student WHERE student_id={id}").fetchone()
                name = cur.execute(f"SELECT name FROM student WHERE student_id={id}").fetchone()
                department = cur.execute(f"SELECT department FROM student WHERE student_id={id}").fetchone()

                if confidence > 77:
                    cv2.putText(img, f"ID: {student_id}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    attendance_marked = self.mark_attendance(student_id, name, department)
                    print(f"Attendance Marked: {attendance_marked}")  # Debugging log

                    if attendance_marked:
                        return img, True  # Exit loop after marking attendance
                    
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img, False

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Error: No frame captured.")
                break

            img, attendance_marked = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            cv2.imshow("Welcome to Face Recognition", img)

            if attendance_marked or cv2.waitKey(1) == 13:
                print("Stopping video capture...")
                break
        if attendance_marked or cv2.waitKey(1) == 13:
            print("Stopping video capture...")
        
            
            video_cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)  # Ensure windows close properly
            
# Initialize the Tkinter Window
root = tk.Tk()
app = Attendance(root)

# Set Application Icon
try:
    image = Image.open(r"images/attendence.jpg")
    photo = ImageTk.PhotoImage(image)
    root.iconphoto(False, photo)
except FileNotFoundError:
    print("Error: Icon file not found.")
except Exception as e:
    print(f"Error loading icon: {e}")

root.mainloop()