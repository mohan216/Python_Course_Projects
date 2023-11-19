from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
all_posts = response.json()
print(all_posts)

@app.route("/")
def home():
    return render_template('index.html', allposts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:p_id>")
def post(p_id):
    return render_template("post.html", post=all_posts[p_id-1])


if __name__ == "__main__":
    app.run(debug='True')
