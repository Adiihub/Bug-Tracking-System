
import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='bts', user='root', password='password')
    return db

#-------------------------------------------
#Customer Module
#-------------------------------------------
def createaccount():
    db = getBTSDatabase()
    mycursor = db.cursor()
    try:
        cuLog = input("Create Login id :- ")
        cuName = input("Enter Your Name :- ")
        cuPass = input("Enter Password :- ")
        cuAge = input("Enter Your Age :- ")
        cuPhone = input("Enter Your Phone no :- ")
        cuEmail = input("Enter Your Email :- ")

        sql= "insert into customer (custLoginId, custPassword, custName, custAge, custPhone, custEmail) " \
            "values('%s','%s', '%s', '%s', '%s', '%s' )"
        values = (cuLog,cuPass,cuName,cuAge,cuPhone,cuEmail)

        mycursor.execute(sql % values)
        print("Your Account is created Successfully.")

    except (IOError, ValueError, NameError) as e1:
        print("Wrong input Retry.. : ",e1)
    finally:
        print("Thank You!")
    mycursor.close()
    db.commit()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()
def UpdateAccount():
    db = getBTSDatabase()
    mycursor = db.cursor()

    id = input("Enter LoginId for Updating details : ")
    pas = input("Enter the Password : ")
    print("=============================")
    print("1. Change the Age ")
    print("2. Change Phone no ")
    print("3. Change Email-id  ")
    print("=============================")
    choice = int(input("Press any number to access : "))

    if choice==1:
        ag=input("Enter New Age : ")
        sql = "update customer set custAge='%s' where custloginid='%s'"
        values = (ag,id)
    elif choice==2:
        ph=input("Enter New Phone-no : ")
        sql = "update customer set custPhone='%s' where custloginid='%s'"
        values = (ph, id)
    elif choice==3:
        em=input("Enter New Email : ")
        sql = "update customer set custEmail='%s' where custloginid='%s'"
        values = (em, id)
    else:
        print("Please enter correct number..")

    mycursor.execute(sql % values)
    db.commit()
    if mycursor.rowcount==1:
        print("Your Account Updated Successfully.")
    else:
        print("Account Updation failed! Retry..")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()
def PostNewBug():
    db = getBTSDatabase()
    mycursor = db.cursor()

    id= input("Enter Customer Login-id : ")
    pn=input("Enter Product Name : ")
    bug=input("Enter Bug Details : ")

    sql = "insert into bug (custLoginId, productName, bugDesc) values('%s','%s','%s' )"
    values = (id,pn,bug)
    mycursor.execute(sql % values)
    print("Bug Submitted Successfully.")
    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()
def Viewbugsol():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("\nEnter Login-id to check Your Bug : ")
    name = input("Enter your product name : ")
    sql = "select * from bug where custLoginId='%s'"
    values = (id)
    mycursor.execute(sql % values)
    print("\n==============================================================================================================================")
    print("%-7s %-15s %-12s %-12s %-25s %-10s}" % ('bugId', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc', 'solution'))
    print("================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<15s} {2:<12s} {3:<12s} {4:<25s} {5:10s}".format(str(row[0]), str(row[2]), str(row[3]), str(row[4]), str(row[5]),str(row[9])), "\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()
def ViewBugsbystatus():
    db = getBTSDatabase()
    mycursor=db.cursor()
    sta = input("\nEnter Bug Status : ")
    sql = "select * from bug where bugStatus='%s' "
    values = (sta)
    mycursor.execute(sql%values)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc', 'expAssDate', 'expLoginId','bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),str(row[8]), str(row[9])), "\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()

def ChangeCustPassword():
    db = getBTSDatabase()
    mycursor = db.cursor()

    id=input("Enter Your Login-id : ")
    pas = input("Enter Current Password : ")
    new = input("Enter New Password : ")
    try:
        mysql = "select * from customer where custloginid='%s' "
        values=(id)
        mycursor.execute(mysql % values)
        row = mycursor.fetchmany(1)
        op = row[0][1]

        if op == pas:
            sql = "update customer set custPassword='%s' where custLoginId = '%s'"
            values = (new, id)
            mycursor.execute(sql % values)
            print("Password Updated Successfully..")
        else:
            print("Please Enter correct Password..")
    except:
        print("PLease enter correct login-id.")

    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customer()
    else:
        Login()

#-------------------------------------------
# Expert Module -
#-------------------------------------------

def viewassignbug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    print("\n\t+---------------------------+")
    print("\t|\t\t\tNew Bug\t\t\t|")
    print("\t+---------------------------+")
    sql = "select * from bug where bugStatus!='solved'"
    mycursor.execute(sql)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc', 'expAssDate', 'expLoginId','bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),str(row[8]), str(row[9])), "\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Expert Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Expert()
    else:
        Login()
