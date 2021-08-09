from flask import Flask
import random

app = Flask(__name__)
ran_no = random.randint(0, 9)
@app.route("/")
def home_page():
    return "<h1>Guess a number between 0 and 9</h1><img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'/>"


@app.route("/<int:num>")
def guessing_page(num):
    
    if num == ran_no:
        return "<h1 style='color:green'>You found me!</h1><img src='https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp'/>"
    elif num > ran_no:
        return "<h1 style='color: purple'>Too high try again!</h1><img src='https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp'/>"
    else:
        return "<h1 style='color: red'>Too low try again!</h1><img src='https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp'/>"
    


app.run(debug=True)