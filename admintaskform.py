#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb
import os

# cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="erp")
cur = conn.cursor()

q1 = """select max(id) from task"""
cur.execute(q1)
r = cur.fetchone()

# print(r)
if r[0] != None:
    n = r[0]
else:
    n = 0

# print(n)

y = ""

if n < 9:
    y = "000"
elif n >= 10 and n <= 99:
    y = "00"
elif n >= 100 and n <= 999:
    y = "0"
taskid = "Task" + y + str(n + 1)

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
                        <h1 class="display-4 fw-normal shadow-sm pb-2 mb-5">New Task</h1>
                    </center>

                    <form action="#" method="post" name="taskForm" class="px-2 shadow-sm" enctype="multipart/form-data">
                        <div class="row pb-4 form-group">
                            <div class="col-md-4">
                                <label for="TaskId" class="form-label">Task Id: </label>""")
print("""
                                <input type="text" name="taskid" value="%s" class="form-control" readonly>
                            </div>""" % taskid)

form = cgi.FieldStorage()
pid = form.getvalue("id")

q2 = """select* from empreg where id="%s" """ % (pid)
cur.execute(q2)
res = cur.fetchall()

for i in res:
    Empid = i[1]
    Ename = i[2]
    Eemail = i[6]
    print("""
                                <div class="col-md-4">
                                    <label for="EmpId" class="form-label">Employee Id: </label>
                                    <input type="text" name="empid" value="%s" readonly class="form-control">
                                </div>""" % i[1])
    print("""
                                <div class="col-md-4">
                                    <label for="name" class="form-label">Employee Name: </label>
                                    <input type="text" name="name" value="%s" readonly class="form-control">
                                </div>""" % i[2])
    print("""
                        </div>
                        <div class="row form-group pb-4">
                        <div class="col-md-6">
                            <label for="" class="form-label">Importance Level: </label>
                                <select class="form-control" type="text" name="level" maxlength="20" required>
                                    <option value="" disabled selected>Select</option>
                                    <option value="normal">Normal</option>
                                    <option value="important">Important</option>
                                    <option value="very_important">Very Important</option>
                                    <select>
                            </div>
                            <div class="col-md-6">
                                <label for="file" class="form-label">Files: </label>
                                <input class="form-control" type="file" name="docs"
                                    placeholder="Upload files" required>
                            </div>

                        </div>
                        <div class="row form-group pb-4">
                            <div class="col-md-12">
                                <textarea name="comments" id="" cols="" rows="3" class="form-control"></textarea>
                            </div>
                        </div>
                        <div class="row formgroup pb-5">""")
    print("""
                        <div class="col-md-6">
                        <input type="mail" class="form-control" name="email" value="%s" readonly required>
                        </div>""" % i[6])
print("""
                            <div class="col-md-6 px-5">
                                <input type="submit" name="sub" value="Assign Task" class="px-2 py-1 mx-2">
                                <input type="reset" value="Clear Field" class="px-2 py-1 mx-2">
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </body>

</html>""")

if len(form) != 0:
    tid = form.getvalue("taskid")
    empid = form.getvalue("empid")
    ename = form.getvalue("name")
    tlevel = form.getvalue("level")
    tabout = form.getvalue("comments")
    emmail = form.getvalue("email")
    esub = form.getvalue("sub")
    efile = form['docs']
    if efile.filename:
        fs = os.path.basename(efile.filename)
        open("media/" + fs, "wb").write(efile.file.read())
        q3 = """insert into task (taskid,empid,name,level,about,file) values('%s','%s','%s','%s','%s','%s')""" % (
            tid, empid, ename, tlevel, tabout, fs)

        cur.execute(q3)
        conn.commit()

        print("""
        <script>
        alert("Task Assigned successfully");
        location.href="empshow.py";
        </script>
        """)

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = 'riyas.rio18@gmail.com'
        password = 'slqfwacxpoyokozd'
        toaddr = emmail

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        msg['Subject'] = "Regarding Task"
        body = "Hi {}".format(ename)

        msg.attach(MIMEText(body, 'plain'))

        filename = efile.filename
        attachment = open("media/" + filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)
        s.quit()

conn.close()