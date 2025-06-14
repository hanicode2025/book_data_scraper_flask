from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route("/")
def book_list():
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            books = json.load(f)
    except Exception as e:
        print("Error loading books.json:", e)
        books = []

    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
