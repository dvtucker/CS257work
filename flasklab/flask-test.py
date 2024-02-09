import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    the_sum = num1 + num2
    return str(the_sum)

@app.route('/pop/<abbrev>')
def state_pops(abbrev):
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="tuckerd",
        user="tuckerd",
        password="carpet664winter")

    cur = conn.cursor()

    abbr = abbrev
    sql = "SELECT state_population FROM state_table WHERE abbreviation = '" + abbr + "';"
    
    cur.execute( sql )
    result = cur.fetchone()

    return result

if __name__ == '__main__':
    my_port = 5136
    app.run(host='0.0.0.0', port = my_port) 