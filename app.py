from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db
import sqlite3
import announcements

app = Flask(__name__)
app.secret_key = config.secret_key


@app.route("/")
def index():
    all_announcements = announcements.get_announcements()
    return render_template("index.html", announcements=all_announcements)

@app.route("/find_announcement")
def find_announcement():
    query = request.args.get("query")
    if query:
        results = announcements.find_announcements(query)
    if not query:
        query = ""
        results = []
    return render_template("find_announcement.html", query=query, results=results)

@app.route("/page/<int:announcement_id>")
def show_announcement(announcement_id):
    announcement = announcements.get_announcement(announcement_id)
    if not announcement:
        abort(404)
    return render_template("show_announcement.html", announcement=announcement)

@app.route("/new_announcement")
def new_item():
    return render_template("new_announcement.html")

@app.route("/create_announcement", methods=["POST"])
def create_announcement():
    title = request.form["title"]
    description = request.form["description"]
    vähimmäismäärä = request.form["vähimmäismäärä"]
    user_id = session["user_id"]

    announcements.add_announcement(title, description, vähimmäismäärä, user_id)

    return redirect("/")

@app.route("/edit_announcement/<int:announcement_id>")
def edit_announcement(announcement_id):
    announcement = announcements.get_announcement(announcement_id)
    if not announcement:
        abort(404)
    if announcement["user_id"] != session["user_id"]:
        abort(403)
    return render_template("edit_announcement.html", announcement=announcement)

@app.route("/update_announcement", methods=["POST"])
def update_announcement():
    announcement_id = request.form["announcement_id"]
    announcement = announcements.get_announcement(announcement_id)
    if not announcement:
        abort(404)
    if announcement["user_id"] != session["user_id"]:
        abort(403)
    title = request.form["title"]
    description = request.form["description"]
    vähimmäismäärä = request.form["vähimmäismäärä"]

    announcements.update_announcement(announcement_id, title, description, vähimmäismäärä)

    return redirect("/page/" + str(announcement_id))

@app.route("/remove_announcement/<int:announcement_id>", methods=["GET", "POST"])
def remove_announcement(announcement_id):
    if request.method == "GET":
        announcement = announcements.get_announcement(announcement_id)
        if not announcement:
            abort(404)
        if announcement["user_id"] != session["user_id"]:
                abort(403)
        return render_template("remove_announcement.html", announcement=announcement)

    if request.method == "POST":
        if "remove" in request.form:
            announcements.remove_announcement(announcement_id)
            return redirect("/")
        else:
            return redirect("/page/" + str(announcement_id))



@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"
    password_hash = generate_password_hash(password1)

    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username]) [0]
        user_id = result["id"]
        password_hash = result["password_hash"]

        if check_password_hash(password_hash, password):
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
