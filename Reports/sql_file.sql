create database students_db;

use students_db;

# create table for login details
create table login_details(id varchar(12) primary key not null,
uname varchar(45) not null,
password varchar(255) not null,
typeofuser varchar(45) not null);

# Enter the super admin details
insert into login_details values ("","",md5(""),"");

# create the admin table
create table admin(id varchar(8) primary key not null,name varchar(45) not null unique,address text not null,phoneno bigint not null,age int not null,sex varchar(10) not null);

# creating the stored procedure to add the admin id automatically
delimiter &&
create procedure addadmin(in name varchar(255),in address text,in phoneno bigint,in age int,in sex varchar(10))
begin
declare countad int default 0;
declare i int default 1000;
declare idreturn varchar(8);
declare getid varchar(8);
select count(*) into countad from admin;
set i=countad+i;
set idreturn=concat("AD",i);
insert into admin values (get_correct_fid(idreturn),name,address,phoneno,age,sex);
end &&
delimiter ;

# trigger for deleting the record from admin and automatically from login details
delimiter &&
create trigger auto_delete_login
after delete
on admin 
for each row
begin
delete from login_details where id=old.id;
end &&
delimiter ;

# create table for faculty
create table faculty (id varchar(8) primary key not null ,
first_name varchar(45) not null,
middle_name varchar(45) not null,
last_name varchar(45) not null,
experience int not null,
doj date not null,
dob date not null,
email varchar(255) not null,
sub varchar(255) not null,
address text not null,
qualification text not null,
age int not null,
sex varchar(8) not null,
phoneno bigint not null);

# stored procedure to add the faculty id automatically
delimiter &&
create procedure addfaculty(in fn varchar(45),in mn varchar(45),in ln varchar(45),in exp int,in doj date,in dob date,in email varchar(255),in  sub varchar(255),in address text,in quali text,in age int,in sex varchar(8),in phone bigint)
begin
declare countad int default 0;
declare i int default 10000;
declare idreturn varchar(8);

declare getid varchar(8);
select id into getid from faculty order by id desc limit 1;
select count(*) into countad from faculty;
set i=countad+i;
set idreturn=concat("FT",i);
insert into faculty values (get_correct_aid(idreturn),fn,mn,ln,exp,doj,dob,email,sub,address,quali,age,sex,phone);
end &&
delimiter ;

# trigger for deleting the record from faculty and automatically from login details
delimiter &&
create trigger auto_delete_login_faculty
after delete
on faculty 
for each row
begin
delete from login_details where id=old.id;
delete from div_details where faculty_id=old.id;
end &&
delimiter ;

# create table for keeping the student record
create table student(
id varchar(8) not null primary key,
first_name varchar(45) not null,
middle_name varchar(45) not null,
last_name varchar(45) not null,
roll_no int not null,
division char(1) not null,
address text not null,
phoneno bigint not null,
father_name varchar(100) not null,
mother_name varchar(100) not null,
std int not null,
dob date not null,
bloodgroup char(4),
doa date not null,
father_occ varchar(100),
mother_occ varchar(100),
father_phoneno bigint not null,
sex varchar(10) not null);

# create table for assigining the class teacher
create table div_details(std int,divison char(1),faculty_id varchar(8), foreign key (faculty_id) references faculty(id) on delete no action on update no action);

# creating a trigger to delete the div details 
delimiter &&
create trigger delete_from_div
before delete
on faculty 
for each row
begin
delete from div_details where faculty_id=old.id;
end &&
delimiter ;

# to add the correct admin id
delimiter &&
create function get_correct_fid(idi varchar(8))
returns varchar(8)
deterministic
begin
declare i int default 0;
declare rore varchar(8);
declare noofro int;
declare ex_id int;
declare returnid varchar(8);
select count(*) into noofro from admin; 
id_label:loop
select id into rore from admin order by id limit 1 offset i;
			select substring(rore,3,5) into ex_id;
			if i>=noofro then return idi;
           elseif rore=idi then 
				set ex_id=ex_id+1;
                set idi=concat("AD",ex_id);
                set i=i+1;
			else set i=i+1;
            end if;
		end loop;
