from flask import Flask, render_template, request, redirect, url_for
import datetime
import mysql.connector as sql

conn=sql.connect(host='Localhost',user='root',passwd='password',database='restaurant') #create a database in mysql named restaurant and connect it here
if conn.is_connected():
    print('successfully connected')

#creating a reservations table if it doesnt exist
def create_reservations():
    c1=conn.cursor()
    c1.execute('create table if not exists reservations(name VARCHAR(50),TIME TIME,status VARCHAR(50) DEFAULT "RESERVED",EMAIL_ID VARCHAR(50),contact VARCHAR(50))')

class reserve:
     def __init__(self, capacity, reservation_start_time, reservation_end_time):
        self.capacity = capacity
        self.reservations = 0
        self.reservation_start_time = reservation_start_time
        self.reservation_end_time = reservation_end_time

     def create_reservations(self):
            c1=conn.cursor()
            rquery="""INSERT INTO Reservations(name,time,email_id,contact) VALUES (%s, %s, %s,%s)"""
            L1=[]
            name=input('enter your name:')
            L1.append(name)
            time=input("time of your reservation(in HH:MM:SS format):")
            L1.append(time)
            email_id=input('enter your email_id:')
            L1.append(email_id)
            contact=input('enter your contact:')
            L1.append(contact)
            c1.execute(rquery,L1)
            current_time = datetime.datetime.now().time()
            if (current_time >= self.reservation_start_time) and (current_time <= self.reservation_end_time):
                    if self.reservations < self.capacity:
                        print("Reservation successful! Enjoy your meal.")
                        self.reservations += 1
                    else:
                        print("Sorry, the restaurant is full. No more reservations can be made.")
            else:
                print("Reservation is only available between 10:00 AM to 8:00 PM")        #reservation can only be done within this time limit
     def check_availability(self):
             return self.capacity - self.reservations
     
reservation_start_time = datetime.time(10, 0)  # Set reservation start time to 10:00 AM
reservation_end_time = datetime.time(20, 0) #reservation tome ends at 8:00 pm
reserve = reserve(2, reservation_start_time, reservation_end_time) #capacity of restaurant with set time
for i in range(3):
    reserve.create_reservations()


def display_reservations():
    c1=conn.cursor()
    dquery="""select * from reservations ORDER BY NAME""" #displays reserved lists in alphabetical order
    c1.execute(dquery)
    rows = c1.fetchall()
    for row in rows:
        print(row)

create_reservations()
 
print("Remaining availability:", reserve.check_availability())  
display_reservations()
conn.commit()


