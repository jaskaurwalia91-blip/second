# JKW Construction - Document Management System v2.0

## ✨ NEW FEATURES - Version 2.0

### 🎯 What's New:

#### 1. **Project Management System**
- Admin can create and manage multiple projects
- Each project has:
  - Project Name
  - Project Code
  - Location
  - Client Name
  - Start Date
  - Description
  - Status (Active/Completed/On-Hold)

#### 2. **Document Categories**
Documents are now organized into 4 specific categories:
- **DPR** (Daily Progress Reports)
- **MOM** (Minutes of Meeting)
- **WEEKLY_REPORT** (Weekly Progress Reports)
- **SITE_PHOTOS** (Site Photographs)

#### 3. **Project-Wise Document Organization**
- Each project has separate sections for all 4 categories
- Staff can upload documents to specific categories within each project
- Users can view documents organized by project and category

#### 4. **Enhanced User Interface**
- Beautiful category cards with unique colors:
  - DPR: Purple gradient
  - MOM: Green gradient
  - Weekly Reports: Blue gradient
  - Site Photos: Pink/Yellow gradient
- Project selection grid for easy navigation
- Category-wise statistics on dashboards

---

## 📋 Complete Features List

### 👑 Admin Features:
- ✅ Create, edit, and delete projects
- ✅ View all projects with document counts
- ✅ Manage users (add, edit, delete, activate/deactivate)
- ✅ View all documents across all projects
- ✅ View project-specific documents by category
- ✅ Download and delete any document
- ✅ Dashboard with:
  - Total users, projects, documents count
  - Category-wise document statistics
  - Recent document uploads

### 👷 Staff Features:
- ✅ View all active projects
- ✅ Upload documents to specific categories for each project:
  - Daily Progress Reports (DPR)
  - Minutes of Meeting (MOM)
  - Weekly Progress Reports
  - Site Photos
- ✅ Add optional descriptions to documents
- ✅ Edit document title and description
- ✅ Delete only their own uploaded documents
- ✅ Dashboard showing:
  - Total documents uploaded
  - Category-wise upload counts
  - Active projects count
  - Recent uploads

### 👤 Client/User Features:
- ✅ View all active projects
- ✅ Browse documents by project
- ✅ View documents organized by categories:
  - DPR
  - MOM
  - Weekly Reports
  - Site Photos
- ✅ Download any document
- ✅ See who uploaded each document
- ✅ Dashboard with recent documents

---