end &&
delimiter ;

# for adding the correcct faculty id 
delimiter &&
create function get_correct_aid(idi varchar(8))
returns varchar(8)
deterministic
begin
declare i int default 0;
declare rore varchar(8);
declare noofro int;
declare ex_id int;
select count(*) into noofro from faculty; 
id_label:loop
select id into rore from faculty order by id limit 1 offset i;
			select substring(rore,3,5) into ex_id;
			if i>=noofro then return idi;
           elseif rore=idi then 
				set ex_id=ex_id+1;
                set idi=concat("FT",ex_id);
                set i=i+1;
			else set i=i+1;
            end if;
		end loop;
end &&
delimiter ;
describe student;

# create a procedure to add the student id
delimiter &&
create procedure addstudent(
in f_name varchar(45),in m_name varchar(45),in l_name varchar(45),in rolno int,in divi char(1),
in addr text,in phone bigint,in father_n varchar(100),in mother_n varchar(100),
in std int,in dob date,in bg char(4),in doa date,in father_occ varchar(100),in mother_occ varchar(100),
in sex varchar(10))
begin
declare countad int default 0;
declare i int default 10000;
declare idreturn varchar(8);
declare getid varchar(8);
select count(*) into countad from admin;
set i=countad+i;
set idreturn=concat("ST",i);
insert into student values (get_correct_sid(idreturn),f_name,m_name,l_name,rolno,divi,addr,father_n,mother_n,std,dob,bg,doa,father_occ,mother_occ,phone,sex);
end &&
delimiter ;

# fucntion to get the correct id for studetn
delimiter &&
create function get_correct_sid(idi varchar(8))
returns varchar(8)
deterministic
begin
declare i int default 0;
declare rore varchar(8);
declare noofro int;
declare ex_id int;
select count(*) into noofro from student; 
id_label:loop
select id into rore from student order by id limit 1 offset i;
			select substring(rore,3,5) into ex_id;
			if i>=noofro then return idi;
           elseif rore=idi then 
				set ex_id=ex_id+1;
                set idi=concat("ST",ex_id);
                set i=i+1;
			else set i=i+1;
            end if;
		end loop;
end &&
delimiter ;

# creating trigger to auto delete the login detials form the student
delimiter &&
create trigger dele_student_login
after delete
on student
for each row
begin
delete from login_details where id=old.id;
end &&
delimiter ;



# creating table for fees 
create table fees (id varchar(8) not null,fullyearpaid enum("Y","N"),
year_ year not null,jan enum("Y","N"),feb enum("Y","N"),mar enum("Y","N"),
april enum("Y","N"),may enum("Y","N"),june enum("Y","N"),july enum("Y","N"),
aug enum("Y","N"),sept enum("Y","N"),oct enum("Y","N"),nov enum("Y","N"),
dece enum("Y","N"),foreign key (id) references student(id) on delete cascade on update no action,
foreign key (year_) references store_fees(year_) on delete no action on update no action);

# creating the table for storing the fees for each year
create table store_fees(year_ year not null primary key,
monthly int,yearly int);

# create a trigger to auto add the student in the fees table
delimiter &&
create trigger auto_add_fees
after insert 
on student
for each row 
begin
insert into fees values (new.id,"N",year(new.doa),"N","N","N","N","N","N","N","N","N","N","N","N");
end &&
delimiter ;

# create procedure to add the fees 
delimiter &&
create procedure add_fees(in id_c varchar(8),in ye year)
begin
insert into fees values (id_c,"N",ye,"N","N","N","N","N","N","N","N","N","N","N","N");
end &&
delimiter ;

# creating a table for the attendance
create table attendance(id varchar(8) not null,attended enum("Y","N"),date_attend date,
foreign key (date_attend) references present(present_date));

# creating the present working days tabble
create table present(present_date date primary key not null);

# creating a function for geting absent or present
delimiter &&
create function get_presentee(PA char(1))
returns varchar(45)
deterministic
begin
if PA="Y" then return "Present";
elseif PA="N" then return "Absent";
end if;
end &&
delimiter ;