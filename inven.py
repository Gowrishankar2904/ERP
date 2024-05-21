#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb

form = cgi.FieldStorage()

pid = form.getvalue("id")

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
    <script>
        function calculateDays() {
            const startDate = new Date(document.getElementById('start-date').value);
            const endDate = new Date(document.getElementById('end-date').value);
            const resultTextBox = document.getElementById('result');

            if (startDate && endDate) {
                const difference = Math.abs(endDate - startDate);
                const daysDifference = Math.ceil(difference / (1000 * 60 * 60 * 24));
                resultTextBox.value = daysDifference;
            } else {
                resultTextBox.value = '';
            }
        }
    </script>
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
                    </div>
                </div>""")
cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="erp")
cur = conn.cursor()

q = """select * from empreg where empid="%s" """ % (pid)
cur.execute(q)
res = cur.fetchall()

for i in res:
    Emp = i[1]

    print("""
            <div class="container col-6">
               <center> <h1 class="mb-3">Employee Leave Form</h1></center>

                <form name="loginform" onsubmit="return login()" onchange="remdays();">
                <div class="mb-3">
                        <label for="Id" class="form-label">Id</label>
                        <input type="number" class="form-control" name="lid" id="Id" placeholder="ID">
                    </div>
                    <div class="mb-3">
                        <label for="employeeId" class="form-label">Employee Id</label>
                        <input class="form-control type="text" name="emp" value="%s" readonly maxlength="20" required>
                    </div>""" % (Emp))
    print("""
                    <div class="mb-3">
                        <label for="employeeName" class="form-label">Employee Name</label>
                        <input type="text" class="form-control" name="lname" id="employeeName" placeholder="Enter your name">
                    </div>

                    <div class="mb-3">
                        <label for="leaveType" class="form-label">Leave Type</label>
                        <select class="form-select" id="leaveType" name="ltype">
                            <option selected>Select leave type</option>
                            <option value="sickLeave">Sick Leave</option>
                            <option value="vacation">Vacation</option>
                            <option value="personal">Personal</option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="startDate" class="form-label">Start Date</label>
                        <input type="date" name="from" class="form-control" id="start-date" oninput="calculateDays()" >
                    </div>

                    <div class="mb-3">
                        <label for="endDate" class="form-label">End Date</label>
                        <input type="date" class="form-control" name="to" id="end-date" oninput="calculateDays()" >
                    </div>

                    <div class="mb-3">
                        <label for="reason" class="form-label">Reason for Leave</label>
                        <textarea class="form-control" id="reason" rows="3" name="lreason"
                            placeholder="Enter the reason for your leave"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="total" class="form-label">Total Days</label>
                        <input type="text" class="form-control" name="days" id="result" readonly></textarea>
                    </div>
                    <!-- ... (unchanged form elements) ... -->
                    <input class="form-control btn btn-info" type="submit" name="login" value="apply">
                </form>
            </div>
        </div>
      </div>
     </body>
    
     </html>
     """)

import pymysql
import cgi, cgitb, os
import smtplib

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="erp")
cur = conn.cursor()

form = cgi.FieldStorage()

lid = form.getvalue("lid")
lempid = form.getvalue("emp")
lname = form.getvalue("lname")
ltype = form.getvalue("ltype")
sdate = form.getvalue("from")
edate = form.getvalue("to")
lrsn = form.getvalue("lreason")
total = form.getvalue("days")
sub = form.getvalue("login")

if len(form) != 0:
    q = """insert into leave_form (id,empid,empname,leavetype,sdate,edate,reason,tdays)
         values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (
        lid, lempid, lname, ltype, sdate, edate, lrsn, total)
    cur.execute(q)
    conn.commit()
    print("""
            <script>
            alert("Data inserted successfully")
            </script>
            """)