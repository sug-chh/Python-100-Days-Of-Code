from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    location = StringField(label="Location on GMAPS (URL)",
                           validators=[DataRequired(), URL()])
    open = StringField(label="Opening Time e.g. 8AM",
                       validators=[DataRequired()])
    close = StringField(label="Closing Time e.g. 5:30PM",
                        validators=[DataRequired()])
    coffee = SelectField(label="Coffee Rating", validators=[
                         DataRequired()], choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"])
    wifi = SelectField(label="Wifi Strength Rating", validators=[
                       DataRequired()], choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power = SelectField(label="Power Socket Availability", validators=[
                        DataRequired()], choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label="Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding="utf-8") as cafe_data:
            cafe_data.write(f"\n{form.cafe_name.data},"
                            f"{form.location.data},"
                            f"{form.open.data},"
                            f"{form.close.data},"
                            f"{form.coffee.data},"
                            f"{form.wifi.data},"
                            f"{form.power.data},"
                            )
        return redirect(url_for(endpoint='cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
