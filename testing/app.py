from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Home page
@app.route("/")
def home():
    return render_template("login.html")

# Login
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Default credentials
    if username == "admin" and password == "admin123":
        session["role"] = "admin"
        return redirect("/dashboard")

    elif username == "staff1" and password == "staff123":
        session["role"] = "staff"
        return redirect("/dashboard")

    elif username == "client1" and password == "user123":
        session["role"] = "user"
        return redirect("/dashboard")

    else:
        flash("Invalid username or password", "error")
        return redirect("/")

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect("/")

    if session["role"] == "admin":
        return render_template("admin_dashboard.html")

    elif session["role"] == "staff":
        return render_template("staff_dashboard.html")

    elif session["role"] == "user":
        return render_template("user_dashboard.html")

    return redirect("/")

# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
