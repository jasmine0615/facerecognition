from ast import Delete
from cgitb import text
from email import message
from lib2to3.pgen2.token import SLASHEQUAL
from logging import exception
from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from turtle import update, width
from winsound import MessageBeep
from PIL import Image, ImageTk
import mysql.connector
import cv2
from tkinter import messagebox


class employee:
    def __init__(self, portal):
        self.portal = portal
        self.portal.geometry("1530x790+0+0")
        self.portal.title("Employee Portal")

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_phn = StringVar()
        self.var_email = StringVar()
        self.var_des = StringVar()
        self.var_gender = StringVar()
        self.var_add = StringVar()
        self.var_bday = StringVar()
        self.var_salary = StringVar()
        # backgroundimage

        img = Image.open(
            r"facerecognition/images/backg.jpg")
        img = img.resize((1530, 710), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img)
        bg_lbl = Label(self.portal, image=self.photo1, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=100, width=1530, height=710)

        lbl_title = Label(self.portal, text="Welcome to the Employee Dashboard", font=(
            "times new roman", 37, "bold"), fg="blue", bg="pink")
        lbl_title.place(x=0, y=-10, width=1530, height=50)

        # main frame of the window
        main_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=15, y=55, width=1500, height=560)

        # left frame to show employee information which consists of basic data
        # such as employeename,id,salary,etc..
        lFrame = LabelFrame(main_frame, bd=4, relief=RIDGE, padx=2, text="Employee information", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        lFrame.place(x=10, y=10, width=660, height=540)

        basic_dat = LabelFrame(lFrame, bd=4, relief=RIDGE, padx=2,
                               text="Basic Details", font=("arial", 12, "bold"), bg="white")
        basic_dat.place(x=0, y=10, width=650, height=750)

        emp_name = Label(basic_dat, font=("arial", 12, "bold"),
                         text="Employee Name:", bg="white")
        emp_name.grid(row=0, column=0, sticky=W, padx=2, pady=7)
        emp_name_entry = ttk.Entry(basic_dat, textvariable=self.var_name, font=(
            "arial", 12, "bold"), width=22)
        emp_name_entry.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        lbl_id = Label(basic_dat, font=("arial", 12, "bold"),
                       text="Employee ID:", bg="white")
        lbl_id.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        id_entry = ttk.Entry(basic_dat, textvariable=self.var_id, font=(
            "arial", 12, "bold"), width=22)
        id_entry.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        emp_no = Label(basic_dat, font=("arial", 12, "bold"),
                       text="Phone number:", bg="white")
        emp_no.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        emp_no_entry = ttk.Entry(basic_dat, textvariable=self.var_phn, font=(
            "arial", 12, "bold"), width=22)
        emp_no_entry.grid(row=5, column=0, sticky=W, padx=2, pady=7)

        emp_email = Label(basic_dat, font=("arial", 12, "bold"),
                          text="Email:", bg="white")
        emp_email.grid(row=6, column=0, sticky=W, padx=2, pady=7)
        emp_email_entry = ttk.Entry(basic_dat, textvariable=self.var_email, font=(
            "arial", 12, "bold"), width=22)
        emp_email_entry.grid(row=7, column=0, sticky=W, padx=2, pady=7)
        emp_gender = Label(basic_dat, font=("arial", 12, "bold"),
                           text="Gender:", bg="white")
        emp_gender.grid(row=8, column=0, sticky=W, padx=2, pady=7)
        com_txt_gender = ttk.Combobox(basic_dat, textvariable=self.var_gender, state="readonly", font=(
            "arial", 12, "bold"), width=22)
        com_txt_gender['value'] = ("Male", "Female", "Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=9, column=0, sticky=W, padx=2, pady=7)
        emp_dob = Label(basic_dat, font=("arial", 12, "bold"),
                        text="DOB:", bg="white")
        emp_dob.grid(row=10, column=0, sticky=W, padx=2, pady=7)
        emp_dob_entry = ttk.Entry(basic_dat, textvariable=self.var_bday, font=(
            "arial", 12, "bold"), width=22)
        emp_dob_entry.grid(row=11, column=0, sticky=W, padx=2, pady=7)
        emp_sal = Label(basic_dat, font=("arial", 12, "bold"),
                        text="Salary CTC:", bg="white")
        emp_sal.grid(row=0, column=1, sticky=W, padx=2, pady=7)
        emp_sal_entry = ttk.Entry(basic_dat, textvariable=self.var_salary, font=(
            "arial", 12, "bold"), width=22)
        emp_sal_entry.grid(row=1, column=1, sticky=W, padx=2, pady=7)
        emp_des = Label(basic_dat, font=("arial", 12, "bold"),
                        text="Designation:", bg="white")
        emp_des.grid(row=2, column=1, sticky=W, padx=2, pady=7)
        emp_des_entry = ttk.Entry(basic_dat, textvariable=self.var_des, font=(
            "arial", 12, "bold"), width=22)
        emp_des_entry.grid(row=3, column=1, sticky=W, padx=2, pady=7)
        emp_add = Label(basic_dat, font=("arial", 12, "bold"),
                        text="Address:", bg="white")
        emp_add.grid(row=4, column=1, sticky=W, padx=2, pady=7)
        emp_add_entry = ttk.Entry(basic_dat, textvariable=self.var_add, font=(
            "arial", 12, "bold"), width=22)
        emp_add_entry.grid(row=5, column=1, sticky=W, padx=2, pady=7)

        # button frame
        # update,reset,save,delete and take photo buttons have been added
        bn_frame = Frame(lFrame, bd=2, relief=RIDGE, bg="white")
        bn_frame.place(x=340, y=280, width=300, height=230)
        # new employee information can be added here
        btn_add = Button(bn_frame, command=self.add_data, text="Save", font=(
            "arial", 13, "bold"), width=30, bg="blue", fg="white")
        btn_add.grid(row=1, column=1, padx=0, pady=5)
        # update button will be used to update a certain value if necesary
        btn_up = Button(bn_frame, command=self.update, text="Update", font=(
            "arial", 13, "bold"), width=30, bg="blue", fg="white")
        btn_up.grid(row=2, column=1, padx=1, pady=5)
        # delete button to delete a certain employee data
        btn_del = Button(bn_frame, command=self.delete_data, text="Delete", font=(
            "arial", 13, "bold"), width=30, bg="blue", fg="white")
        btn_del.grid(row=3, column=1, padx=1, pady=5)

        btn_res = Button(bn_frame, command=self.reset, text="Reset", font=(
            "arial", 13, "bold"), width=30, bg="blue", fg="white")
        btn_res.grid(row=4, column=1, padx=1, pady=5)
        # each employee photo will be taken at the beginning so that data training is done
        take_photo_btn = Button(bn_frame, command=self.gen_data, text="Take Photo", font=(
            "arial", 13, "bold"), width=30, height=2, bg="blue", fg="white")
        take_photo_btn.grid(row=5, column=1, padx=1, pady=5)

        # right frame
        # this frame shows the total employee data in that particular company
        rFrame = LabelFrame(main_frame, bd=4, relief=RIDGE, padx=2, text="Employee Details", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        rFrame.place(x=680, y=10, width=800, height=540)

        searchF = LabelFrame(rFrame, bd=4, relief=RIDGE, padx=2, text="Search employee information", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        searchF.place(x=0, y=10, width=790, height=490)

        search1 = Label(searchF, font=("arial", 12, "bold"),
                        text="Search By:", fg="white", bg="blue")
        search1.grid(row=0, column=0, sticky=W, padx=5)
        # search.. Here you can search the employee on the basis of his id or any parameter
        self.var_search = StringVar()
        com_txt_search = ttk.Combobox(searchF, textvariable=self.var_search, state="readonly", font=(
            "arial", 12, "bold"), width=22)
        com_txt_search['value'] = (
            "Select option", "EmployeeId")
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search1 = StringVar()

        txt_search = ttk.Entry(
            searchF, textvariable=self.var_search1, width=22, font=("arial", 11, "bold"))
        txt_search.grid(row=0, column=2, padx=5)

        btn_sear = Button(searchF, command=self.search, text="Search", font=(
            "arial", 13, "bold"), width=10, bg="blue", fg="white")
        btn_sear.grid(row=0, column=3, padx=5)

        btn_show = Button(searchF, command=self.fetch_data, text="Show All", font=(
            "arial", 13, "bold"), width=10, bg="blue", fg="white")
        btn_show.grid(row=0, column=4, padx=5)

        # emptable
        tab_fr = Frame(rFrame, bd=4, relief=RIDGE)
        tab_fr.place(x=5, y=80, width=770, height=400)

        scroll_x = ttk.Scrollbar(tab_fr, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tab_fr, orient=VERTICAL)
        # treeview for heading
        self.employee_table = ttk.Treeview(tab_fr, column=(
            "name", "id", "phn", "email", "des", "gender", "add", "bday", "salary",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("name", text="Employee Name:")
        self.employee_table.heading("id", text="Employee ID:")
        self.employee_table.heading("phn", text="Phone number:")
        self.employee_table.heading("email", text="Email:")
        self.employee_table.heading("des", text="Designation:")
        self.employee_table.heading("gender", text="Gender:")
        self.employee_table.heading("add", text="Address:")
        self.employee_table.heading("bday", text="DOB")
        self.employee_table.heading("salary", text="Salary CTC:")
        self.employee_table["show"] = "headings"

        self.employee_table.column("name", width=100)
        self.employee_table.column("id", width=100)
        self.employee_table.column("phn", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("des", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("add", width=100)
        self.employee_table.column("bday", width=100)
        self.employee_table.column("salary", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_data)
        self.fetch_data()
# function used to fill the new employee data

    def add_data(self):
        if(self.var_id.get() == "" or self.var_email.get() == "" or self.var_phn.get() == ""):
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                conn = mysql.connector.connect(
                    host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_name.get(),
                    self.var_id.get(),
                    self.var_phn.get(),
                    self.var_email.get(),
                    self.var_des.get(),
                    self.var_gender.get(),
                    self.var_add.get(),
                    self.var_bday.get(),
                    self.var_salary.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Employee details have been added!", parent=self.portal)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.portal)
# this function is used to fetch the data from the database

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()
# once you click on a particular employee row, this function shows the data in the left frame
# accordingly

    def get_data(self, event=""):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        data = content["values"]

        self.var_name.set(data[0])
        self.var_id.set(data[1])
        self.var_phn.set(data[2])
        self.var_email.set(data[3])
        self.var_des.set(data[4])
        self.var_gender.set(data[5])
        self.var_add.set(data[6])
        self.var_bday.set(data[7])
        self.var_salary.set(data[8])
# this function is used to update any particular value

    def update(self):
        if (self.var_id.get() == "" or self.var_email.get() == "" or self.var_phn.get() == ""):
            messagebox.showerror("Error", "All fields are required!")
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update Employee data?", parent=self.portal)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE employee SET employeename=%s,phn_no=%s,emp_email=%s,emp_designation=%s,emp_gender=%s,emp_address=%s,emp_dob=%s,emp_salary=%s WHERE employeeid=%s", (
                        self.var_name.get(),
                        self.var_phn.get(),
                        self.var_email.get(),
                        self.var_des.get(),
                        self.var_gender.get(),
                        self.var_add.get(),
                        self.var_bday.get(),
                        self.var_salary.get(),
                        self.var_id.get(),
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Success", "Employee details Updated successfully!", parent=self.portal)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.portal)
# this function is used to delete a particular row from the database

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "All fields are required",parent=self.portal)
        else:
            try:
                Delete = messagebox.askyesno(
                    "Delete", "Are you sure to delete this entry?")
                if Delete > 0:
                    conn = mysql.connector.connect(
                        host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                    my_cursor = conn.cursor()
                    sql = "delete from employee where employeeid=%s"
                    value = (self.var_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Entry has been deleted!", parent=self.portal)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.portal)
# once this function gets initiated, it resets the whole values
# in the left frame to ""

    def reset(self):

        self.var_id.set("")
        self.var_name.set("")
        self.var_phn.set("")
        self.var_email.set("")
        self.var_des.set("")
        self.var_gender.set("Select Gender: ")
        self.var_add.set("")
        self.var_bday.set("")
        self.var_salary.set("")

    def search(self):
        if self.var_search.get() == "" or self.var_search1.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = mysql.connector.connect(
                    host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employee where "+str(
                    self.var_search.get())+" LIKE '%"+str(self.var_search1.get())+"%'")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.employee_table.delete(
                        *self.employee_table.get_children())
                    for i in data:
                        self.employee_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.portal)


# generate and take photos

    def gen_data(self):
        if self.var_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "All fields required", parent=self.portal)
        else:
            try:
                conn = mysql.connector.connect(
                    host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from employee")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update employee set employeename=%s,phn_no=%s,emp_email=%s,emp_designation=%s,emp_gender=%s,emp_address=%s,emp_dob=%s,emp_salary=%s where employeeid=%s", (
                    self.var_name.get(),
                    self.var_phn.get(),
                    self.var_email.get(),
                    self.var_des.get(),
                    self.var_gender.get(),
                    self.var_add.get(),
                    self.var_bday.get(),
                    self.var_salary.get(),
                    self.var_id.get() == id+1,
                ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

            # loading data
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cam = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cam.read()
                    if face_cropped(my_frame) is not None:

                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "facerecognition/data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed!")
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.portal)


if __name__ == "__main__":
    portal = Tk()
    obj = employee(portal)
    portal.mainloop()
