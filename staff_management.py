from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql

conn=sql.connect(host='Localhost',user='root',passwd='password',database='restaurant')
if conn.is_connected():
    print('successfully connected')

#creating staff table if it doesnt exist
def create_staff():
    c1=conn.cursor()
    create="""CREATE TABLE IF NOT EXISTS staff_management(staff_id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(50),Role VARCHAR(50),age INT,contact_number VARCHAR(50),salary INT)"""
    c1.execute(create)

create_staff()

#displaying existing staff details
def display_staff():
    c1=conn.cursor()
    dquery="""select * from staff_management ORDER BY SALARY DESC"""
    c1.execute(dquery)
    rows = c1.fetchall()
    for row in rows:
        print(row)

display_staff()

#managing/entering new staff details
def manage_staff():
    c1=conn.cursor()
    squery="""INSERT INTO staff_management(name,Role,age,salary,contact_number) VALUES (%s, %s, %s,%s,%s)"""
    L1=[]
    name=input('enter the name of the employee:')
    L1.append(name)
    role=input('enter the role of the employee:')
    L1.append(role)
    age=int(input('enter age of employee:'))
    L1.append(age)
    salary=int(input('salary of the employee:'))
    L1.append(salary)
    contact_number=input('enter the contact number:')
    L1.append(contact_number)
    c1.execute(squery,L1)
    print("Employee added successfully.")



manage_staff()
conn.commit() #commiting the changes made in db
