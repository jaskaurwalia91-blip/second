from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# ==============================
# BASIC CONFIG
# ==============================

app.secret_key = os.environ.get('SECRET_KEY', 'jkw_construction_secret_key_2024')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static/uploads')
app.config['DATABASE'] = os.path.join(BASE_DIR, 'database/jkw_construction.db')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'dwg', 'xlsx', 'xls'}

# Ensure folders exist (VERY IMPORTANT for Render)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'database'), exist_ok=True)

# ==============================
# DATABASE CONNECTION
# ==============================

def get_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# ==============================
# HELPERS
# ==============================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                flash('You do not have permission to access this page', 'error')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# ==============================
# HOME ROUTE (FIXES 404)
# ==============================

@app.route("/")
def home():
    return redirect(url_for("login"))  # Redirect to login page

# ==============================
# EXAMPLE LOGIN ROUTE (SAFE FALLBACK)
# Agar already hai to ye remove kar sakti ho
# ==============================

@app.route("/login")
def login():
    return "Login Page Working ✅"

# ==============================
# RUN APP (Render Compatible)
# ==============================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
