# JKW Construction - Document Management System

A role-based document management system for JKW Construction with Admin, Staff, and User panels.

## Features

### Admin Panel
- Full control over users (add, edit, delete, activate/deactivate)
- View and manage all documents
- Dashboard with statistics
- View recent uploads

### Staff Panel
- Upload construction documents with project details
- Add optional descriptions to documents
- Manage only their uploaded documents (edit, delete)
- View their upload history

### User/Client Panel
- Securely view all available documents
- Download documents
- View project information

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)

## Project Structure

```
jkw_construction/
│
├── app.py                      # Main Flask application
├── init_db.py                  # Database initialization script
├── requirements.txt            # Python dependencies
│
├── database/
│   └── jkw_construction.db    # SQLite database (created after init)
│
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet
│   ├── js/
│   │   └── script.js          # JavaScript functionality
│   └── uploads/               # Uploaded documents folder
│
└── templates/
    ├── base.html              # Base template
    ├── login.html             # Login page
    ├── admin_dashboard.html   # Admin dashboard
    ├── admin_users.html       # User management
    ├── admin_documents.html   # Document management (admin)
    ├── staff_dashboard.html   # Staff dashboard
    ├── staff_documents.html   # Staff document management
    ├── user_dashboard.html    # Client dashboard
    ├── user_documents.html    # Document view (client)
    └── profile.html           # User profile page
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.0 Werkzeug==3.0.1
```

### Step 2: Initialize Database

```bash
python init_db.py
```

This will create:
- SQLite database with users and documents tables
- Default admin, staff, and client accounts
- Necessary folders for file uploads

### Step 3: Run the Application

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

## Default Login Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123

### Staff Account
- **Username**: staff1
- **Password**: staff123

### Client Account
- **Username**: client1
- **Password**: user123

**⚠️ IMPORTANT: Change these default passwords after first login!**

## Usage Guide

### For Admin

1. **Login** with admin credentials
2. **Manage Users**:
   - Click "Users" in navigation
   - Add new users (staff or clients)
   - Edit user details, change passwords
   - Activate/deactivate user accounts
   - Delete users if needed

3. **Manage Documents**:
   - View all uploaded documents
   - Download any document
   - Delete documents if needed

### For Staff

1. **Login** with staff credentials
2. **Upload Documents**:
   - Click "My Documents"
   - Click "Upload Document" button
   - Fill in document title, project name
   - Add optional description
   - Select file (PDF, DOC, DOCX, JPG, PNG, DWG, XLS, XLSX)
   - Click Upload

3. **Manage Your Documents**:
   - Edit document information
   - Delete your documents
   - Download documents

### For Clients/Users

1. **Login** with client credentials
2. **View Documents**:
   - Browse all available documents
   - View project details and descriptions
   - See who uploaded each document
3. **Download Documents**:
   - Click download button on any document

## Security Features

- Password hashing using Werkzeug
- Role-based access control
- Session management
- File type validation
- Secure file upload handling
- SQL injection prevention
- XSS protection

## Allowed File Types

- Documents: PDF, DOC, DOCX
- Images: JPG, JPEG, PNG
- Drawings: DWG
- Spreadsheets: XLS, XLSX

**Maximum file size**: 50MB

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- full_name
- email
- password (Hashed)
- role (admin/staff/user)
- status (active/inactive)
- created_at (Timestamp)

### Documents Table
- id (Primary Key)
- document_title
- project_name
- description
- file_name
- file_path
- uploaded_by (Foreign Key to users)
- upload_date (Timestamp)

## Customization

### Change App Secret Key
Edit `app.py`:
```python
app.secret_key = 'your-secret-key-here'
```

### Change File Upload Limits
Edit `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB
```

### Add More File Types
Edit `app.py`:
```python
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'dwg', 'xlsx', 'xls', 'your_extension'}
```

### Change Database
Replace SQLite with PostgreSQL or MySQL by modifying the database connection in `app.py`.

## Troubleshooting

### Port Already in Use
Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database Not Found
Run the initialization script:
```bash
python init_db.py
```

### Upload Folder Not Found
Create the folder manually:
```bash
mkdir -p static/uploads
```

## Production Deployment

For production deployment:

1. **Disable Debug Mode**:
```python
app.run(debug=False)
```

2. **Use Production WSGI Server**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. **Use Environment Variables** for sensitive data:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY')
```

4. **Use Production Database** (PostgreSQL/MySQL)

5. **Set up HTTPS** with SSL certificates

6. **Configure Firewall** and security settings

## Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Ensure all dependencies are installed

## License

This project is created for JKW Construction internal use.

## Version

Version 1.0.0 - February 2026