def filterassignbugs():
    db = getBTSDatabase()
    mycursor = db.cursor()
    print("\n\t+-----------------------------------+")
    print("\t|\t\t\tAssign Bug..\t\t\t|")
    print("\t+-----------------------------------+\n")
    ex = input("Enter Your Login-id : ")
    bugid = input("Enter Bug-id : ")
    sql = "update bug set expertLoginId='%s', bugStatus='Assigned', expertAssignedDate=now() where bugId='%s' "
    values = (ex,bugid)
    mycursor.execute(sql % values)
    print("Bug has been assigned successfully.")
    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Expert Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Expert()
    else:
        Login()
def solvebug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    print("\n\t+--------------------------------+")
    print("\t|\t\t\tSolve Bug..\t\t\t|")
    print("\t+--------------------------------+\n")

    bugid = input("Enter Bug-id : ")
    sql = "update bug set bugSolvedDate=now(), bugStatus='Solved', solution='Pls visit nearest service center' where bugId='%s' "

    values = (bugid)
    mycursor.execute(sql % values)
    print("Bug has been Solved successfully.")
    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Expert Section\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Expert()
    else:
        Login()


#---------------------------------
# Customer Services -
#---------------------------------

def ViewAll():
    db=getBTSDatabase()
    mycursor=db.cursor()
    # id=input("Enter Your Login-id : ")
    # pas = input("Enter Your Password : ")
    print("\n|-----------------------------------------|")
    print("\t\t~*~ Customer Services ~*~")
    print("|-----------------------------------------|\n")
    sql="select * from customer"
    mycursor.execute(sql)
    rowcount = mycursor.fetchall()
    print("=========================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s" % ('custLoginId','custPassword','custName','custAge','custPhone','custEmail'))
    print("=========================================================================================================================")

    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s}".format(str(row[0]) ,str(row[1]) ,str(row[2]) ,str(row[3]) ,str(row[4]) ,str(row[5])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customerservices()
    else:
        Login()
def SearchbyCustName():
    db = getBTSDatabase()
    mycursor = db.cursor()
    name = input("\nEnter Customer Name to search their Account : ")
    sql = "select * from customer where custName = '%s'"
    values = (name)
    mycursor.execute(sql%values)
    rowcount = mycursor.fetchall()
    print("\n=========================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s" % ('custLoginId', 'custPassword', 'custName', 'custAge', 'custPhone', 'custEmail'))
    print("=========================================================================================================================")
    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s}".format(str(row[0]) ,str(row[1]) ,str(row[2]) ,str(row[3]) ,str(row[4]) ,str(row[5])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customerservices()
    else:
        Login()
def SearchbyCustLog():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("\nEnter Customer Login-id to search their Account : ")
    sql = "select * from customer where custLoginId = '%s'"
    values = (id)
    mycursor.execute(sql % values)
    rowcount = mycursor.fetchall()
    if rowcount==None:
        print("\tPlease enter correct login-id.")
    else:
        print("\n=========================================================================================================================")
        print("%-20s %-20s %-20s %-20s %-20s %-20s" % ('custLoginId', 'custPassword', 'custName', 'custAge', 'custPhone', 'custEmail'))
        print("=========================================================================================================================")

    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Customer Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        Customerservices()
    else:
        Login()

#--------------------------------
#   For Bug Services
#--------------------------------
def ViewAllBugs():
    db = getBTSDatabase()
    mycursor=db.cursor()
    sql = "select * from bug order by bugId asc"
    mycursor.execute(sql)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc', 'expAssDate', 'expLoginId','bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]),str(row[8]), str(row[9])), "\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Bug Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        BugServices()
    else:
        Login()
