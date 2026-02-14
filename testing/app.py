from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"


# Database connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        session["role"] = "admin"
        session["full_name"] = "Admin"
        return redirect("/dashboard")

    flash("Invalid username or password", "error")
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect("/")

    conn = get_db_connection()

    total_users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    total_projects = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
    total_documents = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    total_staff = conn.execute("SELECT COUNT(*) FROM users WHERE role='staff'").fetchone()[0]

    dpr_count = conn.execute("SELECT COUNT(*) FROM documents WHERE category='dpr'").fetchone()[0]
    mom_count = conn.execute("SELECT COUNT(*) FROM documents WHERE category='mom'").fetchone()[0]
    weekly_count = conn.execute("SELECT COUNT(*) FROM documents WHERE category='weekly'").fetchone()[0]
    photos_count = conn.execute("SELECT COUNT(*) FROM documents WHERE category='photos'").fetchone()[0]

    recent_docs = conn.execute(
        "SELECT * FROM documents ORDER BY upload_date DESC LIMIT 5"
    ).fetchall()

    conn.close()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_projects=total_projects,
        total_documents=total_documents,
        total_staff=total_staff,
        dpr_count=dpr_count,
        mom_count=mom_count,
        weekly_count=weekly_count,
        photos_count=photos_count,
        recent_docs=recent_docs
    )


if __name__ == "__main__":
    app.run(debug=True)
