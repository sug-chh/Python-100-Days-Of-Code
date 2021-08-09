from flask import Flask, render_template
import datetime as dt
import requests

time = dt.datetime.now()
year = time.year


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", current_year=year)


@app.route("/name/<name>")
def age_gender(name):
    gender_url = "https://api.genderize.io"
    age_url = "https://api.agify.io"
    query = {"name": name}
    response_gender = requests.get(gender_url, params=query).json()

    response_age = requests.get(age_url, params=query).json()

    return render_template(
        "guess.html",
        name=name,
        gender=response_gender["gender"],
        age=response_age["age"],
    )


@app.route("/blogs/<num>")
def get_blogs(num):
    blog_api = "https://api.npoint.io/2cef02f2542ee1166ghffd"
    response = requests.get(url=blog_api)
    blog_list = response.json()
    return render_template("blog.html", blog_list=blog_list)



if __name__ == "__main__":
    app.run(debug=True)
