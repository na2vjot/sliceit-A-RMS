from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as sql

conn=sql.connect(host='Localhost',user='root',passwd='',database='restaurant')
if conn.is_connected():
    print('successfully connected')

#creating feedback table if it doesnt exist
def create_feedback():
    c1=conn.cursor()
    create="""CREATE TABLE IF NOT EXISTS feedback(customer_id INT,feedback_text VARCHAR(100),Rating INT)"""
    c1.execute(create)

create_feedback()

#displaying existing feedbacks
def display_feedback():
    c1=conn.cursor()
    dquery="""select * from feedback ORDER BY Rating"""
    c1.execute(dquery)
    rows = c1.fetchall()
    for row in rows:
        print(row)
        
display_feedback()

#managing/entering new feedbacks
def manage_feedback():
    c1=conn.cursor()
    squery="""INSERT INTO feedback(customer_id,feedback_text,Rating) VALUES (%s, %s, %s)"""
    L1=[]
    C_ID=int(input('Enter the customer ID:'))
    L1.append(C_ID)
    Feedback=input('Please enter your feedback:')
    L1.append(Feedback)
    Rating=int(input('Please Rate Us:'))
    L1.append(Rating)
    c1.execute(squery,L1)
    print("Feedback Added.")
    
manage_feedback()
conn.commit() #commiting the changes made in db
