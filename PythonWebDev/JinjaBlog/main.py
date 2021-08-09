from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/2cef02f2542ee1166jkjh").json()

post_objects = []
for post in posts:
    post_obj = Post(id=post["id"], title=post["title"], body=post['body'], subtitle=post['subtitle'])
    post_objects.append(post_obj)







app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = post_objects)

@app.route('/blog/<int:id>')
def get_blog(id):
    return render_template('post.html', id=id, all_posts = post_objects)

# Alternative method:
# @app.route('/blog/<int:id>')
# def get_blog(id):
#     for post in post_objects:
#         if post.id == id:
#             requested_post = post
#     return render_template('post.html', requested_post = requested_post)



if __name__ == "__main__":
    app.run(debug=True)
