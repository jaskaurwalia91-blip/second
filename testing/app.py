from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'jkw_construction_secret_key_2024')  # Use env var for security
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'dwg', 'xlsx', 'xls'}

# Database connection
def get_db():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'database/jkw_construction.db'))
    conn.row_factory = sqlite3.Row
    return conn

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Role required decorator
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

# -------------------
# Your existing routes remain unchanged
# Just ensure all file paths use app.config['UPLOAD_FOLDER'] or database path from get_db()
# -------------------

# Example for file upload in staff_upload:
# filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

# -------------------
# RUN APP
# -------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT env
    app.run(debug=False, host='0.0.0.0', port=port)
