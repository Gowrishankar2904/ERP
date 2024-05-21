#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb
import os
import smtplib

cgitb.enable()
conn=pymysql.connect(host="Localhost", user="root", password="", database="erp")
cur=conn.cursor()

q1="""select max(id) from empreg"""
cur.execute(q1)
r=cur.fetchone()

#print(r)
if r[0]!=None:
    n=r[0]
else:
    n=0

#print(n)

z=""

if n<9:
    z="000"
elif n>=10 and n<=99:
    z="00"
elif n>=100 and n<=999:
    z="0"

form=cgi.FieldStorage()

empid="EMP"+z+str(n+1)

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin/HR Home</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    
    <style>
        *,
        body,
        html {
            
            padding: 0px;
            margin: 0px;
            box-sizing: border-box;
        }

        #sidenav {
            background-color: rgb(3,3,27);
            opacity: 1.0;
            max-width: 270px
        }

        #sidenavLinks {
           color :Orangered;
            font-weight: 600;
        }
        body{
        background-color:#fbf9f1;
        }
        #subRes {
                width: 100px;
                border-radius: 20px;
                position: relative;
                left: 100px;
            }
    </style>
</head>

<body>
    <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-lg-3 px-sm-1 px-0" id="sidenav">
                <div class="d-flex flex-column align-items-start p-4 min-vh-100 sticky-left">
                    <a href="/" class="d-flex align-items-center py-2 text-muted text-decoration-underline">
                        <span class="fs-3 fw-bold d-none d-sm-inline">ELNO TECH</span>
                    </a>
                    <ul class="nav flex-column px-lg-4 px-0" id="menu">
                        <li class="nav-item">
                            <a href="./admindashboard.py" class="nav-link align-middle px-0 active">
                                <i class="fs-6 bi bi-house-fill px-2 text-muted"></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Home</span>
                            </a>
                        </li>
                        <li>
                            <a href="#submenu5" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fs-6 bi bi-person-plus-fill px-2 text-muted "></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Employee</span>
                            </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu5" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./Dashboard.py" class="nav-link px-0"> <span id="sidenavLinks"> Add New
                                            Employee</span>
                                    </a>
                                </li>
                                <hr class="dropdown-divider text-white">
                                <li>
                                    <a href="./adminremoveemployee.py" class="nav-link px-0"> <span id="sidenavLinks">Remove
                                            Employee</span>
                                    </a>
                                </li>
                                 <hr class="dropdown-divider text-white">
                                <li>
                                    <a href="./adminupdateemployee.py" class="nav-link px-0"> <span id="sidenavLinks">Update
                                            Employee</span>
                                    </a>
                                </li>
                            </ul>
                        <li>
                            <a href="#submenu1" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fs-6 bi bi-list-task px-2 text-muted "></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Task</span>
                            </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu1" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./empshow.py" class="nav-link px-0"> <span id="sidenavLinks"> Create New
                                            Task</span>
                                    </a>
                                </li>
                                <hr class="dropdown-divider text-white">
                                <li>
                                    <a href="./existtaskadmin.py" class="nav-link px-0"> <span id="sidenavLinks"> Review
                                            Existing Task</span>
                                    </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="fs-6 bi bi-laptop-fill px-2 text-muted"></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Inventory</span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./admininventryview.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks"> Inventory
                                            Request</span>
                                    </a>
                                </li>
                                <li class="w-100">
                                    <a href="./admininventryhistory.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks"> Inventory
                                            View</span>
                                    </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fs-6 bi bi-toggle2-off px-2 text-muted"></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Leave</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./adminleaveview.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks"> New Leave
                                            Request</span>
                                    </a>
                                </li>
                                <hr class="dropdown-divider text-white">
                                <li>
                                    <a href="./adminleaveviewall.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks"> Existing
                                            Request</span>
                                    </a>
                                </li>

                            </ul>
                        </li>
                        <a href="#submenu4" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                            <i class="fs-6 bi bi-wallet-fill px-2 text-muted"></i> <span class="ms-1 d-none d-sm-inline"
                                id="sidenavLinks">Salary</span> </a>
                        <ul class="collapse nav flex-column ms-1" id="submenu4" data-bs-parent="#menu">
                            <li class="w-100">
                                <a href="./adminsalarycalculation.py" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">
                                        
                                        Salary Calculation</span>
                                </a>
                                <hr class="dropdown-divider text-white">
                                <a href="./salaryview.py" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">
                                        
                                        Salary Form</span>
                                </a>
                            </li>
                        </ul>
                        <hr>

                </div>
            </div>
                <div class="col p-4">
                    <center>
                        <h1 class="display-4 fw-normal shadow-sm pb-2">Welcome Admin/HR</h1>
                    </center>

                    <form action="#" class="p-5 " name="image" method="post" enctype="multipart/form-data">
                        <div class="row pb-4">
                            <!-- <input type="text"> -->""")
print(""" <div class="col-md-4">

                                <input class="form-control" type="text" name="empid" value="%s" readonly required>
                            </div>""" %empid)

print("""                          <div class="col-md-4">
                                <input class="form-control" type="text" name="name" placeholder="Name" maxlength="20"
                                    required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" type="date" name="dob" placeholder="Dob" maxlength="20"
                                    required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-4">
                                <input class="form-control" type="text" name="role" placeholder="Designation"
                                    maxlength="20" required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" type="number" name="phone" placeholder="contact no"
                                    maxlength="15" required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" type="mail" name="mail" placeholder="Email_id"
                                    maxlength="30" required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <textarea class="form-control" type="textarea" name="address" placeholder="Address"
                                    maxlength="150" cols="" rows="3"></textarea>
                            </div>
                            <div class="col-md-6">
                                <select class="form-control" type="text" name="city" maxlength="20" required>
                                    <option value="" disabled selected>Select city</option>
                                    <option value="coimbatore">Coimbatore</option>
                                    <option value="kochin">Kochin</option>
                                    <select>

                                        <select class="form-control mt-2" type="text" name="state" maxlength="20"
                                            required>
                                            <option value="" disabled selected>Select state</option>
                                            <option value="Tamilnadu">Tamilnadu</option>
                                            <option value="kerala">Kerala</option>
                                        </select>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <select class="form-control" type="text" name="type" maxlength="20" required>
                                    <option value="" disabled selected>Select Employeement type</option>
                                    <option value="fulltime">Fulltime</option>
                                    <option value="parttime">Parttime</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <input class="form-control" type="number" name="salary" placeholder="Salary" maxlength="10"
                                    required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <input class="form-control" type="text" name="uname" placeholder="Username"
                                    maxlength="20" required>
                            </div>

                            <div class="col-md-6">
                                <input class="form-control" type="password" name="pwd"
                                    placeholder="Enter Password" required>
                            </div>

                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <input class="form-control" type="file" name="image"
                                    placeholder="Upload Profile Picture" required>
                            </div>

                            <div class="col-md-6">
                                <input class="btn btn-dark align-self-center mx-3" type="Submit" name="submit"
                                    value="Submit" id="subRes">
                                <input type="reset" class="btn btn-outline-dark" value="Reset" id="subRes">
                            </div>
                        </div>
                    </form>
                </div>

            </div>
        </div>

    </body>

