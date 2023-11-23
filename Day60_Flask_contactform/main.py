from flask import Flask, render_template, request
import requests
# imports for sending email
import smtplib
import email
import datetime as dt

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


def send_email(sender, recipient, subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create an SMTP object
    smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

    # Start TLS encryption
    smtp_obj.starttls()

    # Login to the SMTP server
    password = "hkch hpst bfpw ceke"
    smtp_obj.login(sender, password)

    # Create a MIME message object
    msg = email.message.EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    # Send the email
    smtp_obj.send_message(msg)

    # Quit the SMTP session
    smtp_obj.quit()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        sender1 = request.form['email']
        recipient1 = "mohan_21688@yahoo.co.in"
        subject1 = "Email sent by contact" + " " + request.form['phone']
        body1 = request.form['name'] + "\n" + request.form['phone'] + "\n" +request.form['message']

        send_email(sender1, recipient1, subject1, body1)

        return render_template("contact.html", method=request.method)
    return render_template("contact.html")




# @app.route("/form-entry", methods=["POST"])
# def recieve_data():
#     return "<h1>Successfully sent your message</h1>"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
