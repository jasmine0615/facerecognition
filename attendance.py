from importlib.resources import path
import os
from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import numpy as np

mydata = []

#defining the structure of the window
class attend:
    def __init__(self, portal):
        self.portal = portal
        self.portal.geometry("1530x790+0+0")
        self.portal.title("Employee Attendance management system")

        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_des = StringVar()
        self.var_gender = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()

        img = Image.open(
            r"images\backg.jpg")
        img = img.resize((1530, 710), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img)
        bg_lbl = Label(self.portal, image=self.photo1, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=1530, height=810)
#creating frames and grids for the attendance portal
        main_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=15, y=55, width=1500, height=680)

        lbl_title = Label(self.portal, text="Attendance Portal", font=(
            "times new roman", 37, "bold"), fg="blue", bg="pink")
        lbl_title.place(x=0, y=-10, width=1530, height=50)

        lFrame = LabelFrame(main_frame, bd=4, relief=RIDGE, padx=2, text="Employee Details", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        lFrame.place(x=10, y=10, width=660, height=650)

        emp_id = Label(lFrame, font=("arial", 12, "bold"),
                       text="Employee ID:", bg="white")
        emp_id.grid(row=0, column=0, sticky=W, padx=2, pady=7)
        emp_id_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_id, width=22)
        emp_id_entry.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        emp_name = Label(lFrame, font=("arial", 12, "bold"),
                         text="Employee Name:", bg="white")
        emp_name.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        emp_name_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_name, width=22)
        emp_name_entry.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        emp_des = Label(lFrame, font=("arial", 12, "bold"),
                        text="Designation:", bg="white")
        emp_des.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        emp_des_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_des, width=22)
        emp_des_entry.grid(row=5, column=0, sticky=W, padx=2, pady=7)

        emp_gen = Label(lFrame, font=("arial", 12, "bold"),
                        text="Gender:", bg="white")
        emp_gen.grid(row=6, column=0, sticky=W, padx=2, pady=7)
        emp_gen_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_gender, width=22)
        emp_gen_entry.grid(row=7, column=0, sticky=W, padx=2, pady=7)

        emp_tm = Label(lFrame, font=("arial", 12, "bold"),
                       text="TIME:", bg="white")
        emp_tm.grid(row=0, column=1, sticky=W, padx=2, pady=7)
        emp_tm_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_time, width=22)
        emp_tm_entry.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        emp_dt = Label(lFrame, font=("arial", 12, "bold"),
                       text="DATE:", bg="white")
        emp_dt.grid(row=2, column=1, sticky=W, padx=2, pady=7)
        emp_dt_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_date, width=22)
        emp_dt_entry.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        emp_stat = Label(lFrame, font=("arial", 12, "bold"),
                         text="Status:", bg="white")
        emp_stat.grid(row=4, column=1, sticky=W, padx=2, pady=7)
        emp_stat_entry = ttk.Entry(lFrame, font=(
            "arial", 12, "bold"), textvariable=self.var_status, width=22)
        emp_stat_entry.grid(row=5, column=1, sticky=W, padx=2, pady=7)

        bn_frame = Frame(lFrame, bd=2, relief=RIDGE, bg="white")
        bn_frame.place(x=0, y=500, width=640, height=105)
        imp_frm = Button(bn_frame, text="Import csv", command=self.imp_dt, font=(
            "arial", 13, "bold"), width=17, height=3, bg="blue", fg="white")
        imp_frm.grid(row=0, column=0, padx=15, pady=10)
        exp_frm = Button(bn_frame, text="Export csv", command=self.exp, font=(
            "arial", 13, "bold"), width=17, height=3, bg="blue", fg="white")
        exp_frm.grid(row=0, column=1, padx=15, pady=10)

        res_frm = Button(bn_frame, text="Reset", command=self.reset, font=(
            "arial", 13, "bold"), width=17, height=3, bg="blue", fg="white")
        res_frm.grid(row=0, column=4, padx=15, pady=10)

        rFrame = LabelFrame(main_frame, bd=4, relief=RIDGE, padx=2, text="Employee Attendance Details", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        rFrame.place(x=680, y=10, width=800, height=650)

        searchFr = LabelFrame(rFrame, bd=4, relief=RIDGE, padx=2, text="Track employee attendance", font=(
            "times new roman", 14, "bold"), fg="blue", bg="white")
        searchFr.place(x=0, y=10, width=790, height=600)

        # tableeee for showing the imported attendance data
        tab_fr = Frame(rFrame, bd=4, relief=RIDGE)
        tab_fr.place(x=5, y=80, width=770, height=520)

        scroll_x = ttk.Scrollbar(tab_fr, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tab_fr, orient=VERTICAL)
        self.details_table = ttk.Treeview(tab_fr, column=(
            "id", "name", "des", "gender", "time", "date", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)
        self.details_table.heading("id", text="Employee ID:")
        self.details_table.heading("name", text="Employee Name:")
        self.details_table.heading("des", text="Designation:")
        self.details_table.heading("gender", text="Gender:")
        self.details_table.heading("time", text="Time:")
        self.details_table.heading("date", text="Date:")
        self.details_table.heading("status", text="Status:")
        self.details_table["show"] = "headings"

        self.details_table.column("id", width=100)
        self.details_table.column("name", width=100)
        self.details_table.column("des", width=100)
        self.details_table.column("gender", width=100)
        self.details_table.column("time", width=100)
        self.details_table.column("date", width=100)
        self.details_table.column("status", width=100)
        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease>", self.cursor)

    def fetchData(self, rows):
        self.details_table.delete(*self.details_table.get_children())
        for i in rows:
            self.details_table.insert("", END, values=i)
#importing the data file using this function
    def imp_dt(self):

        global mydata
        fl = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*csv"), ("All File", "*.*")), parent=self.portal)
        with open(fl) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
#exporting the data file using this function
    def exp(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No data", "No data found to export", parent=self.portal)
                return False
            fl = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*csv"), ("All File", "*.*")), parent=self.portal)
            with open(fl, mode="w", newline="") as myfile:
                exp = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp.writerow(i)
                messagebox.showinfo(
                    "export", "your data is exported to "+os.path.basename(fl)+"succesfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To:{str(es)}", parent=self.portal)

    def cursor(self, event=""):
        cursor_row = self.details_table.focus()
        content = self.details_table.item(cursor_row)
        rows = content["values"]
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_des.set(rows[2])
        self.var_gender.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_status.set(rows[6])

    def reset(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_des.set("")
        self.var_gender.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")


if __name__ == "__main__":
    portal = Tk()
    obj = attend(portal)
    portal.mainloop()