## 🚀 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
python init_db.py
```

This creates:
- ✅ Users table (Admin, Staff, Clients)
- ✅ Projects table
- ✅ Documents table with categories
- ✅ 2 sample projects (Residential Complex A, Commercial Plaza B)
- ✅ Default user accounts

### Step 3: Run Application
```bash
python app.py
```

Open browser: **http://localhost:5000**

---

## 🔐 Default Login Credentials

| Role   | Username | Password  | Access                          |
|--------|----------|-----------|----------------------------------|
| Admin  | admin    | admin123  | Full system control             |
| Staff  | staff1   | staff123  | Upload & manage own documents   |
| Client | client1  | user123   | View & download documents       |

**⚠️ Change these passwords after first login!**

---

## 📂 How to Use - Complete Workflow

### Admin Workflow:

#### 1. Add New Project
```
Login → Projects → Add New Project
Fill in:
- Project Name: "Shopping Mall Construction"
- Project Code: "SMC-2024-003"
- Location: "Downtown, Ludhiana"
- Client Name: "ABC Developers"
- Start Date: Select date
- Description: Project details
```

#### 2. Manage Users
```
Login → Users → Add User
Create staff and client accounts for the new project
```

#### 3. View Project Documents
```
Login → Projects → Select Project → View Documents
See all documents organized by:
- DPR
- MOM
- Weekly Reports
- Site Photos
```

### Staff Workflow:

#### 1. Select Project
```
Login → My Documents → Select Project Card
```

#### 2. Upload DPR (Daily Progress Report)
```
Click "Upload DPR" button
Fill in:
- Document Title: "DPR - 15 Feb 2026"
- Description: "Foundation work completed"
- Select File: Upload PDF/DOC
```

#### 3. Upload MOM (Minutes of Meeting)
```
Click "Upload MOM" button
Fill in:
- Document Title: "Client Meeting - Week 3"
- Description: "Budget discussion and timeline"
- Select File: Upload document
```

#### 4. Upload Weekly Report
```
Click "Upload Weekly Report" button
Fill in:
- Document Title: "Week 3 Progress"
- Description: "Weekly summary"
- Select File: Upload report
```

#### 5. Upload Site Photos
```
Click "Upload Photos" button
Fill in:
- Document Title: "Site Progress - 15 Feb"
- Description: "Foundation laying photos"
- Select File: Upload images (JPG/PNG)
```

### Client Workflow:

#### 1. Browse Projects
```
Login → Documents → Select Project
```

#### 2. View Category Documents
```
Scroll through:
- Daily Progress Reports
- Minutes of Meeting
- Weekly Reports
- Site Photos
```

#### 3. Download Documents
```
Click "Download" button on any document
```

---

## 🎨 Category Color Codes

| Category       | Color       | Icon                  |
|----------------|-------------|-----------------------|
| DPR            | Purple      | 📄 File               |
| MOM            | Green       | 📋 Clipboard          |
Weekly Reports  | Blue        | 📅 Calendar           |
| Site Photos    | Pink/Yellow | 📷 Camera             |

---

## 📊 Database Structure

### Projects Table
```
- id (Primary Key)
- project_name (Unique)
- project_code
- location
- client_name
- start_date
- description
- status (active/completed/on-hold)
- created_by (Foreign Key → users.id)
- created_at
```

### Documents Table
```
- id (Primary Key)
- project_id (Foreign Key → projects.id)
- category (DPR/MOM/WEEKLY_REPORT/SITE_PHOTOS)
- document_title
- description
- file_name
- file_path
- uploaded_by (Foreign Key → users.id)
- upload_date
```

### Users Table
```
- id (Primary Key)
- username (Unique)
- full_name
- email
- password (Hashed)
- role (admin/staff/user)
- status (active/inactive)
- created_at
```

---

## 🔧 Customization

### Add More Categories
Edit `app.py` and `init_db.py`:
```python
# In init_db.py
CHECK(category IN ('DPR', 'MOM', 'WEEKLY_REPORT', 'SITE_PHOTOS', 'YOUR_NEW_CATEGORY'))
```

### Change Category Colors
Edit `static/css/style.css`:
```css
.category-yourcategory {
    border-color: #yourcolor;
}
```

---

## 📱 Responsive Design
- ✅ Mobile-friendly interface
- ✅ Tablet optimized
- ✅ Desktop enhanced

---

## 🔒 Security Features
- ✅ Password hashing (Werkzeug)
- ✅ Role-based access control
- ✅ Session management
- ✅ File type validation
- ✅ SQL injection prevention
- ✅ XSS protection
- ✅ Secure file upload handling

---

## 📝 File Types Allowed
- **Documents**: PDF, DOC, DOCX
- **Images**: JPG, JPEG, PNG
- **Drawings**: DWG
- **Spreadsheets**: XLS, XLSX

**Max file size**: 50MB per file

---

## 🆕 What's Changed from v1.0

| Feature                | v1.0           | v2.0                    |
|------------------------|----------------|-------------------------|
| Projects               | ❌ No          | ✅ Yes (Full Management)|
| Document Categories    | ❌ No          | ✅ 4 Categories         |
| Organization           | Flat list      | Project + Category      |
| Staff Upload           | Any doc        | Category-specific       |
| UI                     | Basic          | Category cards          |
| Dashboard Stats        | Basic          | Category-wise           |

---

## 💡 Tips for Best Use

1. **Organize from Day 1**: Create projects before uploading documents
2. **Use Clear Naming**: "DPR - 15 Feb 2026" better than "report1.pdf"
3. **Add Descriptions**: Helps team find documents quickly
4. **Regular Backups**: Backup database folder regularly
5. **Monitor Storage**: Check uploads folder size periodically

---

## 🐛 Troubleshooting

### "Database locked"
```bash
# Close all connections and restart
python init_db.py
python app.py
```

### "Category not found"
```bash
# Re-initialize database
rm database/jkw_construction.db
python init_db.py
```

### "Project not showing"
```bash
# Check project status in admin panel
Login as admin → Projects → Check status is "active"
```

---

## 📞 Support

For questions or issues:
1. Check this documentation
2. Review code comments in app.py
3. Verify database initialization
4. Ensure all dependencies installed

---

**Version**: 2.0.0  
**Release Date**: February 2026  
**Created for**: JKW Construction  

---

## 🎉 Quick Start Checklist

- [ ] Install Python dependencies
- [ ] Run `python init_db.py`
- [ ] Run `python app.py`
- [ ] Login as admin (admin/admin123)
- [ ] Add a new project
- [ ] Add staff user for the project
- [ ] Login as staff
- [ ] Upload documents to categories
- [ ] Login as client
- [ ] View and download documents

**All set! Happy document management! 🚀**
