from tkinter import *
from tktooltip import ToolTip
from windows import backend as bk, superadmin as sp, admin as ad, faculty, student
from tkinter import messagebox as mb, simpledialog as sd
from tkcalendar import DateEntry


class login():
    def __init__(self, win, img_list):
        self.win = win
        self.img_list = img_list
        self.login_gui()

    def login_gui(self):
        self.username = StringVar()
        self.password = StringVar()
        self.frame1 = Frame(self.win, width=1400,
                            height=790, background="green")
        self.win.config(background="red")
        Label(self.frame1, image=self.img_list[0]).place(x=0, y=0)
        self.frame1.place(x=0, y=0)
        self.lbl = Frame(self.frame1, height=460, width=490,
                         background="#4bf542", bd=2, relief="solid")
        self.lbl.place(x=430, y=140)
        Label(self.lbl, text="LOGIN", font=("Segoe UI Black", 40),
              background="#4bf542").place(x=160, y=10)
        Label(self.lbl, text="Username :", font=("Century", 20),
              background="#4bf542").place(x=10, y=100)
        self.uname_txt = Entry(self.lbl, font=(
            "Times New Roman", 27), background="white", width=25, bd=1, relief="solid", textvariable=self.username)
        self.uname_txt.place(x=15, y=145)
        Label(self.lbl, text="Password :", font=("Century", 20),
              background="#4bf542").place(x=10, y=220)
        self.pass_txt = Entry(self.lbl, font=("Times New Roman", 27),
                              background="white", show="•", width=25, bd=1, relief="solid", textvariable=self.password)
        self.pass_txt.place(x=15, y=270)
        self.reset_btn = Button(self.lbl, image=self.img_list[2], background="#4bf542",
                                activebackground="#4bf542", relief="flat", command=self.reset_field)
        self.reset_btn.place(x=150, y=390)
        Button(self.lbl, image=self.img_list[1], background="#4bf542", height=42,
               width=110, relief="flat", activebackground="#4bf542", command=self.logon).place(x=20, y=390)
        self.count = IntVar()
        self.show_pass = Checkbutton(self.lbl, text="Show Password", variable=self.count, background="#4bf542",
                                     activebackground="#4bf542", font=("Calibri", 14, "bold"), command=self.show_password).place(x=16, y=330)
        ToolTip(self.reset_btn, msg="Reset the field", follow=True)
        self.forgot = Label(self.lbl, text="Forgot Username/Password ?", background="#4bf542",
                            foreground="blue", font=("Calibri", 12, "bold", "underline"))
        self.forgot.place(x=260, y=330)
        self.forgot.bind("<Button-1>", self.__forgot_frame)
        self.main_label = Label(self.frame1, text="STUDENT MANAGEMENT SYSTEM", font=(
            "Times New Roman", 40)).place(x=250, y=30)

    def reset_field(self):
        self.username.set("")
        self.password.set("")

    def __forgot_frame(self, e):
        self.lbl.place_forget()
        self.lbl1 = Frame(self.frame1, height=600, width=500,
                          background="#4bf542", bd=2, relief="solid")
        self.lbl1.place(x=400, y=140)
        self.backlbl = Label(self.lbl1, text="Back to Login Page", background="#4bf542",
                             foreground="blue", font=("Calibri", 14, "bold", "underline"))
        self.backlbl.place(x=10, y=560)
        self.backlbl.bind("<Button-1>", lambda e: self.login_gui())
        Label(self.lbl1, text="Forgot Username/Password", font=("lucida",
              18, "bold"), background="#4bf542").place(x=100, y=10)
        self.id = StringVar()
        Label(self.lbl1, text="Enter Your ID :", font=(
            "Century", 13), background="#4bf542").place(x=10, y=70)
        Label(self.lbl1, text="Enter Your Date Of Birth : (mm/dd/yyyy) format",
              font=("Century", 13), background="#4bf542").place(x=10, y=140)
        Entry(self.lbl1, textvariable=self.id, font=(
            "Times New Roman", 19), relief="solid", bd=2).place(x=10, y=100)
        self.dob = DateEntry(self.lbl1, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.dob.place(x=10, y=170)
        Button(self.lbl1, text="Get Username", font=("Verdana", 15), bg="#fab6b1",
               relief="ridge", bd=2, command=self.__get_username).place(x=100, y=240)
        Button(self.lbl1, text="Forgot Password", font=("Verdana", 15), bg="#fab6b1",
               relief="ridge", bd=2, command=self.__set_password).place(x=270, y=240)

    def validation(self):
        query = '''select uname,typeofuser from login_details where id=%s'''
        data = bk.fetch_details(query, (self.id.get(),))
        if len(data) == 0:
            mb.showinfo("No User", f"No User Found with ID {self.id.get()}")
        elif data[0][1] == "student":
            mb.showinfo(
                "Access Denied", "Hello You are Student\nContact to Admin Office to set your username or password")
            self.login_gui()
        elif data[0][1] == "faculty":
            facultydob = 'select dob from faculty where id=%s;'
            data1 = bk.fetch_details(facultydob, (self.id.get(),))
            if data1[0][0] != self.dob.get_date():
                mb.showinfo("Error", "Incorrect Date of birth")
            else:
                return True
        elif data[0][1] == "admin":
            return True

    def __get_username(self):
        if self.validation():
            uname = bk.fetch_details(
                '''select uname from login_details where id=%s''', (self.id.get(),))[0][0]
            mb.showinfo("Username", f"Your Username is {uname}")

    def __set_password(self):
        if self.validation():
            self.password_label = Label(
                self.lbl1, bg="#4bf542", height=14, width=70)
            self.password_label.place(x=0, y=310)
            self.new_password = StringVar()
            self.reenter_password = StringVar()
            self.new_password_txt = Entry(self.password_label, font=(
                "Times New Roman", 15), background="white", show="•", width=25, bd=1, relief="solid", textvariable=self.new_password)
            self.new_password_txt.place(x=10, y=30)
            self.reenter_pass_txt = Entry(self.password_label, font=(
                "Times New Roman", 15), background="white", show="•", width=25, bd=1, relief="solid", textvariable=self.reenter_password)
            self.reenter_pass_txt.place(x=10, y=100)
            Label(self.password_label, text="Enter New Password :", font=(
                "Century", 13), background="#4bf542").place(x=10, y=0)
            Label(self.password_label, text="Re-enter Password :",
                  font=("Century", 13), background="#4bf542").place(x=10, y=70)
            Button(self.password_label, text="UPDATE", font=("Verdana", 16), bg="#ecfc05",
                   relief="raised", bd=2, command=self.__change_password).place(x=30, y=140)
            self.show_pass = Checkbutton(self.password_label, text="Show Password", variable=self.count, background="#4bf542",
                                         activebackground="#4bf542", font=("Calibri", 13), command=self.show_password1).place(x=280, y=60)

    def show_password1(self):
        if self.count.get() == 1:
            self.new_password_txt.configure(show="")
            self.reenter_pass_txt.configure(show="")
        else:
            self.new_password_txt.configure(show="•")
            self.reenter_pass_txt.configure(show="•")

    def __change_password(self):
        if self.new_password.get() != self.reenter_password.get():
            mb.showerror("Error", "The Passwords are Not matching")
        else:
            query = 'update login_details set password=sha(%s) where id=%s'
            val = (self.new_password.get(), self.id.get())
            if bk.execute_query(query, val):
                mb.showinfo("Success", "successfully changed the password")
                self.login_gui()
            else:
                mb.showerror("Server Error", "Some Error Occured")

    def show_password(self):
        if self.count.get() == 1:
            self.pass_txt.configure(show="")
        else:
            self.pass_txt.configure(show="•")

    def logon(self):
        self.user_name = self.username.get()
        self.pass_word = self.password.get()
        query = "select * from login_details where uname=%s and password=sha(%s);"
        val = (self.user_name, self.pass_word)
        result = bk.fetch_details(query, val)
        if len(result) == 0:
            mb.showerror(
                "No User", "No Username or Password Found\nPlease Check Your Username or password")
        else:
            result = result[0]
            typeofuser = result[3]
            id = result[0]
            self.change_frame(typeofuser, result)

    def change_frame(self, type, user_tuple):

        if type == "superadmin":
            self.frame1.place_forget()
            sp.SA(self.win, self.img_list, user_tuple)
        elif type == "admin":
            self.frame1.place_forget()
            ad.admin(self.win, self.img_list, user_tuple)
        elif type == "faculty":
            self.frame1.place_forget()
            faculty.Faculty(self.win, self.img_list, user_tuple)
        elif type == "student":
            self.frame1.place_forget()
            student.Student(self.win, self.img_list, user_tuple)
