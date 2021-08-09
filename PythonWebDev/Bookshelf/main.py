
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
all_books = []

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(200), nullable = False)
    rating = db.Column(db.Float, nullable = False)

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        book = Book(
            title = data['b_name'], author=data['b_author'], rating=data['b_rating'])
        db.session.add(book)
        db.session.commit()
        print(type(book))
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/edit', methods=["POST", "GET"])
def edit():

    if request.method == "POST":
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit.html', book = book_selected)

@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    db.session.delete(book_selected)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)

