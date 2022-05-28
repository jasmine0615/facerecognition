from asyncore import write
from importlib.metadata import entry_points
from importlib.resources import path
from ntpath import join
import os
from socket import timeout
from time import time
from datetime import date
from datetime import datetime
from winsound import PlaySound
from dateutil import relativedelta
from tkinter import*
from time import strftime
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
import os
import pyttsx3
import numpy as np
from gtts import gTTS


class face_Rec:
    def __init__(self, portal):
        self.portal = portal
        self.portal.geometry("1530x790+0+0")
        self.portal.title("Face Recognition System")
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        lbl_title = Label(self.portal, text="FACE RECOGNITION", font=(
            "times new roman", 37, "bold"), fg="blue", bg="pink")
        lbl_title.place(x=0, y=-10, width=1530, height=50)
    # setting up background images
        img = Image.open(
            r"C:\Users\jasmine p\Desktop\finalproj\ai.jpg")
        img = img.resize((1530, 710), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img)
        bg_lbl = Label(self.portal, image=self.photo1,  relief=RIDGE)
        bg_lbl.place(x=-10, y=50, width=1590, height=730)

        b1 = Button(self.portal, command=self.face_reco, text="Start Face recognition",  font=(
            "times new roman", 45, "bold"), cursor="hand2", fg="white", bg="black")
        b1.place(x=180, y=380, width=1230, height=60)
# function for storing attendance

    def attendance(self, i, n, d, g):
        # here i=employee id, n=employee name,d=employee designation, g=gender
        outfile = open("attendance.csv", "a", newline="\n")
        write_outfile = csv.writer(outfile)
        with open("attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            name_list = []

            for line in dataList:
                entry = line.split((","))

                if len(entry) >= 6 and entry[0] == i:
                    # this condition is used to update the day wise presentees
                    name_list.append(entry[5])

        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")  # date
        tm = now.strftime("%H:%M:%S")  # time at which face has been recognsied
        if((d1 not in name_list)):
            data = [i, n, d, g, tm, d1, "Present"]
            write_outfile.writerow(data)

# code for initialising face recognition
    def face_reco(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, classif):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = classif.predict(gray_image[y:y+h, x:x+w])
                # formula for confidence level
                confidence = (100*(1-predict/300))
                # obtaining the employeedata from database
                conn = mysql.connector.connect(
                    host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "Select employeename from employee where employeeid="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                my_cursor.execute(
                    "Select emp_designation from employee where employeeid="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                my_cursor.execute(
                    "Select employeeid from employee where employeeid="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                my_cursor.execute(
                    "Select emp_gender from employee where employeeid="+str(id))
                g = my_cursor.fetchone()
                g = "+".join(g)
                if confidence > 77:
                    # displaying id's around the rectangle for the recognised tables
                    cv2.putText(
                        img, f"Name:{n}", (x, 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Designation:{d}", (x, 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Id:{i}", (x, 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.attendance(i, n, d, g)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Face cannot be detected", (x, y),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, y]

            return coord

        def recognize(img, classif, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", classif)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                            "haarcascade_frontalface_default.xml")
        # using Local Binary Pattern Histogram
        classif = cv2.face.LBPHFaceRecognizer_create()
        classif.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, classif, faceCascade)
            cv2.imshow("Webcam access!", img)

            if cv2.waitKey(1) == 13:

                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    portal = Tk()
    obj = face_Rec(portal)
    portal.mainloop()
