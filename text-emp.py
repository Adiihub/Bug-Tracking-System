create database BTS;

Table-01: employee (To store ADMIN or EXPERT type of employees)
------------------------------------

create table employee
(
empLoginId varchar(10) primary key,
empPassword varchar(20),
empType varchar(20) ,
empName varchar(45),
empPhone varchar(10),
empEmail varchar(45),
empStatus varchar(20) DEFAULT 'ACTIVE'
);

insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail )
values('AD1001', 'password', 'ADMIN', 'Priti Singh', '9998887776', 'help@admin.com');

insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail )
values('EX3001', 'password', 'EXPERT', 'DemoUser', '4444444', 'expert@admin.com');


Table-02: customer
------------------------------------

create table customer
(
custLoginId varchar(10) primary key,
custPassword varchar(20),
custName varchar(45),
custAge int,
custPhone varchar(10),
custEmail varchar(45)
);

insert into customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail )
values('CU2001', 'password', 'Priya', 21, '9998887776', 'priya@demo.com');

insert into customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail )
values('CU2002', 'password', 'Anjali', 22, '9998887776', 'priya@demo.com');


Table-03: bug
------------------------------------
create table Bug
( bugId int primary key auto_increment,
bugPostingDate datetime default now(),
custLoginId varchar(10) NOT NULL,
bugStatus varchar(20) default 'New Bug',
productName varchar(45) NOT NULL,
bugDesc text NOT NULL,
expertAssignedDate datetime default NULL,
expertLoginId varchar(10) default NULL,
bugSolvedDate datetime default NULL,
solution text default NULL
);

insert into Bug(custLoginId, productName, bugDesc)
values('CU2001', 'Laptop', 'Screen is flickring');

insert into Bug(custLoginId, productName, bugDesc)
values('CU2001', 'Mobile', 'Keyboard not working.');

insert into Bug(custLoginId, productName, bugDesc)
values('CU2002', 'Laptop', 'Wifi connection issues');