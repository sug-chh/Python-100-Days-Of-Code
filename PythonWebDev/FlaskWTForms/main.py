from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(allow_empty_local=True)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8) ])
    submit = SubmitField(label='Login')


app = Flask(__name__)
app.secret_key = "this_ihouihouiuioeu"
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template('denied.html')
    return render_template('login.html', login_form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