def Searchbybugid():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("Enter Bug-id no : ")
    sql = "select * from bug where bugId='%s'"
    values = (id)
    mycursor.execute(sql%values)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc','expAssDate', 'expLoginId', 'bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]), str(row[7]), str(row[8]),str(row[9])),"\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Bug Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        BugServices()
    else:
        Login()
def Searchbystatus():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("Enter Bug Status to show Bug : ")
    sql = "select * from bug where bugStatus='%s'"
    values = (id)
    mycursor.execute(sql%values)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc','expAssDate', 'expLoginId', 'bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]), str(row[7]), str(row[8]),str(row[9])),"\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Bug Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        BugServices()
    else:
        Login()
def Searchbycustid():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("Enter Customer Login-id to Check Bug : ")
    sql = "select * from bug where custLoginId='%s'"
    values = (id)
    mycursor.execute(sql%values)
    print("\n=======================================================================================================================================================")
    print("%-7s %-20s %-15s %-12s %-12s %-25s %-18s %-12s %-12s %-10s}" % ('bugId', 'bugPostingDate', 'custLoginId', 'bugStatus', 'prodName', 'BugDesc','expAssDate', 'expLoginId', 'bugSolDate', 'solution'))
    print("=======================================================================================================================================================")
    for row in mycursor.fetchall():
        print("{0:<7s} {1:<20s} {2:<15s} {3:<12s} {4:<12s} {5:<25s} {6:<18s} {7:<12s} {8:<12s} {9:10s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]), str(row[7]), str(row[8]),str(row[9])),"\n")
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Bug Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        BugServices()
    else:
        Login()
def Assigntoexpert():
    db = getBTSDatabase()
    mycursor = db.cursor()
    bugid = input("Enter Bug-id no :")
    sol = input("Enter the solution of the bug : ")
    sql = "update bug set bugSolvedDate = now(), bugStatus= 'Solved', solution='%s' where bugId='%s' "
    values = (sol,bugid)
    mycursor.execute(sql % values)
    print("Your Updation is done.")
    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Bug Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        BugServices()
    else:
        Login()

#----------------------------
# Employee Services -
#----------------------------

def AddNewAdminExp():       #for Employee Section
    db=getBTSDatabase()
    mycursor = db.cursor()

    empLoginId=input("Enter login-id :")
    empPassword = input("Enter Password :")
    empType = input("Enter Employee-type (Admin/expert) :")
    empName= input("Enter Employee Name :")
    empPhone = input("Enter Employee Phone no :")
    empEmail= input("Enter Employee Email :")

    sql = "INSERT INTO employee(empLoginId, empPassword, empType, empName, empPhone, empEmail )" "values('%s','%s','%s','%s','%s','%s')"

    values = ( empLoginId,empPassword,empType,empName,empPhone,empEmail)
    mycursor.execute(sql % values)
    print("Your Account has been Added.")
    db.commit()
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch==1:
        EmployeeServices()
    else:
        Login()

def viewAll():      #for Employee Section
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = "select * from employee"
    mycursor.execute(sql)
    rowcount = mycursor.fetchall()
    print("\n========================================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s" % ('empLoginId', 'empPassword', 'empType', 'empName', 'empPhone', 'empEmail', 'empStatus'))
    print("========================================================================================================================================")
    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s} {6:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]), str(row[6])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        EmployeeServices()
    else:
        Login()
def Searchbyempname():      #for Employee Section
    db = getBTSDatabase()
    mycursor = db.cursor()
    name = input("\nEnter Employee name to Search their Account : ")
    sql = "select * from employee where empName='%s' "
    values = (name)
    mycursor.execute(sql%values)
    rowcount = mycursor.fetchall()
    print("\n========================================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s}" % ('empLoginId', 'empPassword', 'empType', 'empName', 'empPhone', 'empEmail', 'empStatus'))
    print("========================================================================================================================================")
    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s} {6:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]), str(row[6])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        EmployeeServices()
    else:
        Login()
def Searchbyempid():        #for Employee Section
    db = getBTSDatabase()
    mycursor = db.cursor()
    name = input("\nEnter Employee Login-id to Search their Account : ")
    sql = "select * from employee where empLoginId='%s' "
    values = (name)
    mycursor.execute(sql%values)
    rowcount = mycursor.fetchall()
    print("\n========================================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s}" % ('empLoginId', 'empPassword', 'empType', 'empName', 'empPhone', 'empEmail', 'empStatus'))
    print("========================================================================================================================================")
    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s} {6:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]), str(row[6])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        EmployeeServices()
    else:
        Login()
