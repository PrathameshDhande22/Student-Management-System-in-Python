from tkinter import *
import tkinter
from tkinter.ttk import Combobox, Treeview
from windows import backend as bk, login_win
from tkinter import messagebox as mb


class SA:
    def __init__(self, win, list, tuple):
        self.win = win
        self.img_list = list
        self.user_tuple = tuple
        self.__sa_gui()

    def __sa_gui(self):
        self.counter = 0
        self.frame1 = Frame(self.win, width=1400,
                            height=790, background="#fca503")
        self.frame4 = Frame(self.frame1, width=1350,
                            height=600, bg="#fca503", bd=3)
        self.frame3 = Frame(self.frame1, width=1350,
                            height=600, bg="#fca503", bd=3)
        self.frame1.place(x=0, y=0)
        Label(self.frame1, text="WELCOME  SUPERADMIN !", font=(
            "Lucida Calligraphy", 40), bg="#fca503").place(x=250, y=30)
        self.menu_lbl = Label(background="#02b5d9")
        Button(self.frame1, text="Menu", font=("Verdana", 13), bg="#027cd9", relief="solid", bd=1, fg="white",
               activebackground="#027cd9", width=8, height=1, command=self.place_label_menu).place(x=20, y=120)
        Button(self.frame1, text="Logout", font=("Verdana", 13), bg="#027cd9", relief="solid", bd=1,
               fg="white", activebackground="#027cd9", width=8, height=1, command=self.logout).place(x=130, y=120)
        Button(self.frame1, image=self.img_list[3], bg="#027cd9", relief="solid", bd=1, fg="white",
               activebackground="#027cd9", width=60, command=self.home_icons).place(x=240, y=120)

        self.lbl = Label(bg="#fca503", height=15, width=13)
        Button(self.lbl, text="Add New\nAdmin", font=("Calibri Light", 13), bg="#02cad9", width=9,
               relief="solid", activebackground="yellow", command=self.new_admin).place(x=0, y=1)
        Button(self.lbl, text="Update Your\nPassword", font=("Calibri Light", 13), bg="#02cad9", width=9,
               relief="solid", activebackground="yellow", command=self.update_password_frame).place(x=0, y=63)
        Button(self.lbl, text=" Manage\nAdmin", font=("Calibri Light", 13), bg="#02cad9", width=9,
               relief="solid", activebackground="yellow", command=self.manage_admin).place(x=0, y=125)
        self.frame1.bind("<Button-1>", self.forget_place)
        self.frame2 = Frame(self.frame1, width=1350,
                            height=600, bg="#fca503", bd=4)
        self.frame2.place(x=20, y=170)
        self.frame2.bind("<Button-1>", self.forget_place)
        self.info_lbl = Label(
            self.frame1, text="Click On Menu button to Add New Admin or to Update Your Password\nSuper Admin can Only add admin or Manage the Admin.", font="lucida 16", bg="#fca503")
        self.info_lbl.place(x=350, y=220)
        self.imgsalabel = Label(
            self.frame1, image=self.img_list[4], bg="#fca503")
        self.imgsalabel.place(x=550, y=310)

    def update_password_frame(self):

        self.info_lbl.place_forget()
        self.imgsalabel.place_forget()
        self.forget_place(None)
        try:
            self.frame3.place_forget()
            self.frame4.place_forget()
            self.frame2.place(x=20, y=170)
        except:
            pass
        Label(self.frame2, text="UPDATE USERNAME & PASSWORD", font=(
            "lucida", 20, "bold", "underline"), bg="#fca503").place(x=300, y=10)
        Label(self.frame2, text=f"ID : {self.user_tuple[0]}", font=(
            "lucida", 16), bg="#fca503").place(x=375, y=80)
        Label(self.frame2, text="Username : ", font=(
            "lucida", 16), bg="#fca503").place(x=300, y=120)
        Label(self.frame2, text="Enter New Password : ", font=(
            "lucida", 16), bg="#fca503").place(x=200, y=160)
        Label(self.frame2, text="Confirm Password : ", font=(
            "lucida", 16), bg="#fca503").place(x=222, y=200)
        self.uname = StringVar(value=self.user_tuple[1])
        self.password = StringVar()
        self.confirm_password = StringVar()
        self.uname_txt = Entry(self.frame2, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid", textvariable=self.uname)
        self.uname_txt.place(x=420, y=120)
        self.pass_txt = Entry(self.frame2, font=("Times New Roman", 16), background="white",
                              show="•", width=20, bd=2, relief="solid", textvariable=self.password)
        self.pass_txt.place(x=420, y=160)
        self.confirm_pass_txt = Entry(self.frame2, textvariable=self.confirm_password, font=(
            "Times New Roman", 16), background="white", show="•", width=20, bd=2, relief="solid")
        self.confirm_pass_txt.place(x=420, y=200)
        self.count = IntVar()
        Button(self.frame2, text="Update", font=("Verdana", 16), bg="#027cd9", relief="groove", bd=2,
               fg="white", activebackground="#027cd9", width=9, height=1, command=self.update).place(x=350, y=290)
        self.show_pass = Checkbutton(self.frame2, text="Show Password", variable=self.count, background="#fca503",
                                     activebackground="#fca503", font=("Calibri", 14, "bold"), command=self.show_password).place(x=380, y=230)

    def update(self):
        if self.password.get() != self.confirm_pass_txt.get() or self.password.get() == "" or self.confirm_pass_txt.get() == "" or self.uname.get() == "":
            mb.showwarning(
                "Error", "New Password and Confirm Password Must be same\nOr check Your Username input")

        else:
            query = '''update login_details set uname=%s, password=sha(%s)  where id=%s;'''
            val = (f"{self.uname.get()}", f"{self.password.get()}",
                   f"{self.user_tuple[0]}")
            if bk.execute_query(query, val):
                mb.showinfo("Success", "Updated Successfully")
                self.password.set("")
                self.count.set(0)
                self.confirm_password.set("")
            else:
                mb.showerror("Error", "Some Error Occured")

    def new_admin(self):
        self.forget_place(None)
        self.info_lbl.place_forget()
        self.imgsalabel.place_forget()
        self.frame2.place_forget()
        self.frame4.place_forget()
        self.frame3.place(x=20, y=170)
        self.frame3.bind("<Button-1>", self.forget_place)
        Label(self.frame3, text="    ADD NEW ADMIN   ", font=(
            "lucida", 20, "bold", "underline"), bg="#fca503").place(x=560, y=10)
        Label(self.frame3, text=f"ID : Added Automatically",
              font=("lucida", 16), bg="#fca503").place(x=307, y=70)
        Label(self.frame3, text="Name : ", font=(
            "lucida", 16), bg="#fca503").place(x=270, y=110)
        Label(self.frame3, text="Phone No : ", font=(
            "lucida", 16), bg="#fca503").place(x=232, y=150)
        Label(self.frame3, text="AGE : ", font=(
            "lucida", 16), bg="#fca503").place(x=280, y=190)
        Label(self.frame3, text="Gender : ", font=(
            "lucida", 16), bg="#fca503").place(x=250, y=230)
        Label(self.frame3, text="Address : ", font=(
            "lucida", 16), bg="#fca503").place(x=240, y=270)
        Label(self.frame3, text="Username : ", font=(
            "lucida", 16), bg="#fca503").place(x=222, y=370)
        Label(self.frame3, text="Password : ", font=(
            "lucida", 16), bg="#fca503").place(x=222, y=410)
        self.name = StringVar()
        self.phoneno = IntVar()
        self.auname = StringVar()
        self.apass = StringVar()
        self.age = IntVar()
        self.name_txt = Entry(self.frame3, textvariable=self.name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.name_txt.place(x=350, y=110)
        self.phone_txt = Entry(self.frame3, textvariable=self.phoneno, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.phone_txt.place(x=350, y=150)
        self.age_box = Spinbox(self.frame3, textvariable=self.age, from_=18, to=70, state="readonly",
                               bg="white", width=3, font=("Times New Roman", 16), bd=2, relief="solid")
        self.age_box.place(x=350, y=190)
        self.gender_box = Combobox(self.frame3, background="white", values=(
            "Male", "Female", "Other"), font=("Times New Roman", 16), state="readonly", width=10)
        self.gender_box.place(x=350, y=230)
        self.address_txt = Text(self.frame3, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), height=4, width=37)
        self.address_txt.place(x=350, y=270)
        self.auname_txt = Entry(self.frame3, textvariable=self.auname, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.auname_txt.place(x=350, y=370)
        self.apass_txt = Entry(self.frame3, font=(
            "Times New Roman", 16), textvariable=self.apass, background="white", width=20, bd=2, relief="solid")
        self.apass_txt.place(x=350, y=410)
        Button(self.frame3, text="ADD", font=("Verdana", 16), bg="#027cd9", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", width=9, height=1, command=self.validate).place(x=320, y=470)
        Button(self.frame3, text="Reset", font=("Verdana", 16), bg="#027cd9", relief="groove", bd=2,
               fg="white", activebackground="#027cd9", width=9, height=1, command=self.reset).place(x=480, y=470)

    def place_label_menu(self):
        if self.counter == 0:
            self.lbl.place(x=20, y=153)
            self.counter = 1
        else:
            self.lbl.place_forget()
            self.counter = 0

    def forget_place(self, e):
        try:
            self.counter = 0
            self.lbl.place_forget()
        except:
            pass

    def logout(self):
        a = mb.askyesno("Confirmation", "Are You Sure, You want to logout ?")
        if a:
            mb.showinfo("Done", "Successfully Logout !")
            login_win.login(self.win, self.img_list)

    def show_password(self):
        try:
            if self.count.get() == 1:
                self.pass_txt.configure(show="")
                self.confirm_pass_txt.configure(show="")
            else:
                self.pass_txt.configure(show="•")
                self.confirm_pass_txt.configure(show="•")
        except AttributeError as AE:
            pass
        except Exception as ex:
            print(ex)

    def validate(self):
        try:
            if self.name.get() == "" or self.phoneno.get() == "" or self.auname.get() == "" or self.apass.get() == "":
                mb.showerror(
                    "Wrong Input", "Please Check The Fields\nOne or More Field You have entered is Wrong")
            elif self.address_txt.get(1.0, END) == " " or self.address_txt.get(1.0, END) == "":
                mb.showerror("Wrong Address", "Enter The Correct Address")
            elif len(str(self.phoneno.get())) != 10 or self.phoneno.get() == "":
                mb.showerror("Error", "Enter The correct Phone Number")
            else:
                if bk.call_procedure('addadmin', (self.name.get(), self.address_txt.get(1.0, END), self.phoneno.get(), self.age_box.get(), self.gender_box.get())):
                    id = bk.fetch_details('select * from admin where name=%s and address=%s and age=%s and phoneno=%s and sex=%s',
                                          (self.name.get(), self.address_txt.get(1.0, END), self.age_box.get(), self.phoneno.get(), self.gender_box.get()))[0]
                    bk.execute_query("insert into login_details values (%s,%s,sha(%s),'admin');", (
                        id[0], self.auname.get(), self.apass.get()))
                    # bk.execute_query('insert into login_details values (%s,%s,%s,')
                    mb.showinfo("Success", "Admin Added Successfully")
                    self.reset()
                else:
                    mb.showerror("Error", "Some Error Occured")
        except tkinter.TclError:
            mb.showerror("Error", "Enter the Number Only")

    def reset(self):
        self.auname.set("")
        self.apass.set("")
        self.phoneno.set(0)
        self.gender_box.set("")
        self.name.set("")
        self.address_txt.delete(1.0, END)
        self.age.set(18)

    def home_icons(self):
        try:
            self.frame2.place_forget()
            self.frame3.place_forget()
            self.frame4.place_forget()
            self.info_lbl.place(x=350, y=220)
            self.imgsalabel.place(x=550, y=310)

        except Exception as e:
            print(e)

    def manage_admin(self):
        try:
            self.info_lbl.place_forget()
            self.imgsalabel.place_forget()
            self.frame3.place_forget()
            self.frame2.place_forget()
        except:
            pass
        self.frame4.place(x=20, y=170)
        self.frame2.place_forget()

        self.frame4.bind("<Button-1>", self.forget_place)
        self.forget_place(None)
        Label(self.frame4, text="MANAGE ADMIN", font=("lucida", 20,
              "bold", "underline"), bg="#fca503").place(x=10, y=5)
        Label(self.frame4, text="Click On the id for\nwhich the details you want", font=(
            "lucida", 15, "bold"), bg="#fca503").place(x=1000, y=300)
        Label(self.frame4, text=f"ID : ", font=(
            "lucida", 16), bg="#fca503").place(x=80, y=70)
        Label(self.frame4, text="Name : ", font=(
            "lucida", 16), bg="#fca503").place(x=45, y=110)
        Label(self.frame4, text="Phone No : ", font=(
            "lucida", 16), bg="#fca503").place(x=5, y=150)
        Label(self.frame4, text="AGE : ", font=(
            "lucida", 16), bg="#fca503").place(x=52, y=190)
        Label(self.frame4, text="Gender : ", font=(
            "lucida", 16), bg="#fca503").place(x=27, y=230)
        Label(self.frame4, text="Address : ", font=(
            "lucida", 16), bg="#fca503").place(x=20, y=270)
        Label(self.frame4, text="Username : ", font=(
            "lucida", 16), bg="#fca503").place(x=0, y=370)
        Label(self.frame4, text="Password : ", font=(
            "lucida", 16), bg="#fca503").place(x=0, y=410)
        self.name = StringVar()
        self.phoneno = IntVar()
        self.auname = StringVar()
        self.apass = StringVar()
        self.id = StringVar()
        self.age = IntVar()
        self.name_txt = Entry(self.frame4, textvariable=self.name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.name_txt.place(x=123, y=110)
        self.id_txt = Entry(self.frame4, state="disabled", textvariable=self.id, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.id_txt.place(x=123, y=70)
        self.phone_txt = Entry(self.frame4, textvariable=self.phoneno, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.phone_txt.place(x=123, y=150)
        self.age_box = Spinbox(self.frame4, textvariable=self.age, from_=18, to=70, state="readonly",
                               bg="white", width=3, font=("Times New Roman", 16), bd=2, relief="solid")
        self.age_box.place(x=123, y=190)
        self.gender_box = Combobox(self.frame4, background="white", values=(
            "Male", "Female", "Other"), font=("Times New Roman", 16), state="readonly", width=10)
        self.gender_box.place(x=123, y=230)
        self.address_txt = Text(self.frame4, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), height=4, width=37)
        self.address_txt.place(x=123, y=270)
        self.auname_txt = Entry(self.frame4, textvariable=self.auname, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.auname_txt.place(x=123, y=370)
        self.apass_txt = Entry(self.frame4, font=(
            "Times New Roman", 16), textvariable=self.apass, background="white", width=20, bd=2, relief="solid")
        self.apass_txt.place(x=123, y=410)
        Button(self.frame4, text="UPDATE", font=("Verdana", 16), bg="#027cd9", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", width=9, height=1, command=self.update_madmin).place(x=0, y=470)
        Button(self.frame4, text="DELETE", font=("Verdana", 16), bg="#027cd9", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", width=9, height=1, command=self.delete_admin).place(x=160, y=470)
        self.table = Treeview(self.frame4, columns=[
                              "id", "Name", "Age", "a"], selectmode="browse", show="headings", height=10)
        self.table.place(x=500, y=10, height=500)
        self.table.heading("id", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("a", text="Gender")
        self.table.column("id", anchor="center", width=70)
        self.table.column("Name", anchor="center", width=210)
        self.table.column("Age", anchor="center", width=50)
        self.table.column("a", anchor="center", width=80)

        self.sc = Scrollbar(
            self.frame4, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=913, y=10, height=500)
        self.table_insert_records()
        self.table.bind("<<TreeviewSelect>>", self.filled_record)

    def table_insert_records(self):
        query = '''select id,name,age,sex from admin order by id;'''
        for data in bk.fetch_details(query):
            self.table.insert("", END, values=data)

    def filled_record(self, e):
        # a=self.table.selection()[0]
        try:
            id = self.table.item(self.table.selection()[0])["values"][0]
            self.address_txt.delete(1.0, END)
            data = bk.fetch_details(
                "select * from admin where id=%s", (id,))[0]
            self.phoneno.set(data[3])
            self.name.set(data[1])
            self.gender_box.set(data[5])
            self.age.set(data[4])
            self.address_txt.insert(1.0, data[2], END)
            self.id.set(data[0])
            login = bk.fetch_details(
                "select uname from login_details where id=%s;", (id,))[0][0]
            self.auname.set(login)
        except:
            pass

    def update_madmin(self):
        if self.name.get() == "" or self.phoneno.get() == "" or self.auname.get() == "":
            mb.showerror(
                "Wrong Input", "Please Check The Fields\nOne or More Field You have entered is Wrong")
        elif self.address_txt.get(1.0, END) == " " or self.address_txt.get(1.0, END) == "":
            mb.showerror("Wrong Address", "Enter The Correct Address")
        elif len(str(self.phoneno.get())) != 10 or self.phoneno.get() == "":
            mb.showerror("Error", "Enter The correct Phone Number")
        elif self.apass.get() == "":
            mb.showwarning(
                "Error", "Please Enter Admin Password\nFor Updating a new password is added")
        else:
            query = '''update admin set name=%s,address=%s,phoneno=%s,age=%s,sex=%s where id=%s;'''
            val = (self.name.get(), self.address_txt.get(1.0, END), self.phoneno.get(
            ), self.age_box.get(), self.gender_box.get(), self.id.get())
            if bk.execute_query(query, val):
                bk.execute_query('update login_details set uname=%s,password=sha(%s) where id=%s', (
                    self.auname.get(), self.apass.get(), self.id.get()))
                mb.showinfo("Success", "Updated the Record Successfully")
                for item in self.table.get_children():
                    self.table.delete(item)
                self.table_insert_records()
                self.reset()
                self.id.set("")
            else:
                mb.showerror("Error", "Some Error Occured")

    def delete_admin(self):
        if self.name.get() == "":
            mb.showinfo("Information", "Please Select The One Record")
        else:
            a = mb.askyesnocancel(
                "Confirmation", f"You Want to delete the record of {self.name.get()}")
            if a:
                if bk.execute_query("delete from admin where id=%s", (self.id.get(),)):
                    mb.showinfo('Success', "Record Deleted Successfully")
                    for item in self.table.get_children():
                        self.table.delete(item)
                    self.table_insert_records()
                    self.reset()
                    self.id.set("")
                else:
                    mb.showerror("Error", "Some Error Occured")
