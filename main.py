import sqlite3

conn= sqlite3.connect("new_db")

print("Enter the Employeeid")
r=input()
print("Enter the employee city")
ct=input()
print("Enter employee name")
nm= input()

query= "insert into employee_data(employeeid,employeecity,employeename) values (" + r + ",'" + nm + "','" + ct +"')"

conn.execute(query)
conn.commit()
conn.close()

print("Data Saved")

