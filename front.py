from cProfile import label
from email.mime import image
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
from employee import employee
from datatrain import dTrain
from attendance import attend
from face import face_Rec
import mysql.connector

# main page which appears after login runs with the help
# of the following code


class Front:
    def __init__(self, portal):
        self.portal = portal
        self.portal.geometry("1530x790+0+0")
        self.portal.title("WELCOME...!")
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\jasmine p\Desktop\finalproj\frn.jpg")
        lbl_bg = Label(self.portal, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        img = Image.open(r"C:\Users\jasmine p\Desktop\finalproj\dl.jpg")
        img = img.resize((1530, 250), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        img_lbl = Label(self.portal, image=self.photoimg)
        img_lbl.place(x=0, y=0, width=1530, height=250)
        # employee portal button which opens the employee page
        b1 = Button(self.portal, text="Employee details.", command=self.emp_deets,  font=(
            "times new roman", 25, "bold"), cursor="hand2", fg="white", bg="black")
        b1.place(x=410, y=380, width=700, height=50)
        # data training page is shown upon clicking this button
        b2 = Button(self.portal, text="Train your data.", command=self.Train,  font=(
            "times new roman", 25, "bold"), cursor="hand2", fg="white", bg="black")
        b2.place(x=410, y=470, width=700, height=50)
        # run the face recognition algorithm using the following button
        b3 = Button(self.portal, text="Face Recognition.", command=self.facrec,  font=(
            "times new roman", 25, "bold"), cursor="hand2", fg="white", bg="black")
        b3.place(x=410, y=570, width=700, height=50)
        # admin can check/track employee attendance when clicked here
        b4 = Button(self.portal, text="Employee attendance management", command=self.attendrec,  font=(
            "times new roman", 25, "bold"), cursor="hand2", fg="white", bg="black")
        b4.place(x=410, y=670, width=700, height=50)
        b5 = Button(self.portal, text="Logout", command=self.exit, font=(
            "times new roman", 18, "bold"), cursor="hand2", fg="black", bg="white")
        b5.place(x=1360, y=250, width=170, height=30)

        # functions
    def emp_deets(self):
        self.new_window = Toplevel(self.portal)
        self.app = employee(self.new_window)

    def Train(self):
        self.new_window = Toplevel(self.portal)
        self.app = dTrain(self.new_window)

    def facrec(self):
        self.new_window = Toplevel(self.portal)
        self.app = face_Rec(self.new_window)

    def attendrec(self):
        self.new_window = Toplevel(self.portal)
        self.app = attend(self.new_window)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno(
            "proj", "Do you want to exit?", parent=self.portal)
        if self.exit > 0:
            self.portal.destroy()
        else:
            return


if __name__ == "__main__":
    portal = Tk()
    obj = Front(portal)
    portal.mainloop()
