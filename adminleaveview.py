#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")


print("""<!DOCTYPE html>
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
                        <h1 class="display-4 fw-normal shadow-sm pb-2">Leave Request</h1>
                    </center>
                    <div class="col py-3">
                <table class="table table-dark table-hover table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">id</th>
                            <th scope="col">emp_name</th>
                            <th scope="col">Leave_type</th>
                            <th scope="col">Start_date</th>
                            <th scope="col">End_Date</th>
                            <th scope="col">Reason</th>
                            <th scope="col">status</th>
                        </tr>
                    </thead>""")
import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur=conn.cursor()

q1=""" select * from leave_form where Status="" """
cur.execute(q1)

rec=cur.fetchall()
for i in rec:
                   print(""" <tbody>
                        <tr>
                        <form method="post" name="leaveform">
                            <td><input type="text" name="leave" value="%s" readonly" style="border:none;"></td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td><input class="btn btn-success" type="submit" name="acpt" value="accept">
                            <input class="btn btn-danger" type="submit" name="rjct" value="reject"></td>
                        </form>
                        </tr>
                    </tbody>"""%(i[0],i[2],i[3],i[4],i[5],i[6]))
print("""</table>
 </div>
 </body>
 </html>""")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur=conn.cursor()

form=cgi.FieldStorage()

acpt = form.getvalue("acpt")
rjct = form.getvalue("rjct")
pleave = form.getvalue("leave")
pid= form.getvalue("emp_id")

if acpt!=None:
    q = """update leave_form set Status="Accept" where  id='%s' """%(pleave)
    cur.execute(q)
    conn.commit()

    print("""
      <script>
        alert("leave accepted successfully")
      </script>
     """)


if rjct!=None:
    q = """update leave_form set Status="Reject" where  id='%s' """%(pleave)
    cur.execute(q)
    conn.commit()

    print("""
        <script>
            alert("leave Rejected successfully")
        </script>
         """)
conn.close()
