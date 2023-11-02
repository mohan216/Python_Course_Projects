#"https://www.npoint.io/docs/c790b4d5cab58020d391" # url not giving json response properly
# 1. create a route for guess/<name>.
# 2. It should output the given message.
# " Hey <name>,"
# "I think you are (male or female)"
# "And maybe 63 years old"

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


@app.route("/blog")
def blog():
    blog_url = "https://www.npoint.io/docs/c790b4d5cab58020d391"# url not giving json response properly
    blog_resp = requests.get(blog_url)
    print(blog_resp.text)
    #blog_data = blog_resp.json()
    temp = ['hi', 'hello']
    return render_template('blog.html', blogs=temp)#, blogs=blog_data)


@app.route("/guess/<uname>")
def guess(uname):
    ageurl = f"https://api.agify.io?name={uname}"
    ageresponse = requests.get(ageurl)
    print(ageresponse)
    uage = ageresponse.json()['age']
    genderurl = f"https://api.genderize.io?name={uname}"
    genresponse = requests.get(genderurl)
    ugender = genresponse.json()['gender']
    return render_template('guess.html', name=uname, gender=ugender, age=uage)


if __name__ == "__main__":
    app.run()

