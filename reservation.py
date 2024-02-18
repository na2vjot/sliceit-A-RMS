from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="dbname"
)



# Create the database and table
def create_table():
    conn = mysql.connector.connect(db)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, time TEXT, status TEXT)''')    #creating tabeles in database
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    time = request.form['time']
    
    conn = mysql.connector.connect(db)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations (name, time, status) VALUES (?, ?, ?)", (name, time, 'Pending'))  #inserting values in database
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/queue')
def queue():
    conn = mysql.connector.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE status='Pending'")
    reservations = cursor.fetchall()
    conn.close()
    
    return render_template('queue.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True)
