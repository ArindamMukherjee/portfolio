# app.py
import pymysql
from flask import Flask, render_template, jsonify
from database1 import load_data_from_db

app = Flask(__name__)

skills = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Java'},
    {'id': 3, 'name': 'JavaScript'},
    {'id': 4, 'name': 'C++'},
    {'id': 5, 'name': 'HTML'},
    {'id': 6, 'name': 'CSS'}
]


@app.route("/skills")
def show_skills():
  # skills  = load_skills_from_db()
  return render_template("skills.html", skills = skills)


@app.route("/")
def home_page():
    data = load_data_from_db()
    return render_template("home.html", projects=data)


@app.route("/api/projects")
def show_json():
    data = load_data_from_db()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)