def Searchbyemptype():      #for Employee Section
    db = getBTSDatabase()
    mycursor = db.cursor()
    name = input("\nEnter Employee Type (admin/expert) to Search their Account : ")
    sql = "select * from employee where empType='%s' "
    values = (name)
    mycursor.execute(sql%values)
    rowcount = mycursor.fetchall()
    print("\n========================================================================================================================================")
    print("%-20s %-20s %-20s %-20s %-20s %-20s %-20s}" % ('empLoginId', 'empPassword', 'empType', 'empName', 'empPhone', 'empEmail', 'empStatus'))
    print("========================================================================================================================================")
    for row in rowcount:
        print("{0:<20s} {1:<20s} {2:<20s} {3:<20s} {4:<20s} {5:<20s} {6:<20s}".format(str(row[0]), str(row[1]), str(row[2]),str(row[3]), str(row[4]), str(row[5]), str(row[6])))
    db.close()

    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        EmployeeServices()
    else:
        Login()
def ChangePassword():
    db = getBTSDatabase()
    mycursor=db.cursor()
    print("\n\t-------------------------------------")
    print("\t|\t\t~*~ Change Password ~*~\t\t|")
    print("\t-------------------------------------")
    id = input("\nEnter login id to change password : ")
    pas=input("Enter Current Password : ")
    np = input("Enter New Password : ")
    sql = "select * from employee where empLoginId='%s' "
    values= (id)
    mycursor.execute(sql%values)
    row = mycursor.fetchmany(1)
    val= row[0][1]
    try:
        if val==pas:
            sql = "update employee set empPassword='%s' where empLoginId='%s' "
            values=(np,id)
            mycursor.execute(sql % values)
            print("Your Password has been Updated.")
        else:
            print("Please Enter correct Password..")
    except:
        print("PLease enter correct login-id.")
    db.commit()
    db.close()
    print("\n...................................")
    print("\nPress 1. to go Employee Services\nPress 2. to go Login page\n")
    ch = int(input("Enter any of two options : "))
    if ch == 1:
        EmployeeServices()
    else:
        Login()


#--------------------------------------------------------------------
#                   *** Modules ***
#--------------------------------------------------------------------

def adminlogin():
    db = getBTSDatabase()
    mycursor = db.cursor()
    print('\n................................\n')
    name = input("\tEnter Admin Login-id : ")
    pas = input("\tEnter Admin Password : ")
    sql = "select * from employee where empLoginId = '%s' "
    values = (name)
    mycursor.execute(sql % values)
    try:
        row = mycursor.fetchmany(1)
        check = row[0][1] #because it's storing in tuple list
        if check == pas:
            print("\nLogin Successfull.\n")
            Admin()
        else:
            print("\nWrong Password Retry..\n")
            adminlogin()
    except:
        print("\nInvalid Login-id retry..\n")
        adminlogin()
def Admin():
    print("\n\n\t==============================================================================================")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t\t\t\t\t\t\t~ Welcome Admin ~")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t1. Customer Services")
    print("\t2. Employee Services")
    print("\t3. Bug Services\n")
    choice=int(input("Choose any number you want to proceed : "))
    if choice==1:
        Customerservices()
    elif choice==2:
        EmployeeServices()
    elif choice==3:
        BugServices()
    else:
        print("\t<< Please Choose correct option >>")
def Customerservices():
    print("\n\n\t\t**********************************************************")
    print("\t\t\t\t\tWelcome to Customer Services")
    print("\t\t**********************************************************\n\n")
    print("\t1.View All Customer")
    print("\t2.Search - by Customer Name")
    print("\t3.Search - by Customer Login Id")
    print("\t4.Go to Login\n")
    opt = int( input("Enter Your Choice of above mention options : "))
    if opt==1:
        ViewAll()
    elif opt==2:
        SearchbyCustName()
    elif opt==3:
        SearchbyCustLog()
    elif opt==4:
        Login()
    else:
        print("\n<< You Entered Wrong Number - Retry..>>")
    Customerservices()
