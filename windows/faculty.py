from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox, Treeview
from windows import login_win, backend
from tkcalendar import DateEntry


class Faculty:
    def __init__(self, win, img_list, user):
        self.win = win
        self.usertuple = user
        self.img_list = img_list
        self.__gui()

    def __gui(self):
        # main frame of the faculty
        self.frame1 = Frame(self.win, width=1400,
                            height=790, background="#D671FD")
        self.frame1.place(x=0, y=0)
        # menu frame of the faculty
        self.frame2 = Frame(self.frame1, width=250,
                            height=790, background="#0042FF", bd=3, relief="solid")
        self.frame2.place(x=0, y=0)
        # home frame of the faculty
        self.frame3 = Frame(self.frame1, width=1130,
                            height=790, background="#D671FD")
        # class teacher frame
        self.frame4 = Frame(self.frame1, width=1130,
                            height=790, background="#D671FD")
        # student details frame
        self.frame5 = Frame(self.frame1, width=1130,
                            height=790, background="#D671FD")
        # admission frame
        self.frame6 = Frame(self.frame1, width=1130,
                            height=790, background="#D671FD")
        Label(self.frame2, image=self.img_list[7], bg="#0042FF").place(
            x=20, y=10)
        self.home()
        Label(self.frame2, text=f"Welcome,\n{self.usertuple[1]}", font=(
            "Verdana", 13, "bold"), bg="#0042FF", fg="white").place(x=50, y=220)
        Button(self.frame2, text="HOME", bg="#42FF00", foreground="white", font=("Verdana", 16, "bold"), relief="solid",
               bd=3, fg="black", activebackground="#CB00FF", width=14, command=self.home).place(x=10, y=300, height=60)
        Button(self.frame2, text="Attendance", bg="#42FF00", foreground="white", font=("Verdana", 16, "bold"), relief="solid",
               bd=3, fg="black", activebackground="#CB00FF", width=14, command=self.attendance_frame).place(x=10, y=380, height=60)
        Button(self.frame2, text="Student Details", bg="#42FF00", foreground="white", font=("Verdana", 16, "bold"), relief="solid",
               bd=3, fg="black", activebackground="#CB00FF", width=14, command=self.student_details_frame).place(x=10, y=460, height=60)
        Button(self.frame2, text="Class Teacher", bg="#42FF00", foreground="white", font=("Verdana", 16, "bold"), relief="solid",
               bd=3, fg="black", activebackground="#CB00FF", width=14, command=self.assign_ct).place(x=10, y=540, height=60)
        Button(self.frame2, text="Logout", bg="#42FF00", foreground="white", font=("Verdana", 16, "bold"), relief="solid",
               bd=3, fg="black", activebackground="#CB00FF", width=14, command=self.logout).place(x=10, y=620, height=60)

    def logout(self):
        a = mb.askyesno("Confirmation", "Are You Sure, You want to logout ?")
        if a:
            mb.showinfo("Done", "Successfully Logout !")
            login_win.login(self.win, self.img_list)

    def home(self):
        self.__remove_frames(3)
        self.frame3.place(x=260, y=10)
        data = self.get_faculty_details()

        Label(self.frame3, text="PROFILE", font=("Verdana", 26,
              "bold", "underline"), bg="#D671FD").place(x=500, y=10)
        Label(self.frame3, text=f"ID : {data[0][0]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=115, y=70)
        Label(self.frame3, text=f"First Name : {data[0][1]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=23, y=110)
        Label(self.frame3, text=f"Middle Name : {data[0][2]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=0, y=150)
        Label(self.frame3, text=f"Last Name : {data[0][3]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=23, y=190)
        Label(self.frame3, text=f"Email : {data[0][7]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=78, y=230)
        Label(self.frame3, text=f"Qualification : {data[0][10]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=5, y=270)
        Label(self.frame3, text=f"Subject : {data[0][8]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=56, y=310)
        Label(self.frame3, text=f"Gender : {data[0][12]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=58, y=350)
        Label(self.frame3, text=f"Phone No : {data[0][13]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=34, y=390)
        Label(self.frame3, text=f"Experience : {data[0][4]} Years", font=(
            "Verdana", 16), bg="#D671FD").place(x=18, y=430)
        Label(self.frame3, text=f"Date Of Joining : {data[0][5]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=0, y=470)
        Label(self.frame3, text=f"Birth Date : {data[0][6]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=25, y=510)
        Label(self.frame3, text=f"Address : {data[0][9]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=48, y=550)
        Label(self.frame3, text=f"Username : {data[1]}", font=(
            "Verdana", 16), bg="#D671FD").place(x=26, y=590)

    def get_faculty_details(self):
        data = backend.fetch_details(
            'select * from faculty where id=%s', (self.usertuple[0],))
        uname = backend.fetch_details(
            'select uname from login_details where id=%s', (self.usertuple[0],))[0][0]
        data.append(uname)
        div_details = backend.fetch_details(
            'select * from div_details where faculty_id=%s', (self.usertuple[0],))
        if len(div_details) == 0:
            data.append([])
        else:
            data.append(div_details[0])
            Label(self.frame3, text=f"Divison : {div_details[0][1]}", font=(
                "Verdana", 16), bg="#D671FD").place(x=650, y=140)
            Label(self.frame3, text=f"Standard : {div_details[0][0]}", font=(
                "Verdana", 16), bg="#D671FD").place(x=630, y=180)
            Label(self.frame3, text="Class Teacher of :", font=(
                "Verdana", 16, "bold"), bg="#D671FD").place(x=640, y=100)
        return data

    def assign_ct(self):
        self.__remove_frames(4)
        self.frame4.place(x=260, y=10)
        data = self.get_faculty_details()
        Label(self.frame4, text="Assign Class Teacher", font=(
            "Verdana", 26, "bold", "underline"), bg="#D671FD").place(x=400, y=10)
        if len(data[2]) == 0:
            self.label = "not"
            Label(self.frame4, text="You are not a class teacher ", font=(
                "Verdana", 16, "bold"), bg="#D671FD").place(x=40, y=80)
        else:
            self.label = "current"
            Label(self.frame4, text=f"Divison : {data[2][1]}", font=(
                "Verdana", 16), bg="#D671FD").place(x=40, y=120)
            Label(self.frame4, text=f"Standard : {data[2][0]}", font=(
                "Verdana", 16), bg="#D671FD", width=14, justify="left").place(x=40, y=160)
            Label(self.frame4, text="Currently Class Teacher of :", font=(
                "Verdana", 16, "bold"), bg="#D671FD").place(x=40, y=80)
        if self.label == "not":
            Button(self.frame4, text="Assign", bg="#03fcd7", foreground="white", font=("Verdana", 16, "bold"), relief="ridge", bd=3, fg="black",
                   activebackground="#CB00FF", width=14, activeforeground="white", command=self.assign_ct_frame).place(x=20, y=210, height=50)
        elif self.label == "current":
            Button(self.frame4, text="Update", bg="#03fcd7", foreground="white", font=("Verdana", 16, "bold"), relief="ridge", bd=3, fg="black",
                   activebackground="#CB00FF", width=14, activeforeground="white", command=self.assign_ct_frame).place(x=20, y=210, height=50)
        try:
            self.assign_ctf.place_forget()
        except:
            pass

    def assign_ct_frame(self):
        self.assign_ctf = Label(
            self.frame4, bg="#D671FD", width=100, height=80)
        self.assign_ctf.place(x=40, y=260)
        Label(self.assign_ctf, text="Select Divison :", font=(
            "Verdana", 12), bg="#D671FD").place(x=10, y=20)
        Label(self.assign_ctf, text="Select Standard :", font=(
            "Verdana", 12), bg="#D671FD").place(x=150, y=20)
        self.div_box = Combobox(self.assign_ctf, background="white", values=(
            "A", "B", "C", "D"), font=("Times New Roman", 14), state="readonly", width=6)
        self.div_box.place(x=10, y=50)
        list = []
        for i in range(1, 11):
            list.append(i)
        self.std_box = Combobox(self.assign_ctf, background="white", values=list, font=(
            "Times New Roman", 14), state="readonly", width=6)
        self.std_box.place(x=150, y=50)
        if self.label == "not":
            Button(self.assign_ctf, text="ADD", bg="#03fcd7", foreground="white", font=("Verdana", 14), relief="ridge", bd=3, fg="black",
                   activebackground="#CB00FF", width=14, activeforeground="white", command=self.get_div_faculty_details).place(x=300, y=40)
        elif self.label == "current":
            Button(self.assign_ctf, text="Update", bg="#03fcd7", foreground="white", font=("Verdana", 14), relief="ridge", bd=3, fg="black",
                   activebackground="#CB00FF", width=14, activeforeground="white", command=self.get_div_faculty_details).place(x=300, y=40)

    def get_div_faculty_details(self):
        if self.div_box.get() == "" or self.std_box.get() == "":
            mb.showwarning("Error", "Please select The standard or divison")
        else:
            id = self.usertuple[0]
            data = backend.fetch_details(
                'select * from div_details where std=%s and divison=%s', (self.std_box.get(), self.div_box.get()))
            if len(data) != 0:
                mb.showerror(
                    "Warning", "The class teacher has been already assigned for the selected std and divison")
            else:
                if self.label == "not":
                    if backend.execute_query('insert into div_details values (%s,%s,%s);', (self.std_box.get(), self.div_box.get(), id)):
                        mb.showinfo(
                            "success", "the class teacher has been assigned please refresh the screen")
                        self.assign_ct()
                    else:
                        mb.showerror("Error", "some error Occured")
                elif self.label == "current":
                    if backend.execute_query('update div_details set divison=%s,std=%s where faculty_id=%s;', (self.div_box.get(), self.std_box.get(), id)):
                        mb.showinfo("success", "Updated the Class Teacher")
                        self.assign_ct()
                    else:
                        mb.showerror("Error", "some error Occured")

    def __remove_frames(self, no):
        try:
            if no == 3:
                self.frame4.place_forget()
                self.frame5.place_forget()
                self.frame6.place_forget()

            elif no == 4:
                self.frame3.place_forget()
                self.frame5.place_forget()
                self.frame6.place_forget()

            elif no == 5:
                self.frame4.place_forget()
                self.frame3.place_forget()
                self.frame6.place_forget()

            elif no == 6:
                self.frame4.place_forget()
                self.frame3.place_forget()
                self.frame5.place_forget()

        except Exception as ex:
            print(ex)
            pass

    def student_details_frame(self):
        self.__remove_frames(5)
        self.frame5.place(x=260, y=10)
        self.search = StringVar(value="Search Here")
        Label(self.frame5, text="Search by", font=(
            "lucida", 12, "bold"), bg="#84fa92").place(x=20, y=10)
        self.search_txt = Entry(self.frame5, textvariable=self.search, font=(
            "Times New Roman", 14), background="white", width=25, bd=2, relief="solid")
        self.search_txt.place(x=180, y=40)
        Button(self.frame5, image=self.img_list[6], bg="#3903fc", relief="groove", bd=2, fg="white",
               activebackground="#027cd9", command=self.__search_entryforstudent).place(x=420, y=30)
        self.table = Treeview(self.frame5, columns=[
                              "id", "Name", "roll", "std", "div", 'sex', 'no', 'do'], selectmode="browse", show="headings", height=10)
        self.table.place(x=20, y=80, height=500)
        self.table.heading("id", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("roll", text="Roll No")
        self.table.heading("std", text="Std")
        self.table.heading("div", text="Divison")
        self.table.heading("sex", text="Gender")
        self.table.heading("no", text="Phone No")
        self.table.heading("do", text="Date Of birth")
        self.table.column("id", anchor="center", width=70)
        self.table.column("Name", anchor="center", width=190)
        self.table.column("roll", anchor="center", width=60)
        self.table.column("std", anchor="center", width=50)
        self.table.column("div", anchor="center", width=60)
        self.table.column("sex", anchor="center", width=60)
        self.table.column("no", anchor="center", width=120)
        self.table.column("do", anchor="center", width=90)

        self.__insert_record_student()
        self.sc = Scrollbar(
            self.frame5, command=self.table.yview, bd=2, relief="solid")
        self.table.configure(yscrollcommand=self.sc.set)
        self.sc.place(x=720, y=80, height=500)
        self.searchby_box = Combobox(self.frame5, background="white", values=(
            "All", "ID", "First Name", "Standard", "Division", "Gender"), font=("Times New Roman", 14), state="readonly", width=10)
        self.searchby_box.place(x=20, y=40)
        self.search_txt.bind("<Button-1>", lambda e: self.search.set(""))

    def __insert_record_student(self):
        query = '''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division,sex,father_phoneno,dob from student order by id;'''
        for data in backend.fetch_details(query):
            self.table.insert("", END, values=data)

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
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division,sex,father_phoneno,dob from student where {column} like "{self.search.get()}%";'''
            else:
                query = f'''select id,concat_ws(" ",first_name,middle_name,last_name),roll_no,std,division,sex,father_phoneno,dob from student where {column} like "%{self.search.get()}%";'''
            data = backend.fetch_details(query)
            if len(data) == 0:
                mb.showwarning("warning", "No Record found")
            else:
                for item in self.table.get_children():
                    self.table.delete(item)
                for d in data:
                    self.table.insert("", END, values=d)
                counter = Label(self.frame5, text=f"{len(data)} Records Found", font=(
                    "lucida", 12, "bold"), bg="#D671FD")
                counter.place(x=20, y=600)
                counter.after(6000, lambda: counter.place_forget())

    def attendance_frame(self):
        self.__remove_frames(6)
        self.frame6.place(x=260, y=10)
        Label(self.frame6, text="Mark Attendance", font=("Verdana", 26,
              "bold", "underline"), bg="#D671FD").place(x=400, y=10)
        Label(self.frame6, text="Select Divison :", font=(
            "Verdana", 12), bg="#D671FD").place(x=30, y=107)
        Label(self.frame6, text="Select Standard :", font=(
            "Verdana", 12), bg="#D671FD").place(x=180, y=107)
        Label(self.frame6, text="Select Date :", font=(
            "Verdana", 12), bg="#D671FD").place(x=340, y=107)
        self.div_box = Combobox(self.frame6, background="white", values=(
            "A", "B", "C", "D"), font=("Times New Roman", 14), state="readonly", width=6)
        self.div_box.place(x=30, y=130)
        self.date_of_attend = DateEntry(self.frame6, selectmode="day", font=(
            "Times New Roman", 16), bd=2, relief="solid")
        self.date_of_attend.place(x=340, y=130)
        list = []
        for i in range(1, 11):
            list.append(i)
        self.std_box = Combobox(self.frame6, background="white", values=list, font=(
            "Times New Roman", 14), state="readonly", width=6)
        self.std_box.place(x=180, y=130)
        Button(self.frame6, text="Get Students", bg="#03fcd7", foreground="white", font=("Verdana", 14), relief="ridge", bd=3,
               fg="black", activebackground="#CB00FF", width=14, activeforeground="white", command=self.mark_attendance).place(x=500, y=120)
        try:
            self.mark_atf.place_forget()
        except:
            pass

    def mark_attendance(self):
        if self.div_box.get() == "" or self.std_box.get() == "":
            mb.showwarning(
                "Error", "Please Select correct Standard and divison")
        else:
            data = backend.fetch_details(
                'select id,concat_ws(" ",first_name,last_name),roll_no from student where division=%s and std=%s order by roll_no;', (self.div_box.get(), self.std_box.get()))
            if len(data) == 0:
                mb.showinfo("No", "No Students found")
            else:
                self.btn = IntVar()
                self.mark_atf = Label(
                    self.frame6, bg="#D671FD", width=70, height=30, bd=3, relief="solid")
                self.mark_atf.place(x=20, y=180)
                self.add_present_days()
                self.get_no(data, 0)

                # print(row)

    def get_no(self, data, i):
        label_row = StringVar(value=" ")
        label_row.set(value=" ")
        try:
            row = data[i]
            label_row.set(value=f"{row[2]}.\t{row[1]}")
        except IndexError:
            mb.showinfo("Success", "Attendance has Been marked Successfully")
            self.mark_atf.place_forget()
        yes_radio = Radiobutton(self.mark_atf, text="Present", bg="#D671FD", font=(
            "Verdana", 14), variable=self.btn, value=1)
        no_radio = Radiobutton(self.mark_atf, text="Absent", bg="#D671FD", font=(
            "Verdana", 14), variable=self.btn, value=2)
        b2 = Button(self.mark_atf, text="<", font=("Verdana", 18, "bold"), bg="light grey",
                    width=3, relief="raised", command=lambda: self.evaluate(row, i-1, data))
        b1 = Button(self.mark_atf, text=">", font=("Verdana", 18, "bold"), bg="light grey",
                    width=3, relief="raised", command=lambda: self.evaluate(row, i+1, data))
        b2.place(x=5, y=150, height=80)
        b1.place(x=430, y=150, height=80)
        lbl = Label(self.mark_atf, text="Mark Attendance",
                    font=("Verdana", 14, "bold"), bg="#D671FD")
        lbl.place(x=160, y=10)

        yes_radio.place(x=90, y=160)
        no_radio.place(x=190, y=160)

        self.label_name = Entry(self.mark_atf, textvariable=label_row, font=(
            "Verdana", 14), bg="#D671FD", relief="flat", width=30, state="readonly")
        self.label_name.place(x=40, y=60)

    def evaluate(self, row, i, data):
        self.get_no(data, i)
        self.add_attendance(row[0])

    def add_attendance(self, row):
        if self.btn.get() == 0:
            mb.showwarning(
                "Error", "Please Select Any Choice Present or Absent")
        else:
            if self.btn.get() == 1:
                attend = "Y"
            elif self.btn.get() == 2:
                attend = "N"
            query = 'insert into attendance values (%s,%s,%s);'
            val = (row, attend, self.date_of_attend.get_date())
            if backend.execute_query(query, val):
                pass
            else:
                mb.showerror("Error", "Some Error Occured")

    def add_present_days(self):
        data = backend.fetch_details('select * from present;')
        present = False
        for d in data:
            if self.date_of_attend.get_date() in d:
                present = True
        if present == False:
            backend.execute_query(
                'insert into present values (%s);', (self.date_of_attend.get_date(),))
