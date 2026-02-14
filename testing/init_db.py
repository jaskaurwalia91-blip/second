import sqlite3
from werkzeug.security import generate_password_hash

def init_database():
    # Connect to database
    conn = sqlite3.connect('database/jkw_construction.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'staff', 'user')),
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create projects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT UNIQUE NOT NULL,
            project_code TEXT,
            location TEXT,
            client_name TEXT,
            start_date TEXT,
            description TEXT,
            status TEXT DEFAULT 'active' CHECK(status IN ('active', 'completed', 'on-hold')),
            created_by INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (created_by) REFERENCES users (id)
        )
    ''')
    
    # Create documents table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            category TEXT NOT NULL CHECK(category IN ('DPR', 'MOM', 'WEEKLY_REPORT', 'SITE_PHOTOS')),
            document_title TEXT NOT NULL,
            description TEXT,
            file_name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            uploaded_by INTEGER NOT NULL,
            upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id),
            FOREIGN KEY (uploaded_by) REFERENCES users (id)
        )
    ''')
    
    # Check if admin already exists
    cursor.execute("SELECT * FROM users WHERE role = 'admin'")
    admin_exists = cursor.fetchone()
    
    if not admin_exists:
        # Create default admin user
        admin_password = generate_password_hash('admin123')
        cursor.execute('''
            INSERT INTO users (username, full_name, email, password, role, status) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('admin', 'Administrator', 'admin@jkwconstruction.com', admin_password, 'admin', 'active'))
        
        # Create sample staff user
        staff_password = generate_password_hash('staff123')
        cursor.execute('''
            INSERT INTO users (username, full_name, email, password, role, status) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('staff1', 'John Smith', 'john@jkwconstruction.com', staff_password, 'staff', 'active'))
        
        # Create sample client user
        user_password = generate_password_hash('user123')
        cursor.execute('''
            INSERT INTO users (username, full_name, email, password, role, status) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('client1', 'Sarah Johnson', 'sarah@example.com', user_password, 'user', 'active'))
        
        # Get admin ID for creating sample projects
        cursor.execute("SELECT id FROM users WHERE username = 'admin'")
        admin_id = cursor.fetchone()[0]
        
        # Create sample projects
        cursor.execute('''
            INSERT INTO projects (project_name, project_code, location, client_name, start_date, description, status, created_by) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('Residential Complex A', 'RC-2024-001', 'Sector 15, Ludhiana', 'ABC Developers', '2024-01-15', 'Multi-story residential building project', 'active', admin_id))
        
        cursor.execute('''
            INSERT INTO projects (project_name, project_code, location, client_name, start_date, description, status, created_by) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('Commercial Plaza B', 'CP-2024-002', 'Mall Road, Ludhiana', 'XYZ Corporation', '2024-02-01', 'Commercial shopping complex', 'active', admin_id))
        
        print("✓ Default users created:")
        print("  Admin - Username: admin, Password: admin123")
        print("  Staff - Username: staff1, Password: staff123")
        print("  Client - Username: client1, Password: user123")
        print("✓ Sample projects created:")
        print("  Project 1: Residential Complex A")
        print("  Project 2: Commercial Plaza B")
    else:
        print("✓ Database already initialized")
    
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully!")

if __name__ == '__main__':
    import os
    if not os.path.exists('database'):
        os.makedirs('database')
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
    
    init_database()
