from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Click the buttom below to generate a random number between 0 and 100"
    return render_template("my-homepage.html", someText = message)

@app.route('/randnum')
def getNumber():
    randnum = randint(0,100)
    return render_template("numberpage.html", randnum)


if __name__ == '__main__':
    my_port = 5136
    app.run(host='0.0.0.0', port = my_port) 
