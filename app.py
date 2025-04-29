from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.route("/")
def base():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/student_list")
def student_list():
    return render_template("student_list.html")


@app.route("/deshdoard")
def deshboard():
    return render_template("deshboard.html")


@app.route("/")
def add_notes():
    return render_template("add_notes.html")


@app.route("/add_courses")
def add_courses():
    return render_template("add_courses.html")


@app.route("/add_student")
def add_student():
    return render_template("add_student.html")


@app.route("/student_stats")
def student_stats():
    return render_template("student_stats.html")

if __name__ == '__main__':
    app.run(debug=True)