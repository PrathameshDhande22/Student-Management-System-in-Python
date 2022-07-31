from datetime import datetime
from tkinter import messagebox as mb
from tkinter import *
from tkinter.ttk import Combobox, Treeview
from windows import login_win, backend, fees
from tkcalendar import DateEntry


"""Admin can Do:
        Features: 1.Home Page
                  2.Add Faculty
                  3.Manage Faculty
                  4.Add Student
                  5.Manage Student
                  6.Manage Fees
                  7.Logout"""


class admin:
    def __init__(self, win, list, user_tuple):
        self.win = win
        self.img_list = list
        self.user_tuple = user_tuple

        self.__a_gui()

    def __a_gui(self):

        # main frame
        name = self.get_admin_details()[0][1]
        self.frame1 = Frame(self.win, width=1400,
                            height=790, background="#84fa92")
        # profile or homepage frame
        self.frame2 = Frame(self.frame1, width=1375,
                            height=640, bg="#84fa92", bd=3)
        # add faculty frame
        self.frame3 = Frame(self.frame1, width=1375,
                            height=640, bg="#84fa92", bd=3)
        # manage faculty frame
        self.frame4 = Frame(self.frame1, width=1375,
                            height=640, bg="#84fa92", bd=3)
        # add student frame
        self.frame5 = Frame(self.frame1, width=1400,
                            height=640, bg="#84fa92", bd=3)
        # manage student frame
        self.frame6 = Frame(self.frame1, width=1400,
                            height=640, bg="#84fa92", bd=3)
        # fees frame
        self.frame7 = Frame(self.frame1, width=1400,
                            height=640, bg="#84fa92", bd=3)

        self.frame1.place(x=0, y=0)
        self.frame2.place(x=10, y=130)
        self.homepage()
        Label(self.frame1, image=self.img_list[5], bg="#84fa92").place(
            x=1290, y=10)
        Label(self.frame1, text=f"Welcome {name}", font=(
            "Verdana", 13), bg="#84fa92").place(x=1020, y=105)
        Label(self.frame1, text=f"ADMIN", font=(
            "Verdana", 25, "bold"), bg="#84fa92").place(x=1150, y=40)
        Button(self.frame1, image=self.img_list[3], bg="#7a02fa", relief="solid", bd=3, fg="white",
               activebackground="#fa0202", width=100, height=38, command=self.homeicon).place(x=20, y=10)
        Button(self.frame1, text="Add Faculty", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3, fg="white",
               activebackground="#fa0202", width=12, height=1, command=lambda: self.faculty(self.frame3, "add", 3)).place(x=140, y=10)
        Button(self.frame1, text="Manage Faculty", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3, fg="white",
               activebackground="#fa0202", width=14, height=1, command=lambda: self.manage_faculty(self.frame4, "manage")).place(x=345, y=10)
        Button(self.frame1, text="Add Student", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3, fg="white",
               activebackground="#fa0202", width=12, height=1, command=lambda: self.add_student(self.frame5, "add", 5)).place(x=580, y=10)
        Button(self.frame1, text="Manage Student", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3, fg="white",
               activebackground="#fa0202", width=15, height=1, command=lambda: self.manage_student(self.frame6)).place(x=20, y=65)
        Button(self.frame1, text="Fees", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="white", activebackground="#fa0202", width=8, height=1, command=self.__fees_frame).place(x=270, y=65)
        Button(self.frame1, text="Logout", bg="#7a02fa", font=("Verdana", 16, "bold"), relief="solid", bd=3,
               fg="white", activebackground="#fa0202", width=10, height=1, command=self.logout).place(x=415, y=65)

    def logout(self):
        a = mb.askyesno("Confirmation", "Are You Sure, You want to logout ?")
        if a:
            mb.showinfo("Done", "Successfully Logout !")
            login_win.login(self.win, self.img_list)

    # this contians the profile of the login admin
    def homepage(self):
        data = self.get_admin_details()

        Label(self.frame2, text="PROFILE", font=("Verdana", 20,
              "bold", "underline"), bg="#84fa92").place(x=650, y=10)
        Label(self.frame2, text=f"ID : {data[0][0]}", font=(
            "lucida", 16), bg="#84fa92").place(x=400, y=80)
        Label(self.frame2, text=f"Name : {data[0][1]}", font=(
            "lucida", 16), bg="#84fa92").place(x=365, y=110)
        Label(self.frame2, text=f"Address : {data[0][2]}", font=(
            "lucida", 16), bg="#84fa92").place(x=343, y=140)
        Label(self.frame2, text=f"Phone No. : {data[0][3]}", font=(
            "lucida", 16), bg="#84fa92").place(x=321, y=200)
        Label(self.frame2, text=f"Age : {data[0][4]}", font=(
            "lucida", 16), bg="#84fa92").place(x=383, y=230)
        Label(self.frame2, text=f"Sex : {data[0][5]}", font=(
            "lucida", 16), bg="#84fa92").place(x=383, y=260)
        Label(self.frame2, text=f"Username : {data[1]}", font=(
            "lucida", 16), bg="#84fa92").place(x=324, y=290)

    def faculty(self, frame, label_place, no):
        self.__remove_frames(no)
        frame.place(x=10, y=130)
        if label_place == "add":
            Label(frame, text="ADD FACULTY", font=("Verdana", 20,
                  "bold", "underline"), bg="#84fa92").place(x=600, y=10)
            Button(frame, text="Reset", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.reset).place(x=680, y=160)
            Button(frame, text="ADD", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.add_faculty_into_data).place(x=520, y=160)
        elif label_place == "manage":
            Button(frame, text="Update", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.update_faculty).place(x=680, y=160)
            Button(frame, text="Delete", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.delete_faculty).place(x=520, y=160)
            Label(frame, text="MANAGE FACULTY", font=("Verdana", 20,
                  "bold", "underline"), bg="#84fa92").place(x=570, y=10)
        Label(frame, text="First Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=50, y=60)
        Label(frame, text="Middle Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=32, y=100)
        Label(frame, text="Last Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=50, y=140)
        Label(frame, text="Date Of birth : ", font=(
            "lucida", 16), bg="#84fa92").place(x=32, y=180)
        Label(frame, text="Age : ", font=("lucida", 16),
              bg="#84fa92").place(x=115, y=220)
        Label(frame, text="Email : ", font=("lucida", 16),
              bg="#84fa92").place(x=100, y=260)
        Label(frame, text="Subject : ", font=(
            "lucida", 16), bg="#84fa92").place(x=80, y=300)
        Label(frame, text="Address : ", font=(
            "lucida", 16), bg="#84fa92").place(x=72, y=340)
        Label(frame, text="Qualification : ", font=(
            "lucida", 16), bg="#84fa92").place(x=30, y=410)
        Label(frame, text="Gender : ", font=("lucida", 16),
              bg="#84fa92").place(x=75, y=450)
        Label(frame, text="Date Of Joining : ", font=(
            "lucida", 16), bg="#84fa92").place(x=0, y=490)
        Label(frame, text="Experience : ", font=(
            "lucida", 16), bg="#84fa92").place(x=36, y=530)
        Label(frame, text="Phone No.: ", font=(
            "lucida", 16), bg="#84fa92").place(x=50, y=570)
        Label(frame, text="Username : ", font=(
            "lucida", 16), bg="#84fa92").place(x=520, y=60)
        Label(frame, text="Password : ", font=(
            "lucida", 16), bg="#84fa92").place(x=520, y=100)
        self.variables_used()
        # first name entry
        self.f_name_txt = Entry(frame, textvariable=self.f_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.f_name_txt.place(x=180, y=60)
        # middle name entry
        self.m_name_txt = Entry(frame, textvariable=self.m_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.m_name_txt.place(x=180, y=100)
        # last name entry
        self.l_name_txt = Entry(frame, textvariable=self.l_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.l_name_txt.place(x=180, y=140)
        # email entry box
        self.email_txt = Entry(frame, textvariable=self.email, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.email_txt.place(x=180, y=260)
        # date of birth entry
        self.dob = DateEntry(frame, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.dob.place(x=180, y=180)
        # date of joining
        self.doj = DateEntry(frame, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.doj.place(x=180, y=490)
        # subject entry
        self.subject_txt = Entry(frame, textvariable=self.subject, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.subject_txt.place(x=180, y=300)
        # phone entry
        self.phone_txt = Entry(frame, textvariable=self.phoneno, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.phone_txt.place(x=180, y=570)
        # Experience entry
        self.experi_txt = Entry(frame, textvariable=self.experi, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.experi_txt.place(x=180, y=530)
        # creatung the age box
        self.age_box = Spinbox(frame, from_=18, to=70, state="readonly", textvariable=self.age,
                               bg="white", width=3, font=("Times New Roman", 16), bd=2, relief="solid")
        self.age_box.place(x=180, y=220)
        # gender box
        self.gender_box = Combobox(frame, background="white", values=(
            "Male", "Female", "Other"), font=("Times New Roman", 16), state="readonly", width=10)
        self.gender_box.place(x=180, y=450)
        # creating the address txt
        self.address_txt = Text(frame, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), height=3, width=37)
        self.address_txt.place(x=180, y=340)
        # creating the qualification text
        self.qualifi_txt = Entry(frame, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), width=20, textvariable=self.qualifi)
        self.qualifi_txt.place(x=180, y=410)
        # username entry
        self.uname_txt = Entry(frame, textvariable=self.uname, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.uname_txt.place(x=635, y=60)
        # password entry
        self.pass_txt = Entry(frame, font=("Times New Roman", 16), textvariable=self.passw,
                              background="white", width=20, bd=2, relief="solid")
        self.pass_txt.place(x=635, y=100)

    def get_admin_details(self):
        id = self.user_tuple[0]
        query = '''select * from admin where id=%s;'''
        data = backend.fetch_details(query, (id,))
        uname = backend.fetch_details(
            'select uname from login_details where id=%s', (id,))[0][0]
        data.append(uname)
        return data

    def homeicon(self):
        try:
            self.frame2.place(x=10, y=130)
            self.frame3.place_forget()
            self.frame4.place_forget()
            self.frame5.place_forget()
            self.frame6.place_forget()
            self.frame7.place_forget()
        except:
            pass

    def variables_used(self):
        self.f_name = StringVar()
        self.m_name = StringVar()
        self.l_name = StringVar()
        self.email = StringVar()
        self.subject = StringVar()
        self.phoneno = IntVar()
        self.experi = IntVar()
        self.uname = StringVar()
        self.passw = StringVar()
        self.qualifi = StringVar()
        self.age = IntVar()
        self.id = StringVar()
        self.search = StringVar(value="Search Here")
        self.rollno = IntVar()
        self.father_name = StringVar()
        self.mother_name = StringVar()
        self.bloodg = StringVar()
        self.father_occ = StringVar()
        self.mother_occ = StringVar()

    def reset(self):
        try:
            self.f_name.set("")
            self.m_name.set("")
            self.l_name.set("")
            self.email.set("")
            self.father_occ.set("")
            self.mother_occ.set("")
            self.subject.set("")
            self.qualifi.set("")
            self.experi.set(0)
            self.uname.set("")
            self.passw.set("")
            self.phoneno.set(0)
            self.gender_box.set("")
            self.address_txt.delete(1.0, END)
            self.dob.set_date(datetime.date(datetime.now()))

            self.doa.set_date(datetime.date(datetime.now()))
            self.age.set(18)
            self.rollno.set(0)
            self.division_box.set("")
            self.father_name.set("")
            self.mother_name.set("")
            self.bloodg.set("")
            self.standard_box.set("")
            self.doj.set_date(datetime.date(datetime.now()))

        except Exception as ex:
            # print(ex)
            pass

    def reset1(self):
        try:
            self.first_name.set("")
            self.middle_name.set("")
            self.last_name.set("")
            self.fat_occ.set("")
            self.mot_occ.set("")
            self.username.set("")
            self.password.set("")
            self.phno.set(0)
            self.gender_box.set("")
            self.address_txt.delete(1.0, END)
            self.dob.set_date(datetime.date(datetime.now()))
            self.doa.set_date(datetime.date(datetime.now()))
            self.age.set(18)
            self.roool.set(0)
            self.division_box.set("")
            self.fat_name.set("")
            self.mot_name.set("")
            self.blog.set("")
            self.standard_box.set("")
            self.doj.set_date(datetime.date(datetime.now()))

        except Exception as ex:
            # print(ex)
            pass

    def add_faculty_into_data(self):
        if self.valid():
            val = (self.f_name.get(), self.m_name.get(), self.l_name.get(), self.experi.get(), self.doj.get_date(), self.dob.get_date(), self.email.get(
            ), self.subject.get(), self.address_txt.get(1.0, END), self.qualifi.get(), self.age_box.get(), self.gender_box.get(), self.phoneno.get())
            if backend.call_procedure('addfaculty', val):
                id = backend.fetch_details('select id from faculty where first_name=%s and middle_name=%s and last_name=%s and age=%s and sex=%s', (
                    self.f_name.get(), self.m_name.get(), self.l_name.get(), self.age_box.get(), self.gender_box.get()))[0][0]
                if backend.execute_query("insert into login_details values (%s,%s,sha(%s),'faculty');", (id, self.uname.get(), self.passw.get())):
                    mb.showinfo("Success", "Successfully Added the Faculty")
                    self.reset()
                else:
                    mb.showerror("Error", "Some Error Occured")
            else:
                mb.showerror('Error', "Some Error Occured")

    def valid(self):
        if self.l_name.get() == "" or self.f_name.get() == "" or self.m_name.get() == "" or self.uname.get() == "" or self.passw.get() == "" or self.address_txt.get(1.0, END) == "" or self.email.get() == "" or self.qualifi.get() == "" or self.subject.get() == "":
            mb.showerror(
                "Check", "Check that You have filled the correct Requirements")
            return False
        elif len(str(self.phoneno.get())) != 10 or self.phoneno.get() == "":
            mb.showerror("Error", "Enter The correct Phone Number")
            return False
        elif '@' not in self.email.get() or '.' not in self.email.get():
            mb.showerror("Error", "Please Enter The correct Email ID")
        else:
            return True

    def manage_faculty(self, frame, label_place):
        self.faculty(frame, label_place, 4)
        Label(self.frame4, text="ID : ", font=(
            "lucida", 16), bg="#84fa92").place(x=133, y=20)
        Label(self.frame4, text="Search by", font=(
            "lucida", 12, "bold"), bg="#84fa92").place(x=900, y=15)
        self.id_txt = Entry(self.frame4, textvariable=self.id, state="disabled", font=(
            "Times New Roman", 16), background="white", width=10, bd=2, relief="solid")
        self.id_txt.place(x=180, y=20)
        self.search_txt = Entry(self.frame4, textvariable=self.search, font=(
            "Times New Roman", 14), background="white", width=25, bd=2, relief="solid")
        self.search_txt.place(x=1020, y=40)
        Button(self.frame4, image=self.img_list[6], bg="#3903fc", relief="groove", bd=2,
               fg="white", activebackground="#027cd9", command=self.__search_entry).place(x=1255, y=30)
        self.table = Treeview(self.frame4, columns=[
                              "id", "Name", "Age", "a"], selectmode="browse", show="headings", height=10)
        self.table.place(x=900, y=70, height=500)
        self.table.heading("id", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("a", text="Gender")
        self.table.column("id", anchor="center", width=70)
        self.table.column("Name", anchor="center", width=210)
        self.table.column("Age", anchor="center", width=50)
        self.table.column("a", anchor="center", width=80)
        self.__insert_records()
        self.sc = Scrollbar(
            self.frame4, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=1315, y=70, height=500)
        self.table.bind("<<TreeviewSelect>>", self.filled_record)
        self.searchby_box = Combobox(self.frame4, background="white", values=(
            "All", "ID", "First Name", "Experience", "Subject", "Gender", "age"), font=("Times New Roman", 14), state="readonly", width=10)
        self.searchby_box.place(x=900, y=40)
        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))

    def __search_entry(self):
        if self.search.get() == "Search Here" or self.searchby_box.get() == "":
            mb.showwarning("Warning", "NO Results found")
        elif self.searchby_box.get() == "ID":
            self.__search_engine("id")
        elif self.searchby_box.get() == "First Name":
            self.__search_engine("first_name")
        elif self.searchby_box.get() == "All":
            for item in self.table.get_children():
                self.table.delete(item)
            self.__insert_records()
        elif self.searchby_box.get() == "Experience":
            self.__search_engine("experience")
        elif self.searchby_box.get() == "Subject":
            self.__search_engine("sub")
        elif self.searchby_box.get() == "Gender":
            self.__search_engine("sex")
        elif self.searchby_box.get() == "age":
            self.__search_engine("age")

    def __search_engine(self, column):
        if self.search.get() == "":
            mb.showwarning("warning", "No Record found")
        else:
            if column == "sex":
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),age,sex from faculty where {column} like "{self.search.get()}%";'''
            else:
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),age,sex from faculty where {column} like "%{self.search.get()}%";'''
            data = backend.fetch_details(query)
            if len(data) == 0:
                mb.showwarning("warning", "No Record found")
            else:
                for item in self.table.get_children():
                    self.table.delete(item)
                for d in data:
                    self.table.insert("", END, values=d)
                counter = Label(self.frame4, text=f"{len(data)} Records Found", font=(
                    "lucida", 12, "bold"), bg="#84fa92")
                counter.place(x=900, y=580)
                counter.after(10000, lambda: counter.place_forget())

    def update_faculty(self):
        if self.valid():
            query = '''update faculty set first_name=%s,middle_name=%s,last_name=%s,experience=%s,doj=%s,dob=%s,email=%s,sub=%s,address=%s,qualification=%s,age=%s,sex=%s,phoneno=%s where id=%s;'''
            val = (self.f_name.get(), self.m_name.get(), self.l_name.get(), self.experi.get(), self.doj.get_date(), self.dob.get_date(), self.email.get(
            ), self.subject.get(), self.address_txt.get(1.0, END), self.qualifi.get(), self.age_box.get(), self.gender_box.get(), self.phoneno.get(), self.id.get())
            if backend.execute_query(query, val):
                if backend.execute_query('update login_details set uname=%s,password=sha(%s) where id=%s', (self.uname.get(), self.passw.get(), self.id.get())):
                    mb.showinfo("Success", "Updated the Record Successfully")
                    for item in self.table.get_children():
                        self.table.delete(item)
                    self.__insert_records()
                    self.reset()
                    self.id.set("")
            else:
                mb.showerror("Error", "Some Error Occured")

    def delete_faculty(self):
        if self.id.get() == "":
            mb.showinfo("Information", "Please Select The One Record")
        else:
            a = mb.askyesnocancel(
                "Confirmation", f"You Want to delete the record of {self.f_name.get()}")
            if a:
                if backend.execute_query("delete from faculty where id=%s", (self.id.get(),)):
                    mb.showinfo('Success', "Record Deleted Successfully")
                    for item in self.table.get_children():
                        self.table.delete(item)
                    self.__insert_records()
                    self.reset()
                    self.id.set("")
                else:
                    mb.showerror("Error", "Some Error Occured")

    def __remove_frames(self, no):
        try:
            if no == 3:
                self.frame2.place_forget()
                self.frame4.place_forget()
                self.frame5.place_forget()
                self.frame6.place_forget()
                self.frame7.place_forget()

            elif no == 4:
                self.frame2.place_forget()
                self.frame3.place_forget()
                self.frame5.place_forget()
                self.frame6.place_forget()
                self.frame7.place_forget()

            elif no == 5:
                self.frame2.place_forget()
                self.frame3.place_forget()
                self.frame4.place_forget()
                self.frame6.place_forget()
                self.frame7.place_forget()

            elif no == 6:
                self.frame2.place_forget()
                self.frame3.place_forget()
                self.frame4.place_forget()
                self.frame5.place_forget()
                self.frame7.place_forget()

            elif no == 7:
                self.frame2.place_forget()
                self.frame3.place_forget()
                self.frame4.place_forget()
                self.frame5.place_forget()
                self.frame6.place_forget()

        except:
            pass

    def __insert_records(self):
        query = '''select id,concat_ws(" ",first_name,middle_name,last_name),age,sex from faculty order by id;'''
        for data in backend.fetch_details(query):
            self.table.insert("", END, values=data)

    def filled_record(self, e):
        # a=self.table.selection()[0]
        try:
            self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))
            id = self.table.item(self.table.selection()[0])["values"][0]
            self.address_txt.delete(1.0, END)
            data = backend.fetch_details(
                "select * from faculty where id=%s", (id,))[0]
            self.id.set(id)
            self.f_name.set(data[1])
            self.m_name.set(data[2])
            self.l_name.set(data[3])
            self.email.set(data[7])
            self.subject.set(data[8])
            self.qualifi.set(data[10])
            self.experi.set(data[4])
            self.phoneno.set(data[13])
            self.gender_box.set(data[12])
            self.address_txt.insert(1.0, data[9], END)
            self.dob.set_date(data[6])
            self.doj.set_date(data[5])
            self.age.set(data[11])
            login = backend.fetch_details(
                "select uname from login_details where id=%s;", (id,))[0][0]
            self.uname.set(login)
        except:
            pass

    def add_student(self, frame, framename, no):
        self.__remove_frames(no)
        frame.place(x=0, y=130)
        self.variables_used()
        if framename == "add":
            Label(frame, text="ADD STUDENT", font=("Verdana", 20,
                  "bold", "underline"), bg="#84fa92").place(x=600, y=10)
            Button(frame, text="Reset", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.reset).place(x=700, y=290)
            Button(frame, text="ADD", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.__add_student_intodata).place(x=540, y=290)
        elif framename == "manage":
            Button(frame, text="Update", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.update_student).place(x=700, y=290)
            Button(frame, text="Delete", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2, fg="white",
                   activebackground="#027cd9", width=9, height=1, command=self.delete_student).place(x=540, y=290)
            Label(frame, text="MANAGE STUDENT", font=("Verdana", 20,
                  "bold", "underline"), bg="#84fa92").place(x=570, y=10)
        Label(frame, text="First Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=50, y=60)
        Label(frame, text="Middle Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=32, y=100)
        Label(frame, text="Last Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=50, y=140)
        Label(frame, text="Date Of birth : ", font=(
            "lucida", 16), bg="#84fa92").place(x=30, y=180)
        Label(frame, text="Roll No : ", font=(
            "lucida", 16), bg="#84fa92").place(x=83, y=220)
        Label(frame, text="Division : ", font=(
            "lucida", 16), bg="#84fa92").place(x=76, y=260)
        Label(frame, text="Blood Group : ", font=(
            "lucida", 16), bg="#84fa92").place(x=35, y=300)
        Label(frame, text="Address : ", font=(
            "lucida", 16), bg="#84fa92").place(x=72, y=340)
        Label(frame, text="Father Occupation : ", font=(
            "lucida", 16), bg="#84fa92").place(x=0, y=410)
        Label(frame, text="Gender : ", font=("lucida", 16),
              bg="#84fa92").place(x=75, y=450)
        Label(frame, text="Date Of Admission : ", font=(
            "lucida", 16), bg="#84fa92").place(x=0, y=490)
        Label(frame, text="Mother Occupation : ", font=(
            "lucida", 16), bg="#84fa92").place(x=0, y=530)
        Label(frame, text="Father Phone No.: ", font=(
            "lucida", 16), bg="#84fa92").place(x=15, y=570)
        Label(frame, text="Father Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=520, y=60)
        Label(frame, text="Mother Name : ", font=(
            "lucida", 16), bg="#84fa92").place(x=515, y=100)
        Label(frame, text="Standard : ", font=(
            "lucida", 16), bg="#84fa92").place(x=555, y=140)
        Label(frame, text="Username : ", font=(
            "lucida", 16), bg="#84fa92").place(x=545, y=180)
        Label(frame, text="Password : ", font=(
            "lucida", 16), bg="#84fa92").place(x=545, y=220)
        values = []
        for i in range(1, 11):
            values.append(i)
        # first name entry
        self.f_name_txt = Entry(self.frame5, textvariable=self.f_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.f_name_txt.place(x=180, y=60)
        # middle name entry
        self.m_name_txt = Entry(self.frame5, textvariable=self.m_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.m_name_txt.place(x=180, y=100)
        # last name entry
        self.l_name_txt = Entry(self.frame5, textvariable=self.l_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.l_name_txt.place(x=180, y=140)
        # father occ entry box
        self.father_occ_txt = Entry(self.frame5, textvariable=self.father_occ, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.father_occ_txt.place(x=200, y=410)
        # mother occ entry box
        self.mother_occ_txt = Entry(self.frame5, textvariable=self.mother_occ, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.mother_occ_txt.place(x=200, y=530)
        # date of birth entry
        self.dob = DateEntry(frame, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.dob.place(x=180, y=180)
        # date of admission
        self.doa = DateEntry(frame, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.doa.place(x=200, y=490)
        # rolln0 entry
        self.rollno_txt = Entry(self.frame5, textvariable=self.rollno, font=(
            "Times New Roman", 16), background="white", width=8, bd=2, relief="solid")
        self.rollno_txt.place(x=180, y=220)
        # bloodgroup entry
        self.bloodg_txt = Entry(self.frame5, textvariable=self.bloodg, font=(
            "Times New Roman", 16), background="white", width=8, bd=2, relief="solid")
        self.bloodg_txt.place(x=180, y=300)
        # phone entry
        self.phone_txt = Entry(self.frame5, textvariable=self.phoneno, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.phone_txt.place(x=200, y=570)
        # Father Name entry
        self.father_name_txt = Entry(self.frame5, textvariable=self.father_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.father_name_txt.place(x=665, y=60)
        # gender box
        self.gender_box = Combobox(frame, background="white", values=(
            "Male", "Female", "Other"), font=("Times New Roman", 16), state="readonly", width=10)
        self.gender_box.place(x=180, y=450)
        # divsion box
        self.division_box = Combobox(frame, background="white", values=(
            "A", "B", "C", "D"), font=("Times New Roman", 16), state="readonly", width=4)
        self.division_box.place(x=180, y=260)
        # standard box
        self.standard_box = Combobox(frame, background="white", values=values, font=(
            "Times New Roman", 16), state="readonly", width=4)
        self.standard_box.place(x=665, y=140)
        # creating the address txt
        self.address_txt = Text(frame, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), height=3, width=37)
        self.address_txt.place(x=180, y=340)
        # creating the mother name txt
        self.mother_name_txt = Entry(self.frame5, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), width=20, textvariable=self.mother_name)
        self.mother_name_txt.place(x=665, y=100)
        # username entry
        self.uname_txt = Entry(self.frame5, textvariable=self.uname, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.uname_txt.place(x=665, y=180)
        # password entry
        self.pass_txt = Entry(self.frame5, font=("Times New Roman", 16),
                              textvariable=self.passw, background="white", width=20, bd=2, relief="solid")
        self.pass_txt.place(x=665, y=220)

    def __add_student_intodata(self):
        if self.valid1():
            val = (self.f_name.get(), self.m_name.get(), self.l_name.get(), self.rollno.get(), self.division_box.get(), self.address_txt.get(1.0, END), self.phoneno.get(), self.father_name.get(
            ), self.mother_name.get(), self.standard_box.get(), self.dob.get_date(), self.bloodg.get(), self.doa.get_date(), self.father_occ.get(), self.mother_occ.get(), self.gender_box.get())
            if backend.call_procedure('addstudent', val):
                id = backend.fetch_details('select id from student where first_name=%s and middle_name=%s and last_name=%s;', (
                    self.f_name.get(), self.m_name.get(), self.l_name.get()))[0][0]
                if backend.execute_query("insert into login_details values (%s,%s,sha(%s),'student');", (id, self.uname.get(), self.passw.get())):
                    mb.showinfo("Success", "Successfully Added the record")
                    self.reset()
            else:
                mb.showerror("Error", "Some Errored Occured")

    def valid1(self):
        if self.l_name.get() == "" or self.f_name.get() == "" or self.m_name.get() == "" or self.uname.get() == "" or self.passw.get() == "" or self.address_txt.get(1.0, END) == "" or self.father_name.get() == "" or self.mother_name.get() == "" or self.father_occ.get() == "" or self.mother_occ.get() == "" or self.bloodg.get() == "" or self.division_box.get() == "" or self.rollno.get() == "" or self.uname.get() == "" or self.passw.get() == "":
            mb.showerror(
                "Check", "Check that You have filled the correct Requirements")
        elif len(str(self.phoneno.get())) != 10 or self.phoneno.get() == "":
            mb.showerror("Error", "Enter The correct Phone Number")
        else:
            return True

    def valid2(self):
        if self.last_name.get() == "" or self.first_name.get() == "" or self.middle_name.get() == "" or self.username.get() == "" or self.password.get() == "" or self.address_txt.get(1.0, END) == "" or self.fat_name.get() == "" or self.mot_name.get() == "" or self.fat_occ.get() == "" or self.mot_occ.get() == "" or self.blog.get() == "" or self.division_box.get() == "" or self.roool.get() == "":
            mb.showerror(
                "Check", "Check that You have filled the correct Requirements")
        elif len(str(self.phno.get())) != 10 or self.phno.get() == "":
            mb.showerror("Error", "Enter The correct Phone Number")
        else:
            return True

    def manage_student(self, frame):

        self.add_student(frame, "manage", 6)
        # variables
        self.id1 = StringVar()
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.middle_name = StringVar()
        self.fat_occ = StringVar()
        self.mot_occ = StringVar()
        self.roool = IntVar()
        self.blog = StringVar()
        self.phno = IntVar()
        self.fat_name = StringVar()
        self.mot_name = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        # first name entry
        self.f_name_txt = Entry(self.frame6, textvariable=self.first_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.f_name_txt.place(x=180, y=60)
        # middle name entry
        self.m_name_txt = Entry(self.frame6, textvariable=self.middle_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.m_name_txt.place(x=180, y=100)
        # last name entry
        self.l_name_txt = Entry(self.frame6, textvariable=self.last_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.l_name_txt.place(x=180, y=140)
        # father occ entry box
        self.father_occ_txt = Entry(self.frame6, textvariable=self.fat_occ, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.father_occ_txt.place(x=200, y=410)
        # mother occ entry box
        self.mother_occ_txt = Entry(self.frame6, textvariable=self.mot_occ, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.mother_occ_txt.place(x=200, y=530)
        self.rollno_txt = Entry(self.frame6, textvariable=self.roool, font=(
            "Times New Roman", 16), background="white", width=8, bd=2, relief="solid")
        self.rollno_txt.place(x=180, y=220)
        # bloodgroup entry
        self.bloodg_txt = Entry(self.frame6, textvariable=self.blog, font=(
            "Times New Roman", 16), background="white", width=8, bd=2, relief="solid")
        self.bloodg_txt.place(x=180, y=300)
        # phone entry
        self.phone_txt = Entry(self.frame6, textvariable=self.phno, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.phone_txt.place(x=200, y=570)
        # Father Name entry
        self.father_name_txt = Entry(self.frame6, textvariable=self.fat_name, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.father_name_txt.place(x=665, y=60)
        # creating the mother name txt
        self.mother_name_txt = Entry(self.frame6, bd=2, relief="solid", bg="white", font=(
            "Times New Roman", 14), width=20, textvariable=self.mot_name)
        self.mother_name_txt.place(x=665, y=100)
        # username entry
        self.uname_txt = Entry(self.frame6, textvariable=self.username, font=(
            "Times New Roman", 16), background="white", width=20, bd=2, relief="solid")
        self.uname_txt.place(x=665, y=180)
        # password entry
        self.pass_txt = Entry(self.frame6, font=("Times New Roman", 16),
                              textvariable=self.password, background="white", width=20, bd=2, relief="solid")
        self.pass_txt.place(x=665, y=220)

        Label(self.frame6, text="ID : ", font=(
            "lucida", 16), bg="#84fa92").place(x=133, y=20)

        self.id_txt = Entry(self.frame6, textvariable=self.id1, state="disabled", font=(
            "Times New Roman", 16), background="white", width=10, bd=2, relief="solid")
        self.id_txt.place(x=180, y=20)
        Label(self.frame6, text="Search by", font=(
            "lucida", 12, "bold"), bg="#84fa92").place(x=900, y=15)
        self.search_txt = Entry(self.frame6, textvariable=self.search, font=(
            "Times New Roman", 14), background="white", width=25, bd=2, relief="solid")
        self.search_txt.place(x=1020, y=40)
        Button(self.frame6, image=self.img_list[6], bg="#3903fc", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", command=self.__search_entryforstudent).place(x=1255, y=30)
        self.table = Treeview(self.frame6, columns=[
                              "id", "Name", "roll", "std", "div"], selectmode="browse", show="headings", height=10)
        self.table.place(x=900, y=70, height=500)
        self.table.heading("id", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("roll", text="Roll No")
        self.table.heading("std", text="Std")
        self.table.heading("div", text="Divison")
        self.table.column("id", anchor="center", width=70)
        self.table.column("Name", anchor="center", width=190)
        self.table.column("roll", anchor="center", width=60)
        self.table.column("std", anchor="center", width=50)
        self.table.column("div", anchor="center", width=60)

        self.__insert_record_student()
        self.sc = Scrollbar(
            self.frame6, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=1340, y=70, height=500)
        self.searchby_box = Combobox(self.frame6, background="white", values=(
            "All", "ID", "First Name", "Standard", "Division", "Gender"), font=("Times New Roman", 14), state="readonly", width=10)
        self.searchby_box.place(x=900, y=40)
        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))
        self.table.bind("<<TreeviewSelect>>", self.filled_record_st)

    def __fees_insert_record(self, e):
        self.name = StringVar()
        self.__month_box_reset()
        self.win.update()
        self.id_s = self.table.item(self.table.selection()[0])["values"][0]
        name = backend.fetch_details(
            'select concat_ws(" ",first_name,middle_name,last_name) from student where id=%s', (self.id_s,))[0][0]
        Label(self.frame7, text=f"ID : {self.id_s}", font=(
            "lucida", 14), bg="#84fa92").place(x=350, y=60)
        Label(self.frame7, text=f"Name : ", font=(
            "lucida", 14), bg="#84fa92").place(x=350, y=90)
        self.name_txt = Entry(self.frame7, textvariable=self.name, font=(
            "Times New Roman", 14), state="readonly", background="#84fa92", bg="#84fa92", width=25)
        self.name_txt.place(x=420, y=90)
        self.name.set(name)
        Label(self.frame7, text=f"View Record By Year ", font=(
            "lucida", 10), bg="#84fa92").place(x=350, y=120)
        data = backend.fetch_details(
            'select * from fees where id=%s', (self.id_s,))
        yearlist = []
        for y in data:
            yearlist.append(y[2])
        self.year_box = Combobox(self.frame7, background="white", values=yearlist, font=(
            "Times New Roman", 14), state="readonly", width=6)
        self.year_box.place(x=350, y=140)
        self.year_box.bind("<<ComboboxSelected>>",
                           lambda e: self.__fees_by_year(self.id_s))
        self.year_f = IntVar()
        self.year_txt = Entry(self.frame7, textvariable=self.year_f, font=(
            "Times New Roman", 14), background="white", width=10, bd=2, relief="solid")
        self.year_txt.place(x=350, y=170)
        Button(self.frame7, text="ADD Record For\nYear", font=("Verdana", 10), bg="#3903fc", relief="groove",
               bd=2, fg="white", activebackground="#027cd9", command=self.__add_year).place(x=450, y=170)

    def __add_year(self):
        if self.year_f.get() == "" or self.year_f.get() == 0 or self.year_f.get() < 1950:
            mb.showwarning("Warning", "Enter the correct Date")
        else:
            if backend.call_procedure('add_fees', (self.id_s, self.year_f.get())):
                mb.showinfo("Success", "Successfully added the record")
            else:
                mb.showinfo(
                    "Error", "Please Check That if you have enter the year in store fees")

    def __fees_by_year(self, id):
        self.Mfees_details = ""
        self.Yfees_details = ""
        self.win.update()
        data = backend.fetch_details(
            'select * from fees where id=%s and year_=%s;', (id, self.year_box.get()))[0]
        data = list(data)
        for i in range(len(data)):
            if data[i] == "N":
                data[i] = "No"
            elif data[i] == "Y":
                data[i] = "Yes"
        self.full_box.set(data[1])
        self.jan_box.set(data[3])
        self.feb_box.set(data[4])
        self.mar_box.set(data[5])
        self.aprl_box.set(data[6])
        self.may_box.set(data[7])
        self.june_box.set(data[8])
        self.july_box.set(data[9])
        self.aug_box.set(data[10])
        self.sept_box.set(data[11])
        self.oct_box.set(data[12])
        self.nov_box.set(data[13])
        self.dec_box.set(data[14])
        self.win.update()
        f_details = backend.fetch_details(
            'select * from store_fees where year_=%s;', (self.year_box.get(),))[0]
        Label(self.frame7, text=f"{self.year_box.get()} Details", font=(
            "lucida", 16, "underline"), bg="#84fa92").place(x=450, y=230)
        self.Mfees_details = f_details[1]
        self.Yfees_details = f_details[2]
        self.month_f_label = Label(
            self.frame7, text=f"Monthly Fees : {self.Mfees_details}", font=("lucida", 14), bg="#84fa92")
        self.month_f_label.place(x=430, y=280)
        self.year_f_label = Label(
            self.frame7, text=f"Year Fees : {self.Yfees_details}", font=("lucida", 14), bg="#84fa92")
        self.year_f_label.place(x=430, y=310)
        self.win.update()

    def __month_box_reset(self):
        self.Mfees_details = ""
        self.Yfees_details = ""
        self.full_box.set("")
        self.jan_box.set("")
        self.feb_box.set("")
        self.mar_box.set("")
        self.aprl_box.set("")
        self.may_box.set("")
        self.june_box.set("")
        self.july_box.set("")
        self.aug_box.set("")
        self.sept_box.set("")
        self.oct_box.set("")
        self.nov_box.set("")
        self.dec_box.set("")

    def __insert_record_student(self):
        query = '''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division from student order by id;'''
        for data in backend.fetch_details(query):
            self.table.insert("", END, values=data)

    def filled_record_st(self, e):

        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))
        try:
            id = self.table.item(self.table.selection()[0])["values"][0]
        except IndexError:
            pass
        self.address_txt.delete(1.0, END)
        try:
            data = backend.fetch_details(
                "select * from student where id=%s", (id,))[0]
            self.variables_used()
            self.id1.set(id)
            self.first_name.set(data[1])
            self.middle_name.set(data[2])
            self.last_name.set(data[3])
            self.roool.set(data[4])
            self.division_box.set(data[5])
            self.address_txt.insert(1.0, data[6], END)
            self.fat_name.set(data[7])
            self.mot_name.set(data[8])
            self.standard_box.set(data[9])
            self.dob.set_date(data[10])
            self.blog.set(data[11])
            self.doa.set_date(data[12])
            self.fat_occ.set(data[13])
            self.mot_occ.set(data[14])
            self.phno.set(data[15])
            self.gender_box.set(data[16])
            login = backend.fetch_details(
                "select uname from login_details where id=%s;", (id,))[0][0]
            self.username.set(login)
        except UnboundLocalError:
            pass

    def update_student(self):
        if self.valid2():
            query = '''update student set first_name=%s,middle_name=%s,last_name=%s,roll_no=%s,division=%s,address=%s,father_name=%s,mother_name=%s,std=%s,dob=%s,bloodgroup=%s,doa=%s,father_occ=%s,mother_occ=%s,father_phoneno=%s,sex=%s where id=%s'''
            val = (self.first_name.get(), self.middle_name.get(), self.last_name.get(), self.roool.get(), self.division_box.get(), self.address_txt.get(1.0, END), self.fat_name.get(), self.mot_name.get(
            ), self.standard_box.get(), self.dob.get_date(), self.blog.get(), self.doa.get_date(), self.fat_occ.get(), self.mot_occ.get(), self.phno.get(), self.gender_box.get(), self.id1.get())
            if backend.execute_query(query, val):
                if backend.execute_query('update login_details set uname=%s,password=sha(%s) where id=%s', (self.username.get(), self.password.get(), self.id1.get())):
                    mb.showinfo("Success", "Updated the Record")
                    for item in self.table.get_children():
                        self.table.delete(item)
                    self.__insert_record_student()
                    self.reset1()
                    self.id1.set("")
            else:
                mb.showerror("Error", "some Error Occured")

    def delete_student(self):
        if self.id1.get() == "":
            mb.showinfo("Information", "Please Select The One Record")
        else:
            a = mb.askyesnocancel(
                "Confirmation", f"You Want to delete the record of {self.first_name.get()}")
            if a:
                if backend.execute_query("delete from student where id=%s", (self.id1.get(),)):
                    mb.showinfo('Success', "Record Deleted Successfully")
                    for item in self.table.get_children():
                        self.table.delete(item)
                    self.__insert_record_student()
                    self.reset()
                    self.id.set("")
                else:
                    mb.showerror("Error", "Some Error Occured")

    def __search_entryforstudent(self):
        if self.search.get() == "Search Here" or self.searchby_box.get() == "":
            mb.showwarning("Warning", "NO Results found")
        elif self.searchby_box.get() == "ID":
            self.__search_engine_for_student("id")
        elif self.searchby_box.get() == "First Name":
            self.__search_engine_for_student("first_name")
        elif self.searchby_box.get() == "All":
            for item in self.table.get_children():
                self.table.delete(item)
            self.__insert_record_student()
        elif self.searchby_box.get() == "Standard":
            self.__search_engine_for_student("std")
        elif self.searchby_box.get() == "Division":
            self.__search_engine_for_student("division")
        elif self.searchby_box.get() == "Gender":
            self.__search_engine_for_student("sex")

    def __search_engine_for_student(self, column):
        if self.search.get() == "":
            mb.showwarning("warning", "No Record found")
        else:
            if column == "sex":
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division from student where {column} like "{self.search.get()}%";'''
            else:
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division from student where {column} like "%{self.search.get()}%";'''
            data = backend.fetch_details(query)
            if len(data) == 0:
                mb.showwarning("warning", "No Record found")
            else:
                for item in self.table.get_children():
                    self.table.delete(item)
                for d in data:
                    self.table.insert("", END, values=d)
                counter = Label(self.frame6, text=f"{len(data)} Records Found", font=(
                    "lucida", 12, "bold"), bg="#84fa92")
                counter.place(x=900, y=580)
                counter.after(10000, lambda: counter.place_forget())

    def __fees_frame(self):
        self.frame7.place(x=0, y=130)
        Label(self.frame7, text="Search by", font=(
            "lucida", 12, "bold"), bg="#84fa92").place(x=900, y=15)
        self.variables_used()
        self.search_txt = Entry(self.frame7, textvariable=self.search, font=(
            "Times New Roman", 14), background="white", width=25, bd=2, relief="solid")
        self.search_txt.place(x=1020, y=40)
        Button(self.frame7, image=self.img_list[6], bg="#3903fc", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", command=self.__search_entryforstudent).place(x=1255, y=30)
        self.table = Treeview(self.frame7, columns=[
                              "id", "Name", "roll", "std", "div"], selectmode="browse", show="headings", height=10)
        self.table.place(x=900, y=70, height=500)
        self.table.heading("id", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("roll", text="Roll No")
        self.table.heading("std", text="Std")
        self.table.heading("div", text="Divison")
        self.table.column("id", anchor="center", width=70)
        self.table.column("Name", anchor="center", width=190)
        self.table.column("roll", anchor="center", width=60)
        self.table.column("std", anchor="center", width=50)
        self.table.column("div", anchor="center", width=60)
        self.__insert_record_student()
        self.sc = Scrollbar(
            self.frame7, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=1340, y=70, height=500)
        self.table.bind("<<TreeviewSelect>>", self.__fees_insert_record)
        self.searchby_box = Combobox(self.frame7, background="white", values=(
            "All", "ID", "First Name", "Standard", "Division", "Gender"), font=("Times New Roman", 14), state="readonly", width=10)
        self.searchby_box.place(x=900, y=40)
        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))
        Label(self.frame7, text="FEES DETAILS", font=("Verdana", 20,
              "bold", "underline"), bg="#84fa92").place(x=350, y=10)
        Button(self.frame7, text="FEES Delete/Update", font=("Verdana", 16), bg="#3903fc", relief="groove",
               bd=2, fg="white", activebackground="#027cd9", command=lambda: fees.Fees(self.win)).place(x=20, y=80)
        Button(self.frame7, text="Update", font=("Verdana", 16), bg="#3903fc", relief="groove", bd=2,
               fg="white", activebackground="#027cd9", command=self.update_fees).place(x=300, y=540)
        monthlist = ["January : ", "February : ", "March : ", "April : ", "May : ", "June : ",
                     "July : ", "August : ", "September : ", "October : ", "November : ", "December : "]
        Label(self.frame7, text=monthlist[0], font=(
            "lucida", 13), bg="#84fa92").place(x=40, y=130)
        Label(self.frame7, text=monthlist[1], font=(
            "lucida", 13), bg="#84fa92").place(x=33, y=160)
        Label(self.frame7, text=monthlist[2], font=(
            "lucida", 13), bg="#84fa92").place(x=53, y=190)
        Label(self.frame7, text=monthlist[3], font=(
            "lucida", 13), bg="#84fa92").place(x=65, y=220)
        Label(self.frame7, text=monthlist[4], font=(
            "lucida", 13), bg="#84fa92").place(x=67, y=250)
        Label(self.frame7, text=monthlist[5], font=(
            "lucida", 13), bg="#84fa92").place(x=60, y=280)
        Label(self.frame7, text=monthlist[6], font=(
            "lucida", 13), bg="#84fa92").place(x=65, y=310)
        Label(self.frame7, text=monthlist[7], font=(
            "lucida", 13), bg="#84fa92").place(x=45, y=340)
        Label(self.frame7, text=monthlist[8], font=(
            "lucida", 13), bg="#84fa92").place(x=15, y=370)
        Label(self.frame7, text=monthlist[9], font=(
            "lucida", 13), bg="#84fa92").place(x=36, y=400)
        Label(self.frame7, text=monthlist[10], font=(
            "lucida", 13), bg="#84fa92").place(x=20, y=430)
        Label(self.frame7, text=monthlist[11], font=(
            "lucida", 13), bg="#84fa92").place(x=18, y=460)
        Label(self.frame7, text="Full Year : ", font=(
            "lucida", 13), bg="#84fa92").place(x=28, y=490)
        self.jan_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.jan_box.place(x=125, y=130)
        self.feb_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.feb_box.place(x=125, y=160)
        self.mar_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.mar_box.place(x=125, y=190)
        self.aprl_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.aprl_box.place(x=125, y=220)
        self.may_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.may_box.place(x=125, y=250)
        self.june_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.june_box.place(x=125, y=280)
        self.july_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.july_box.place(x=125, y=310)
        self.aug_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.aug_box.place(x=125, y=340)
        self.sept_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.sept_box.place(x=125, y=370)
        self.oct_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.oct_box.place(x=125, y=400)
        self.nov_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.nov_box.place(x=125, y=430)
        self.dec_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.dec_box.place(x=125, y=460)
        self.full_box = Combobox(self.frame7, background="white", values=(
            "Yes", "No"), font=("Times New Roman", 13), state="readonly", width=3)
        self.full_box.place(x=125, y=490)

    def update_fees(self):
        if self.full_box.get() == "":
            mb.showwarning("Warning", "Please Select One Record")
        else:
            arg = [self.full_box.get(), self.jan_box.get(), self.feb_box.get(), self.mar_box.get(), self.aprl_box.get(), self.may_box.get(
            ), self.june_box.get(), self.july_box.get(), self.aug_box.get(), self.sept_box.get(), self.oct_box.get(), self.nov_box.get(), self.dec_box.get()]
            for i in range(len(arg)):
                if arg[i] == "No":
                    arg[i] = "N"
                elif arg[i] == "Yes":
                    arg[i] = "Y"

            arg.append(self.id_s)
            arg.append(self.year_box.get())
            query = '''update fees set fullyearpaid=%s,jan=%s,feb=%s,mar=%s,april=%s,may=%s,june=%s,july=%s,aug=%s,sept=%s,oct=%s,nov=%s,dece=%s where id=%s and year_=%s'''
            if backend.execute_query(query, arg):
                mb.showinfo("Success", "Successfully Updated the Record")
            else:
                mb.showerror("Error", "Some Error Occured")
