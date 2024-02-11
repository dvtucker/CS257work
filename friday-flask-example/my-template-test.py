from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index2.html")

@app.route('/randomName')
def getName():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")
    
    cur = conn.cursor()
    sql = "SELECT person_name FROM names_adjectives_table"
    cur.execute( sql )
    result = cur.fetchall()
    row = []
    for r in result:
        row.append(r[0])
    rand_name = str(r[random.randint(0,7)])
    rand_year = random.randint(1800, 2024)
    return render_template("random2.html", name = rand_name, year = rand_year)

if __name__ == '__main__':
    my_port = 5136
    app.run(host='0.0.0.0', port = my_port) 
