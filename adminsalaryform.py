#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")


import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur=conn.cursor()

q1=""" select * from sal """
cur.execute(q1)

form=cgi.FieldStorage()

pid=form.getvalue("id")

rec=cur.fetchall()

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

        .navbarr{
           background-color: rgb(3, 3, 27);
           color: orangered;
           opacity: 1.0;
           max-width: 270px
        }

        *,
            body,
            html {
                padding: 0px;
                margin: 0px;
                box-sizing: border-box;
            }

            #sidenav {
                background-color: rgb(3, 3, 34);
                opacity: 1.0;
                max-width: 270px
            }

            #sidenavLinks {
                color: orangered;
                font-weight: 550;
            }

            #accept {
                border-radius: 20px;
                width:105px;
            }

            .move{
            margin-top:-650px
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
</head>""")
print("""
<body>
      <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0  navbarr">
                <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                    <a href="/"
                        class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                        <span class="fs-5 d-none d-sm-inline"><class style="color: grey;"><h3><b><u>ELNO TECH</u></b></h3></span>
                    </a>""")
print("""
                    <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                        id="menu">
                        <li class="nav-item">
                            <a href="./empadd.py?id=%s" class="nav-link align-middle px-0">
                                <i class="bi bi-house"></i> <span class="ms-1 d-none d-sm-inline" id="sidenavLinks">Home</span>
                            </a>
                        </li>""" % (pid))
print("""
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="bi bi-person-plus-fill"></i> <span
                                    class="ms-1 d-none d-sm-inline"
                                     id="sidenavLinks">Employee</span>
                            </a>""")
print("""
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./tvb.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                        id="sidenavLinks">View Employee
                                        </span>
                                    </a>
                                </li>""" % (pid))
print("""
                                <li class="w-100">
                                    <a href="./empadd.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks">Update employee</span>
                                    </a>
                                </li>
                            </ul>
                        </li>""" % (pid))
print("""
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="bi bi-card-list"></i> <span class="ms-1 d-none d-sm-inline" id="sidenavLinks">Task</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./emptask.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">Assign
                                            Task</span>
                                    </a>
                                </li>""" % (pid))
print("""
                                <li>
                                    <a href="./emprevtask.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">Review
                                            Task</span>
                                    </a>
                                </li>

                            </ul>
                            </li>""" % (pid))
print("""

                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i i class="bi bi-laptop"></i> <span
                                    class="ms-1 d-none d-sm-inline" id="sidenavLinks">Inventory</span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./employeeinventryreq.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">Inventry
                                            Request</span>
                                    </a>
                                </li> """ % (pid))
print("""
                                <li class="w-100">
                                    <a href="./employeeinventryview.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline"
                                            id="sidenavLinks">view Inventory</span>
                                    </a>
                                </li>
                            </ul>
                        </li> """ % (pid))
print("""
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="bi bi-toggle2-off"></i> <span class="ms-1 d-none d-sm-inline" id="sidenavLinks">Leave</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./leaveform.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">New
                                            Request</span>
                                    </a>
                                </li>""" % (pid))
print("""
                                <li>
                                    <a href="./leaveview.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">Existing
                                            Request</span>
                                    </a>
                                </li>

                            </ul>
                            </li>""" % (pid))
print("""

                        <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                            <i class="bi bi-currency-rupee"></i> <span class="ms-1 d-none d-sm-inline" id="sidenavLinks">Salary</span> </a>
                        <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                            <li class="w-100">

                                <a href="./adminsalaryform.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">
                                        Salary Form</span>
                                </a>
                            </li>
                        </ul>""" % (pid))

print("""
                         <a href="./pagelog.py" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                            <i class="bi bi-box-arrow-left"></i> <span class="ms-1 d-none d-sm-inline" id="sidenavLinks">Logout</span> </a>
                         </div>
                </div>
                
                """)
print("""
            <div class="col p-4">
                    <center>
                        <h2
                            style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">
                            Salary View</h2>
                    </center><br>
                <table class="table table-dark table-hover table-bordered">
                    <thead>
                        <tr>
                            <th scope="col">empid</th>
                            <th scope="col">name</th>
                            <th scope="col">year</th>
                            
                            <th scope="col">month</th>
                            <th scope="col">salary</th>
                            <th scope="col">wdays</th>
                            <th scope="col">pdays</th>
                            <th scope="col">leave_taken</th>
                            <th scope="col">gross_salary</th>
                        </tr>
                    </thead>""")
for i in rec:
                   print(""" <tbody>
                        <tr>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                            <td>%s</td>
                        </tr>
                    </tbody>"""%(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
print(""" </table>
            </div>
        </div>
    </div>
</body>

</html>""")

conn.commit()
conn.close()