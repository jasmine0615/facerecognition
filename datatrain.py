from importlib.resources import path
import os
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

# training the data set i.e; images obtained


class dTrain:
    def __init__(self, portal):
        self.portal = portal
        self.portal.geometry("1530x790+0+0")
        self.portal.title("Data training System")
        # background image
        img = Image.open(
            r"images\bg1.jpg")
        img = img.resize((1530, 710), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img)
        bg_lbl = Label(self.portal, image=self.photo1,  relief=RIDGE)
        bg_lbl.place(x=-10, y=50, width=1590, height=730)

        b1 = Button(self.portal, text="TRAIN DATASET", command=self.train, font=(
            "times new roman", 45, "bold"), cursor="hand2", fg="white", bg="black")
        b1.place(x=180, y=380, width=1230, height=60)

        lbl_title = Label(self.portal, text="Data  Set Training", font=(
            "times new roman", 37, "bold"), fg="blue", bg="pink")
        lbl_title.place(x=0, y=-10, width=1530, height=50)

    def train(self):
        # path of the directory where images have been stored
        data_dir = ("data")
        path = [os.path.join(data_dir, file)for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            # conversion of images to grayscale
            img1 = Image.open(image).convert('L')
            imageNp = np.array(img1, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        classif = cv2.face.LBPHFaceRecognizer_create()  # using the LBPH algorithm
        classif.train(faces, ids)
        # writing the data in the form of xml file after training
        classif.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training DataSets Completed...!")


if __name__ == "__main__":
    portal = Tk()
    obj = dTrain(portal)
    portal.mainloop()
