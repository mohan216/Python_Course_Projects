from flask import Flask
import random as rand

app = Flask(__name__)

css_colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "gray",
    "teal"
]

@app.route("/")
def first_func():
    return f"<h1>Guess a number between 0 and 9</h1>" \
            "<img src ='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Numbers'></img>"


@app.route("/<num_entered>")
def checknumentered(num_entered):
    text_color = rand.choice(css_colors)
    if num == int(num_entered):
        return f"<h1 style='color: {text_color}'>You found me{num} and {num_entered}.</h1>" \
            "<img src ='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct number image'></img>"
    elif num < int(num_entered):
        return f"<h1 style='color: {text_color}'>Number too high{num} and {num_entered}.</h1>" \
               "<img src ='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Low number image'></img>"
    else:
        return f"<h1 style='color: {text_color}'>Number too low{num} and {num_entered}.</h1>" \
               "<img src ='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='Low number image'></img>"


if __name__ == "__main__":
    num = rand.randint(0, 9)
    app.run()

