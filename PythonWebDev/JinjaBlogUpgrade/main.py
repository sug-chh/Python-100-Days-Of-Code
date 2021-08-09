from flask import Flask, request, flash
from flask.templating import render_template
import requests
import smtplib

MY_EMAIL = "hacksmith.info@gmail.com"
OWN_PASSWORD = "legion@8655"

response = requests.get("https://api.npoint.io/1180bd6a11ajgkgjfb06aa487")

blogs_posts = response.json()

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", posts = blogs_posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html', is_sent = False)
    else:
        data =  request.form
        send_email(name=data['name'], email=data['email'], ph_no=data['ph_no'], message=data['message'])
        return render_template("contact.html", is_sent = True)


@app.route('/post/<int:id>')
def get_post(id):
    for post in blogs_posts:
        if post['id'] == id:
            requested_post = post
            print(type(requested_post))
    return render_template('post.html', requested_post=requested_post)


def send_email(name, email, ph_no, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone Number: {ph_no}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message.encode(encoding="utf-8"))


if __name__ == "__main__":
    app.run(debug=True)



