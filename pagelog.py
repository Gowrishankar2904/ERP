#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")


import cgi,cgitb
import pymysql

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur = conn.cursor()

form = cgi.FieldStorage()

print("""<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    
    <style>
        html,
        body {
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }

        body {
            background-image: url(./img/1767974.jpg);
            height: 100vh;
            width: 100%;
            background-size: cover;
            background-repeat: no-repeat;
            height: 100%;
        }

        #Lgninfo {
            padding-top: 60px;
            padding-bottom: 40px;
            border-radius: 250px;
            background-color: #fff9;
            border: 3px solid #0005;
        }

        #layout {
            border: 0px;
            position: relative;
            top: 10px;
        }

        #AdHrUname,
        #AdHrPwd,
        #ename,
        #epass {
            background-color: #0000;
            border: 0px;
            border-bottom: 2px solid rgb(1, 1, 80);
            border-radius: 0%;
            position: relative;
            bottom: 10px;
        }

        #sub,
        #close {
            background-color: #365486;
            position: relative;
            left: 180px;
            bottom: 35px;
            border-radius: 50px;

        }

        #sub,
        #close:hover {
            color: whitesmoke;
            background-color: rgb(3, 3, 27);
        }

        #logLinks {
            background-color: #0000;
        }

        #icon {
            color: #365486;
            position: relative;
            bottom: 65px;
            left: 340px;
        }

        .icon {
            text-align: left;
            color: #faf9f9;
        }

        .contact-article {
            background: #030000;
            left: 200px;
        }

        .article-title.contact-title {
            text-align: left;
            margin-bottom: 135px;
        }

        .contact-widget .cw-text {
            overflow: hidden;
            margin-bottom: 35px;

        }

        .contact-widget .cw-text i:hover {
            background: #b1c9ef;
            color: #ffffff;
        }

        .contact-widget .cw-text i {
            font-size: 30px;
            color: #f36100;
            display: inline-block;
            height: 65px;
            width: 65px;
            background: #628ecb;
            border-radius: 60%;
            line-height: 65px;
            text-align: center;
            float: left;
            margin-right: 20px;

        }

        .contact-widget .cw-text p {
            overflow: hidden;
            color: #c4c4c4;
            margin-bottom: 0;
            padding-top: 10px;
        }

        .contact-widget .cw-text ul {
            overflow: hidden;
            padding-top: 20px;
        }

        .contact-widget .cw-text ul li {
            list-style: none;
            font-size: 14px;
            color: #c4c4c4;
            margin-right: 25px;
            display: inline-block;
            position: relative;
        }

        .contact-widget .cw-text ul li:after {
            position: absolute;
            right: -18px;
            top: 0;
            content: "|";
            color: #545454;
        }

        .contact-widget .cw-text ul li:last-child {
            margin-right: 0;
        }

        .contact-widget .cw-text ul li:last-child:after {
            display: none;
        }

        .contact-widget .cw-text.email p {
            padding-top: 20px;
        }

        .img1 {
            text-align: right;
            width: 300px;
            height: 100px;
        }

        #contact-us {
            margin-top: 10px;
            left: 300px;
        }

        #contact-us .container-fluid .col-lg-6 {
            padding: 0px;
        }

        #contact-us .contact-form {
            padding: 80px;
            /* background-image: url(../images/contact-bg.jpg); */
            background-position: center center;
            background-repeat: no-repeat;
            background-size: cover;
        }

        #contact-us .contact-form #contact {
            background-color: #fff;
            padding: 40px;
            border-radius: 5px;
        }

        .contact-form input,
        .contact-form textarea {
            color: #7a7a7a;
            font-size: 13px;
            border: 1px solid #ddd;
            background-color: #fff;
            width: 100%;
            height: 40px;
            outline: none;
            line-height: 40px;
            padding: 0px 10px;
            -webkit-appearance: none;
            -moz-appearance: none;
            appearance: none;
            margin-bottom: 30px;
        }

        .contact-form textarea {
            height: 150px;
            resize: none;
        }

        .contact-form ::-webkit-input-placeholder {
            /* Edge */
            color: #7a7a7a;
        }

        .contact-form :-ms-input-placeholder {
            /* Internet Explorer 10-11 */
            color: #7a7a7a;
        }

        .contact-form ::placeholder {
            color: #7a7a7a;
        }

        .contact-form button {
            display: inline-block;
            font-size: 13px;
            padding: 11px 17px;
            background-color: #ed563b;
            color: #fff;
            text-align: center;
            font-weight: 400;
            text-transform: uppercase;
            transition: all .3s;
            border: none;
            outline: none;
            margin-top: -8px;
        }

        .mm {
            font-family: Arial, Helvetica, sans-serif;

        }

        .contact-form button:hover {
            background-color: #f9735b;
        }

        .main {
            margin: 0px;
            padding: 0px;
        }


        .map iframe {
            width: 100%;
            padding: 20px;
        }

        @media screen and (max-width: 768px) {
            .form {
                width: 400px;
                right: 50px;
            }
        }
    </style>
    <script>
        var AdHrUname, AdHrPwd;
        function validation() {
            AdHrUname = document.forms["AdHrLogin"]["AdHrUname"];
            AdHrPwd = document.forms["AdHrLogin"]["AdHrPwd"];

            if (AdHrUname.value == "") {
                alert("Please enter User name")
                AdHrUname.focus()
                return false;
            }

            if (AdHrPwd.value == "") {
                alert("Please enter your password")
                AdHrPwd.focus()
                return false;
            }

            if (AdHrUname.value == "Admin" && AdHrPwd.value == "Admin@1234") {
                alert("Login was sucessful.")
                return true;
            }

            if (AdHrUname.value == "HR" && AdHrPwd.value == "Hr@1234") {
                alert("Login was sucessful.")
                return true;
            }

            else {
                alert("Invalid data.")
                return false;
            }
        }
    </script>
</head>

<body>
    <!-- navbar -->
    <section>
        <div class="container-fluid bg-transparent">
            <ul class="navbar-nav align-items-end bg-transparent">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="Login" role="button" data-bs-toggle="dropdown">
                        Login
                    </a>
                    <ul class="dropdown-menu bg-transparent">
                        <li class="dropdown-item">
                            <a class="nav-link" href="#" id="employee" data-bs-toggle="modal"
                                data-bs-target="#EmployeeLogin">Employee</a>
                        </li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li class="dropdown-item">
                            <a class="nav-link" href="#" id="admin/hr" data-bs-toggle="modal"
                                data-bs-target="#AdminLogin">Admin/HR</a>
                        </li>
                    </ul>
                </li>
            </ul>

        </div>
    </section>
    <article>
        <section class="section" id="contact-us">
            <div class="container-fluid">
                <div class="col-lg-6">
                    <div class="contact-widget">
                        <div class="cw-text">
                            <i class="fa fa-mobile"><a href="www.linkedin.com/in/elayaprasatht"><img src="./img/linkedin.svg" alt=""></a></i>

                        </div>
                        <div class="cw-text email">
                            <i class="fa fa-envelope"><a href="https://mail.google.com/mail/u/0/#inbox?compose=new"><img src="./img/envelope.svg" alt=""></a></i>

                        </div>
                        <div class="cw-text email">
                            <i class="fa fa-envelope"><a href="https://www.facebook.com/login/"><img src="./img/facebook.svg" alt=""></a></i>

                        </div>
                        <div class="cw-text email">
                            <i class="fa fa-envelope"><a href="https://www.instagram.com/accounts/login/?hl=en"><img src="./img/instagram.svg" alt=""></a></i>

                        </div>
                    </div>
                </div>
    </article>

    <div class="modal fade" data-bs-backdrop="static" id="AdminLogin">
        <div class="modal-dialog">
            <div class="modal-content bg-transparent" id="layout">
                <div class="modal-body shadow" id="Lgninfo">
                    <center>
                        <h1 class="display-4" style="color:#0008; text-decoration:underline;">Login</h1>
                    </center>
                    <form action="./admindashboard.py" method="post" name="AdHrLogin" enctype="multipart/form-data"
                        onsubmit="return validation()">
                        <div class="m-5 form-group">
                            <input type="text" placeholder="User Name:" id="AdHrUname" name="AdHrUname"
                                class="form-control mb-4"><span id="icon"><i class="bi bi-person-circle"></i></span>
                            <input type="password" placeholder="Password:" minlength="5" maxlength="10" id="AdHrPwd"
                                name="AdHrPwd" class="form-control mb-4"><span id="icon"><i
                                    class="bi bi-lock-fill"></i></span>
                            <div class="mt-3">
                                <input type="submit" value="Login" name="sub" id="sub" class="btn btn-dark px-4 shadow">
                                <button class="btn btn-primary px-4 shadow" id="close"
                                    data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
    <div class="modal fade" data-bs-backdrop="static" id="EmployeeLogin">
        <div class="modal-dialog">
            <div class="modal-content bg-transparent" id="layout">
                <div class="modal-body shadow" id="Lgninfo">
                    <center>
                        <h1 class="display-4" style="color:#0009; text-decoration:underline;">Login</h1>
                    </center>
                    <form action="" method="post" name="EmployeeLogin" enctype="multipart/form-data">
                        <div class="m-5 form-group">
                            <input type="text" placeholder="User Name:" id="ename" name="EmpUname"
                                class="form-control mb-4"><span id="icon"><i class="bi bi-person-circle"></i></span>
                            <input type="password" id="epass" placeholder="Password:" name="EmpPwd"
                                class="form-control mb-4"><span id="icon"><i class="bi bi-lock-fill"></i></span>
                            <div class="mt-3">
                                <input type="submit" value="Login" name="submit" id="sub"
                                    class="btn btn-dark px-4 shadow">
                                <button class="btn btn-primary px-4 shadow" id="close"
                                    data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>


</body>

</html>""")

puserna =form.getvalue("EmpUname")
ppass =form.getvalue("EmpPwd")
psubmit =form.getvalue("submit")

if psubmit!=None:
    q="""select id from empreg where uname="%s" and password="%s" """%(puserna,ppass)
    cur.execute(q)


    res=cur.fetchone()

    if res!=None:
        print("""
        <script>
        alert("login success");
        location.href="empadd.py?id=%s"
        </script>""" %res[0])
    else:
        print("""
        <script>
        alert("enter valid data");
        </script>
        """)