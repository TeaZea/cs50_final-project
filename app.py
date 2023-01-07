import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Add the user's entry
        name = request.form.get("name")
        todo = request.form.get("todo")

        db.execute("INSERT INTO list (name, todo) VALUES (?, ?)", name, todo)

        return redirect("/")

    else:

        # Display the entries
        todos = db.execute("SELECT * FROM list")

        # return render_template("index.html", todos=todos)
        return render_template("index.html", todos=todos)


@app.route("/delete", methods=["POST"])
def delete():
    # delete
    id = request.form.get("item_id")
    if id:
        db.execute("DELETE FROM list WHERE id = ?", id)

    return redirect("/")
