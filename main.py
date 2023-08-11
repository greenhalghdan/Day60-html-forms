from flask import Flask, render_template, request
import requests


app = Flask(__name__)
print(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login/", methods=["post"])
def receive_data():
    name = request.form['username']
    password = request.form['password']
    return f"<h1>name: {name} password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)