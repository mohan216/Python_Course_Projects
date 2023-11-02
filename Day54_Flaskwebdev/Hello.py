from flask import Flask

app = Flask(__name__)


def make_bold(func):
    # def wrapper(**kwargs):
    #      #bold_name = f"<b>{args[0]}</b>"
    #      return "<b>"+func(kwargs[0])+"</b>"
    # return wrapper
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper


def logging(func):
    def wrapper(*args, **kwargs):
        print(f"You called function {func.__name__}")
        temp = func(*args, **kwargs)
        print(f"The output is {temp}")
        return
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/check/<name>")
@make_bold
def check_name(name):
    return f"User name is Mr.{name}" \
           "<H1> This is next line </H1>" \
           "<H3> This is third line </H3>"


@logging
def a_func(a, b, c):
    return a * b * c


if __name__ == "__main__":
    input_str = input()  # Read the input as a string
    nums = [int(num) for num in input_str.split()]  # Split the input string into a list of integers
    a_func(nums[0], nums[1], nums[2])
    print("Hi")
    app.run(debug="True")


# I see the issue now. The problem is that you're trying to run both the console input and the Flask server in the same script, and this can lead to a conflict. The `input()` function for console input is blocking, and it prevents the server from running properly.
#
# If you want to run both the console input and the Flask server, you should do so in separate threads or processes. You can use Python's `threading` module to run the Flask server in a separate thread. Here's an example of how you can do it:
#
# ```python
# from flask import Flask
# import threading
#
# app = Flask(__name)
#
# # Your decorator, routes, and functions go here...
#
# if __name__ == "__main__":
#     input_thread = threading.Thread(target=read_input_and_run_server)
#     input_thread.start()
#
# def read_input_and_run_server():
#     input_str = input("Enter input: ")  # Read the input as a string
#     nums = [int(num) for num in input_str.split()]  # Split the input string into a list of integers
#     a_func(nums[0], nums[1], nums[2])
#     print("Hi")
#     app.run(debug=True)  # Start the Flask server
# ```
#
# With this code, the Flask server will run in a separate thread, allowing you to use the console input as well as run the server. The `read_input_and_run_server` function is responsible for reading input and starting the server in a new thread.