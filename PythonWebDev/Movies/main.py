
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


THE_MOVIE_DB_URL = "https://api.themoviedb.org/3"
API_KEY = "Your Api Key"


class Update(FlaskForm):
    new_movie_rating = StringField(
        "Your Rating Out Of 10 eg. 7.5", validators=[DataRequired()]
    )
    new_review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class Add(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300))
    img_url = db.Column(db.String)


db.create_all()



@app.route("/")
def home():
    
    #This line of code give me the ascending data as an array:
    #all_movies = db.session.query(Movie).order_by('rating').all()
    #OR
    #all_movies = db.session.query(Movie).order_by(Movie.rating).all()

    #MY WAY OF SOLVING IT.
    # #This line of code gives me the data in objects
    # all_movies = db.session.query(Movie).order_by('rating')
    # ranking = all_movies.count()
    # for movie in all_movies:
    #     movie_to_update = Movie.query.get(movie.id)
    #     movie_to_update.ranking = ranking
    #     ranking = ranking - 1
    # db.session.commit()
    # return render_template("index.html", all_movies=all_movies)


    ##Angela's way of doing it using lesser lines of code
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()
    for n in range(len(all_movies)):
        all_movies[n].ranking = len(all_movies) - n
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = Update()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = request.form["new_movie_rating"]
        movie_to_update.review = request.form["new_review"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    add_movie = Add()
    if add_movie.validate_on_submit():
        new_movie_title = request.form['movie_title']
        params = {
            "api_key": API_KEY,
            "query": new_movie_title
        }
        response = requests.get(
            f"{THE_MOVIE_DB_URL}/search/movie", params=params)

        return render_template('select.html', results=response.json()['results'])
    return render_template('add.html', add_movie=add_movie)


@app.route('/find')
def find():
    params = {
        "api_key": API_KEY,
    }
    movie_id = request.args['id']
    movie_data = requests.get(
        f"{THE_MOVIE_DB_URL}/movie/{movie_id}", params=params).json()

    new_movie = Movie(
        title=movie_data['title'],
        year=movie_data['release_date'].split('-')[0],
        description=movie_data['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit',id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=True)
