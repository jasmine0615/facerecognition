from atexit import register
from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from front import Front


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, net):
        self.net = net
        self.net.title("Login")
        self.net.geometry("1550x800+0+0")

        self.var_email = StringVar()
        self.var_passw = StringVar()

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\jasmine p\Desktop\finalproj\emp2.jpg")
        lbl_bg = Label(self.net, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.net, bg="black")
        frame.place(x=610, y=190, width=340, height=450)
        avatar = Image.open(r"C:\Users\jasmine p\Desktop\finalproj\avv1.jpg")
        avatar = avatar.resize((120, 120), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(avatar)
        lblavatar1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblavatar1.place(x=730, y=190, width=100, height=100)

        get_start = Label(frame, text="Welcome! Let's get started", font=(
            "times new roman", 18, "bold"), fg="white", bg="black")
        get_start.place(x=38, y=100)

        # usernamelabel
        username = lbl = Label(frame, text="Username", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40, y=155)
        self.txtuser = ttk.Entry(frame, font=(
            "times new roman", 15, "bold")) 
        self.txtuser.place(x=40, y=180, width=270)
        # passwordlabel
        password = lbl = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=225)
        self.txtpw = ttk.Entry(frame, font=(
            "times new roman", 15, "bold"), show="*")
        self.txtpw.place(x=40, y=250, width=270)

        loginbtn = Button(frame, command=self.Login, text="Login", font=(
            "times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="blue", activeforeground="white", activebackground="blue")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User? Register", command=self.reg_window, font=(
            "times new roman", 10, "bold"), borderwidth=0, cursor="hand2", fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=160)

    def reg_window(self):
        self.new_window = Toplevel(self.net)
        self.app = Register(self.new_window)
# login button runs through the following code

    def Login(self):
        if self.txtuser.get() == "" or self.txtpw.get() == "":
            messagebox.showerror("Error", "all fields required")
        else:
            conn = mysql.connector.connect(
                host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from details where email=%s and password=%s", (
                self.var_email.get(),
                self.var_passw.get(),
            ))

            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin?")
                if open_main > 0:
                    self.new_window = Toplevel(self.net)
                    self.app = Front(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

# registration facility for the new admin


class Register:
    def __init__(self, net):
        self.net = net
        self.net.title("Register")
        self.net.geometry("1600x900+0+0")

        # data entry
        self.var_frname = StringVar()
        self.var_lname = StringVar()
        self.var_contactno = StringVar()
        self.var_email = StringVar()
        self.var_passw = StringVar()
        self.var_confpassw = StringVar()

        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\jasmine p\Desktop\finalproj\bgg.jpg")
        lbl_bg = Label(self.net, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\jasmine p\Desktop\finalproj\regist.jpg")
        lbl_wel = Label(self.net, image=self.bg1)
        lbl_wel.place(x=50, y=100, width=470, height=550)
        # registerwindow
        frame = Frame(self.net, bg="black")
        frame.place(x=520, y=100, width=800, height=550)
        lbl_register = Label(frame, text="REGISTER HERE!", font=(
            "times new roman", 25, "bold"), fg="pink", bg="black")
        lbl_register.place(x=20, y=20)

        frname = Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        frname.place(x=50, y=100)

        self.frname_entry = ttk.Entry(frame, textvariable=self.var_frname, font=(
            "times new roman", 15, "bold"))
        self.frname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        lname.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=(
            "times new roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        contactno = Label(frame, text="Contact No", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        contactno.place(x=50, y=170)
        self.txt_contactno = ttk.Entry(frame, textvariable=self.var_contactno, font=(
            "times new roman", 15, "bold"))
        self.txt_contactno.place(x=50, y=200, width=250)

        email = Label(frame, text="Email Id", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=(
            "times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        passw = Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        passw.place(x=50, y=250)
        self.txt_passw = ttk.Entry(frame, textvariable=self.var_passw, font=(
            "times new roman", 15, "bold"))
        self.txt_passw.place(x=50, y=280, width=250)
        confpassw = Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), fg="white", bg="black")
        confpassw.place(x=370, y=250)
        self.txt_confpassw = ttk.Entry(frame, textvariable=self.var_confpassw, font=(
            "times new roman", 15, "bold"))
        self.txt_confpassw.place(x=370, y=280, width=250)

        self.var_check = IntVar()
        self.chkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=(
            "times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.chkbtn.place(x=50, y=340)

        # login,reg
        img = Image.open(r"C:\Users\jasmine p\Desktop\finalproj\reg.jpg")
        img = img.resize((250, 55), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2")
        b1.place(x=45, y=390, width=210)

        img1 = Image.open(r"C:\Users\jasmine p\Desktop\finalproj\login1.jpg")
        img1 = img1.resize((250, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, command=self.return_login, image=self.photoimage1,
                    borderwidth=0, cursor="hand2")
        b2.place(x=390, y=320, width=180)
# initialising the registrarion window

    def register_data(self):
        if self.var_frname.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_passw.get() != self.var_confpassw.get():
            messagebox.showerror("Error", "Passwords do not match!")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please check the box")
        else:
            conn = mysql.connector.connect(
                host="sql6.freemysqlhosting.net", username="sql6495618", password="6fT2uk3lM3", database="sql6495618")
            my_cursor = conn.cursor()
            query = ("select * from details where email =%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User already exists! Try another email")
            else:
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s)", (
                    self.var_frname.get(),
                    self.var_lname.get(),
                    self.var_contactno.get(),
                    self.var_email.get(),
                    self.var_passw.get(),
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successfull")
            self.net.destroy()

    def return_login(self):
        self.net.destroy()


if __name__ == "__main__":
    main()
