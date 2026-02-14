# JKW Construction Document Management System - Quick Start Guide

## 🚀 Quick Installation (3 Steps)

### Step 1: Install Python Dependencies
```bash
cd jkw_construction
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python init_db.py
```

You'll see:
```
✓ Default users created:
  Admin - Username: admin, Password: admin123
  Staff - Username: staff1, Password: staff123
  Client - Username: client1, Password: user123
✓ Database initialized successfully!
```

### Step 3: Run the Application
```bash
python app.py
```

Open your browser and go to: **http://localhost:5000**

---

## 📁 File Structure Overview

```
jkw_construction/
│
├── 📄 app.py                    # Main application (Backend)
├── 📄 init_db.py                # Database setup script
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Complete documentation
│
├── 📂 database/                 # Database files (auto-created)
│
├── 📂 static/
│   ├── 📂 css/
│   │   └── style.css           # All styling
│   ├── 📂 js/
│   │   └── script.js           # All JavaScript
│   └── 📂 uploads/             # Uploaded files (auto-created)
│
└── 📂 templates/                # All HTML pages
    ├── base.html               # Base layout
    ├── login.html              # Login page
    ├── admin_dashboard.html    # Admin home
    ├── admin_users.html        # User management
    ├── admin_documents.html    # Document management (admin)
    ├── staff_dashboard.html    # Staff home
    ├── staff_documents.html    # Upload & manage documents
    ├── user_dashboard.html     # Client home
    ├── user_documents.html     # View & download documents
    └── profile.html            # User profile
```

---

## 🎯 Default Login Credentials

| Role   | Username | Password  |
|--------|----------|-----------|
| Admin  | admin    | admin123  |
| Staff  | staff1   | staff123  |
| Client | client1  | user123   |

**⚠️ Change passwords after first login!**

---

## ✨ Features by Role

### 👑 Admin Can:
- ✅ Add, edit, delete users
- ✅ View all documents
- ✅ Download any document
- ✅ Delete any document
- ✅ View statistics dashboard

### 👷 Staff Can:
- ✅ Upload construction documents
- ✅ Add project details & descriptions
- ✅ Edit their own documents
- ✅ Delete their own documents
- ✅ Download documents

### 👤 Client/User Can:
- ✅ View all documents
- ✅ Download documents
- ✅ See project information
- ✅ View who uploaded each document

---

## 📝 How to Use

### Admin: Add a New User
1. Login as admin
2. Click "Users" in navigation
3. Click "Add User" button
4. Fill in details (username, name, email, password, role)
5. Click "Add User"

### Staff: Upload a Document
1. Login as staff
2. Click "My Documents"
3. Click "Upload Document"
4. Fill in:
   - Document Title
   - Project Name
   - Description (optional)
   - Select File
5. Click "Upload"

### Client: Download a Document
1. Login as client
2. Click "Documents"
3. Find the document you need
4. Click download button

---

## 🔒 Security Features

✅ Password hashing (Werkzeug)
✅ Role-based access control
✅ Session management
✅ File type validation
✅ SQL injection prevention
✅ XSS protection

---

## 📦 Allowed File Types

- **Documents**: PDF, DOC, DOCX
- **Images**: JPG, JPEG, PNG
- **Drawings**: DWG
- **Spreadsheets**: XLS, XLSX

**Max file size**: 50MB

---

## 🛠️ Troubleshooting

### "Port already in use"
Edit `app.py`, line 280:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port
```

### "Database not found"
Run:
```bash
python init_db.py
```

### "Module not found"
Install dependencies:
```bash
pip install Flask Werkzeug
```

---

## 🔧 Customization

### Change Maximum File Size
Edit `app.py`, line 11:
```python
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB
```

### Add New File Types
Edit `app.py`, line 12:
```python
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'dwg', 'xlsx', 'xls', 'zip'}
```

### Change App Colors
Edit `static/css/style.css`:
- Line 42: Login page gradient
- Line 111: Navigation bar gradient
- Line 293: Primary button color

---

## 🌐 Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Database**: SQLite
- **Security**: Werkzeug password hashing

---

## 📊 Database Tables

### users
- id, username, full_name, email, password, role, status, created_at

### documents
- id, document_title, project_name, description, file_name, file_path, uploaded_by, upload_date

---

## 🚀 Production Deployment

1. **Disable debug mode** in `app.py`
2. **Use Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. **Use PostgreSQL/MySQL** instead of SQLite
4. **Set up HTTPS** with SSL
5. **Use environment variables** for secrets

---

## 💡 Tips

- Always backup the database before major changes
- Change default passwords immediately
- Keep uploads folder organized by project
- Regular database backups recommended
- Monitor upload folder size

---

## 📞 Need Help?

1. Check README.md for detailed documentation
2. Review code comments in app.py
3. Ensure all dependencies are installed
4. Check database is initialized

---

**Version**: 1.0.0
**Created for**: JKW Construction
**Date**: February 2026
