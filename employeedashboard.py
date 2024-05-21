#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur = conn.cursor()

form = cgi.FieldStorage()

pid=form.getvalue("id")

q="""select * from empreg where id=%s """ %(pid)
cur.execute(q)

res=cur.fetchall()

for i in res:
    fn="Media/"+ i[14]

print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .image {
            padding-right: 100px;
            padding-top: 30px;
        }
    </style>
</head>

<body>
    <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
                <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                    <a href="/"
                        class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                        <span class="fs-5 d-none d-sm-inline">Menu</span>
                    </a>
                    <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                        id="menu">
                        <li class="nav-item">
                            <a href="#" class="nav-link align-middle px-0">
                                <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline">Home</span>
                            </a>
                        </li>
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="bi bi-person-plus-fill"></i> <span
                                    class="ms-1 d-none d-sm-inline">Employee</span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./tvb.py" class="nav-link px-0"> <span class="d-none d-sm-inline">View Employee
                                        </span>
                                    </a>
                                </li>
                                <li class="w-100">
                                    <a href="./empadd.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks">Update employee</span>
                                    </a>
                                </li>
                            </ul>
                        </li>
                
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i i class="bi bi-laptop"></i> <span
                                    class="ms-1 d-none d-sm-inline">Inventory</span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./employeeinventryreq.py" class="nav-link px-0"> <span class="d-none d-sm-inline">Inventry
                                            Request</span>
                                    </a>
                                </li>
                                <li class="w-100">
                                    <a href="./employeeinventryview.py" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks">view Inventory</span>
                                    </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="bi bi-toggle2-off"></i> <span class="ms-1 d-none d-sm-inline">Leave</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./leaveform.py" class="nav-link px-0"> <span class="d-none d-sm-inline">New
                                            Request</span>
                                    </a>
                                </li>
                                <li>
                                    <a href="./leaveview.py" class="nav-link px-0"> <span class="d-none d-sm-inline">Existing
                                            Request</span>
                                    </a>
                                </li>

                            </ul>
                        </li>
                        <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                            <i class="bi bi-currency-rupee"></i> <span class="ms-1 d-none d-sm-inline">Salary</span> </a>
                        <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                            <li class="w-100">
                                
                                <a href="./adminsalaryform.py" class="nav-link px-0"> <span class="d-none d-sm-inline">
                                        Salary Form</span>
                                </a>
                            </li>
                        </ul>
                         <a href="./pagelog.py" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                            <i class="bi bi-box-arrow-left"></i> <span class="ms-1 d-none d-sm-inline">Logout</span> </a>
                        <hr>
                       
                </div>
            </div>
            <div class="image">
<center>
           <img src="%s" height="200px" width="200px">

           <h3> Hello %s </h3></center>
           <center><h4>  %s </h4></center>
       </div>
 </div>           
   </div>
</table>
</body>
</html> """%(fn,i[2],i[1]))



