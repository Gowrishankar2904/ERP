#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb
import os

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="erp")
cur = conn.cursor()

form = cgi.FieldStorage()
pid = form.getvalue("id")

q1 = """select* from empreg where id="%s" """ %(pid)
cur.execute(q1)
res = cur.fetchall()

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
                                    <a href="./empupdate.py" class="nav-link px-0"> <span id="sidenavLinks">Update
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
                        <h1 class="display-5 shadow-sm pb-2">UPDATE EMPLOYEE</h1>
                    </center>""")

for i in res:
    Empid = i[1]
    Ename = i[2]
    EDob = i[3]
    Erole = i[4]
    Ephone = i[5]
    Eemail = i[6]
    Eaddress = i[7]
    Ecity = i[8]
    Estate = i[9]
    Eemtype = i[10]
    Esalary = i[11]
    Euname = i[12]
    Epass = i[13]
    print("""
                    <form action="#" class="p-5 " name="image" method="post" enctype="multipart/form-data">
                        <div class="row pb-4">
                            <!-- <input type="text"> -->
                            <div class="col-md-4">

                                <input class="form-control" type="text" name="empid" value="%s" readonly required>
                            </div>

                          <div class="col-md-4">
                                <input class="form-control" type="text" value="%s" name="name" placeholder="Name" maxlength="20"
                                    required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" value="%s" type="date" name="dob" placeholder="Dob" maxlength="20"
                                    required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-4">
                                <input class="form-control" value="%s" type="text" name="role" placeholder="Designation"
                                    maxlength="20" required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" value="%s" type="number" name="phone" placeholder="contact no"
                                    maxlength="10" required>
                            </div>
                            <div class="col-md-4">
                                <input class="form-control" value="%s" type="mail" name="mail" placeholder="Email_id"
                                    maxlength="30" required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <input class="form-control" style="height:85px;" value="%s" type="text" name="address" placeholder="Address"
                                    maxlength="500" required>
                            </div>
                            <div class="col-md-6">
                                <input class="form-control mb-2" value="%s" type="text" name="city" placeholder="City"
                                    maxlength="30" required>

                                        <input class="form-control" value="%s" type="text" name="state" placeholder="state"
                                    maxlength="30" required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <input class="form-control" value="%s" type="text" name="emtype" placeholder="Employment Type"
                                    maxlength="30" required>
                            </div>
                            <div class="col-md-6">
                                <input class="form-control" value="%s" type="number" name="salary" placeholder="Salary" maxlength="10"
                                    required>
                            </div>
                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                <input class="form-control" value="%s" type="text" name="uname" placeholder="Username"
                                    maxlength="20" required>
                            </div>

                            <div class="col-md-6">
                                <input class="form-control" value="%s" type="password" name="pwd"
                                    placeholder="Enter Password" required>
                            </div>

                        </div>
                        <div class="row pb-4">
                            <div class="col-md-6">
                                
                            </div>
                            <div class="col-md-3">
                                <input class="btn btn-outline-dark align-self-center mx-3 form-control" type="submit" name="update"
                                    value="Update" id="subRes">
                            </div>

                            <div class="col-md-3">
                                
                                <input type="reset" class="btn btn-dark form-control" value="Reset" id="subRes">
                            </div>
                        </div>
                    </form>""" %(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13]))
print("""
                </div>

            </div>
        </div>

    </body>

</html>
""")

import pymysql
import cgi,cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="erp")
cur = conn.cursor()

pupdate=form.getvalue("update")
if pupdate !=None:
    empid = form.getvalue("empid")
    name = form.getvalue("name")
    dob = form.getvalue("dob")
    role = form.getvalue("role")
    phone = form.getvalue("phone")
    mail = form.getvalue("mail")
    address = form.getvalue("address")
    city = form.getvalue("city")
    state = form.getvalue("state")
    emtype = form.getvalue("emtype")
    salary = form.getvalue("salary")
    uname = form.getvalue("uname")
    pwd = form.getvalue("pwd")

    q ="""update empreg set name='%s', dob='%s', role='%s', phone='%s', mail='%s', address='%s', city='%s', state='%s', emtype='%s', salary='%s', uname='%s', password='%s' where empid='%s'""" %(name,dob,role,phone,mail,address,city,state,emtype,salary,uname,pwd,empid)
    cur.execute(q)
    conn.commit()

    if(q):
        print("""
        <script>
        alert("Updated Successfully")
        location.href="./empupdate.py";
        </script>
        """)
    else:
        print("""
        <script>
        alert("Error!! Data not updated")
        location.href=./empupdateform.py?id=%s";
        </script>
        """ %(pid))

conn.close()