</html>
""")


emname=form.getvalue("name")
emdob=form.getvalue("dob")
emrole=form.getvalue("role")
emphone=form.getvalue("phone")
emmail=form.getvalue("mail")
emaddr=form.getvalue("address")
emcity=form.getvalue("city")
emstate=form.getvalue("state")
emtype=form.getvalue("type")
emsalary=form.getvalue("salary")
emuname=form.getvalue("uname")
empass=form.getvalue("pwd")
empid=form.getvalue("empid")
emsubmit=form.getvalue("submit")

if len(form) !=0:
    empimg = form['image']
    if empimg.filename:
        fn=os.path.basename(empimg.filename)
        open("media/" + fn, "wb").write(empimg.file.read())
        q = """insert into empreg (empid, name, dob, role, phone, mail, address, city, state, emtype, salary, uname, password, profile) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(empid,emname,emdob,emrole,emphone,emmail,emaddr,emcity,emstate,emtype,emsalary,emuname,empass,fn)

        cur.execute(q)
        conn.commit()

        print("""
            <scirpt>
            alert("Data inserted successfully")
            </script>
             """)

        fromaddr = "elayaprasatht@gmail.com"
        password ="xkevcqxftsvewxbw"
        toaddr = emmail
        subject = 'Hi,welcome'
        body = """ Username: '%s'\nPassword: '%s' """ % (emuname, empass)
        msg = """ Subject:{}\n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()


        conn.close()