def EmployeeServices():
    print("\n\t\t**********************************************************")
    print("\t\t\t\t\tWelcome to Employee Services")
    print("\t\t**********************************************************\n")
    print("\t1.Add New (Admin or Expert)")
    print("\t2.View All")
    print("\t3.Search - by Employee Name")
    print("\t4.Search - by Employee Login Id")
    print("\t5.Search - by Employee Type")
    print("\t6.Activate or Deactivate")
    print("\t7.Change Password")
    print("\t8.Go to Login\n")
    choice=int(input("Choose any number you want to proceed : "))
    if choice==1:
        AddNewAdminExp()
    elif choice==2:
        viewAll()
    elif choice==3:
        Searchbyempname()
    elif choice==4:
        Searchbyempid()
    elif choice==5:
        Searchbyemptype()
    elif choice==6:
        ActiDeacti()
    elif choice==7:
        ChangePassword()
    elif choice==8:
        Login()
    else:
        print("\n<< You Entered Wrong Number - Retry..>>")
    EmployeeServices()
def BugServices():
    print("\t\t********************************************************")
    print("\t\t\t\t\tWelcome to Bug Services")
    print("\t\t********************************************************\n")
    print("\t1.View All Bug")
    print("\t2.Search Bug by bugId")
    print("\t3.Search Bug by status")
    print("\t4.Search Bug by custLoginId")
    print("\t5.Assign Bug to Expert")
    print("\t6.Logout")
    choice=int(input("Choose any number you want to proceed : "))
    if choice==1:
        ViewAllBugs()
    elif choice==2:
        Searchbybugid()
    elif choice==3:
        Searchbystatus()
    elif choice==4:
        Searchbycustid()
    elif choice==5:
        Assigntoexpert()
    elif choice==6:
        Login()
    else:
        print("\n<< You Entered Wrong Number - Retry..>>")
    BugServices()

#--------------------------------------------------------------
def Customer():
    print("\n\n==============================================================================================")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t\t\t\t\t\t\t~ Welcome User ~")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t1. Create Account")
    print("\t2. Update Account")
    print("\t3. Post New Bug\n")
    print("\t4. View All Bugs")
    print("\t5. Search Bugs based on status")
    print("\t6. View Bug Solution\n")
    print("\t7. Change Password")
    print("\t8. Logout\n")
    choice = int(input("Choose any number you want to proceed : "))
    if choice == 1:
        createaccount()
    elif choice == 2:
        UpdateAccount()
    elif choice == 3:
        PostNewBug()
    elif choice==4:
        Viewbugsol()
    elif choice==5:
        ViewBugsbystatus()
    elif choice==6:
        Viewbugsol()
    elif choice==7:
        ChangeCustPassword()
    elif choice==8:
        Login()
    else:
        print("\n<< You Entered Wrong Number - Retry..>>")
        Customer()

#--------------------------------------------------------------
def Expert():
    print("\n\n==============================================================================================")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t\t\t\t\t\t\t~ Welcome Expert ~")
    print("\n\t\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\t1. View Assigned Bug")
    print("\t2. Filter Assigned Bugs based on status")
    print("\t3. Solve the Bug")
    print("\t4. Change Password")
    print("\t5. Logout\n")
    choice = int(input("\nChoose any number you want to proceed : "))
    if choice == 1:
        viewassignbug()
    elif choice == 2:
        filterassignbugs()
    elif choice == 3:
        solvebug()
    elif choice == 4:
        ChangePassword()
    elif choice == 5:
        Login()
    else:
        print("\n<< You Entered Wrong Number - Retry..>>")

#======================================================================
#               Program Execution start form here
#======================================================================
def Login():
    print("\n\n\t\t\t\t\t******************************************************\n")
    print("\t\t\t\t\t\t\t~*~ Welcome to Bug Tracking System ~*~\t\t\t")
    print("\n\t\t\t\t\t******************************************************\n")
    print("\t\t\t\t\t\t1.Admin")
    print("\t\t\t\t\t\t2.Customer")
    print("\t\t\t\t\t\t3.Expert\n")
    print("\t\t\t\t\t\t-----------------------------------------")
    choice = int(input("\t\t\t\t\t\tPress any no that You want to access : "))
    if choice==1:
        adminlogin()
    elif choice==2:
        Customer()
    elif choice==3:
        Expert()
    else:
        print("Wrong Number Entered Retry..Thank You!")

Login()
