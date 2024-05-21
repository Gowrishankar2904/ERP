#!C:/Users/Elaya Prasath/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="erp")
cur = conn.cursor()

form = cgi.FieldStorage()

pid=form.getvalue("id")

q="""select * from emp_details where id=%s """ %(pid)
cur.execute(q)

res=cur.fetchall()
print("""
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
   <div>
   
       <img src="%s" height="400px" width="400px">
       
       <h3> im %s </h3>
   </div>
</body>

</html>

"""%(i[1]))