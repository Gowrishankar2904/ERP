#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb
from datetime import date

today = date.today()
year = today.year

form = cgi.FieldStorage()

pid = form.getvalue("id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!------ Include the above in your HEAD tag ---------->


    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">

    <link rel="icon" type="image/x-icon" href="./media/logoonly.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">

    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!------ Include the above in your HEAD tag ---------->

    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="./media/logoonly.png">
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">


    <style>
         *,
            body,
            html {
                padding: 0px;
                margin: 0px;
                box-sizing: border-box;
            }

            #sidenav {
                background-color: #000;
                opacity: 1.0;
                max-width: 270px
            }

            #sidenavLinks {
                color: white;
                font-weight: 600;
            }
    </style>

    <script type="text/javascript">
     function calc(){
     var ch=loginform.mon.selectedIndex;
     if(ch==0)
        loginform.wdays.value="31";
        if(ch==1)
        loginform.wdays.value="28";
        if(ch==2)
        loginform.wdays.value="31";
        if(ch==3)
        loginform.wdays.value="30";
        if(ch==4)
        loginform.wdays.value="31";
        if(ch==5)
        loginform.wdays.value="30";
        if(ch==6)
        loginform.wdays.value="31";
        if(ch==7)
        loginform.wdays.value="31";
        if(ch==8)
        loginform.wdays.value="30";
        if(ch==9)
        loginform.wdays.value="31";
        if(ch==10)
        loginform.wdays.value="30";
        if(ch==11)
        loginform.wdays.value="31";
    }
    function remdays(){
    var wdays=parseInt(loginform.wdays.value);
    var ldays=parseInt(loginform.pleave_taken.value);
    var perdays=wdays-ldays;
    loginform.pdays.value=perdays;    
    }

    function gross(){
    var sal=parseInt(loginform.salary.value);
    var present=parseInt(loginform.pdays.value);
    var work=parseInt(loginform.wdays.value);
    var gross=Math.round((sal * present)/work);
    loginform.gross_salary.value=gross;    
    }
</script>
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
                            <a href="#" class="nav-link align-middle px-0 active">
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
                                    <a href="#" class="nav-link px-0"> <span id="sidenavLinks">Remove
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
                                    <a href="#" class="nav-link px-0"> <span id="sidenavLinks"> Create New
                                            Task</span>
                                    </a>
                                </li>
                                <hr class="dropdown-divider text-white">
                                <li>
                                    <a href="#" class="nav-link px-0"> <span id="sidenavLinks"> Review
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
                                    <a href="#" class="nav-link px-0"> <span class="d-none d-sm-inline"
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
                                <a href="./view.py" class="nav-link px-0"> <span class="d-none d-sm-inline" id="sidenavLinks">
                                        
                                        Salary Form</span>
                                </a>
                            </li>
                        </ul>
                        <hr>

                </div>
            </div class=" col">
            
            <div class="col col-sm-5" 
""")
cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="erp")
cur = conn.cursor()

q = """select * from empreg where id="%s" """ % (pid)
cur.execute(q)
res = cur.fetchall()

for i in res:
    salary = i[11]
    Emp = i[1]
    name = i[2]

    print("""
        <div style="margin-left:210px;">
        <form style="margin-top:50px;" name="loginform" onsubmit="return login()">
        <div>
            <div class="col">
                <span onclick="document.getElementById('more').style.display='none'">
                 <center><h3> SALARY FORM </h3></center>
        </div>

        <!-- model -->
        <div class="col-md-5"></div>
        <div clss="col-md-4 mar" style="padding:50px;">
            <div class="input-container">
      <input class="form-control type="text" name="emp" value="%s" readonly maxlength="20" required><br>
      """ % (Emp))
    print("""
          <input class="form-control type="text" name="name" value="%s" readonly maxlength="20" required><br>
          """ % (name))

    print("""
      <input class="form-control type="text" name="year" value="%s" readonly maxlength="20" required><br>
      """ % (year))
    print("""
        <select class="form-control" type="date" name="mon" maxlength="20" onchange="calc();remdays();gross();" required><br>
        <option value="Jan">Jan</option>
        <option value="Feb">Feb</option>
        <option value="March">March</option>
        <option value="April">April</option>
        <option value="May">May</option>
        <option value="June">June</option>
        <option value="July">July</option>
        <option value="Aug">Aug</option>
        <option value="Sep">Sep</option>
        <option value="Oct">Oct</option>
        <option value="Nov">Nov</option>
        <option value="Dec">Dec</option>
        </select><br>
    """)

    print("""
    <input class="form-control" type="text" value="%s" name="salary" readonly placeholder="Salary" maxlength="20" required><br>
    """ % (salary))
    print("""
    <input class="form-control" type="text" name="wdays"   placeholder="Working days" maxlength="20" required><br>
    <input class="form-control" type="text" name="pdays"  placeholder="Present days" maxlength="20" required><br>
    """)

    q1 = """select * from leave_form where empid="%s" """ % (Emp)
    cur.execute(q1)
    r = cur.fetchall()

    for i in r:
     print(""" <input class="form-control" type="text" readonly name="pleave_taken" value="%s" placeholder="Leave taken" maxlength="20" required><br>""" % i[7])
     print("""
                <input class="form-control" type="text" name="gross_salary"  placeholder="Gross Salary" maxlength="20" required><br>
                <input class="form-control btn btn-info" type="Submit" name="login" value="submit"><br><br><br>
                </form>
        """)
    print("""
</table>
</div>
</body>
</html>
""")
    print("""
             </div>   
            </div>
        </div>
    </div>
</body>

</html>
      """)



import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", database="erp")
cur = conn.cursor()

q1 = """select * from sal"""
cur.execute(q1)
r = cur.fetchall()

form = cgi.FieldStorage()

pemailid = form.getvalue("emp")
pname = form.getvalue("name")
pyear = form.getvalue("year")
pmonth = form.getvalue("mon")
psalary = form.getvalue("salary")
pwdays = form.getvalue("wdays")
ppdays = form.getvalue("pdays")
pleave = form.getvalue("pleave_taken")
pgross_salary = form.getvalue("gross_salary")
psubmit = form.getvalue("login")
if psubmit != None:
    q = """insert into sal(empid,name,year,month,salary,wdays,pdays,leave_taken,gross_salary) 
    values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (pemailid,pname,pyear, pmonth, psalary, pwdays, ppdays, pleave, pgross_salary)
    cur.execute(q)
    print("""
    <script>
    alert("salary calculated");
    </script>
    """)

conn.commit()
conn.close()