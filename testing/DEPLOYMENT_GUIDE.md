# Production Deployment Checklist

## 🔒 Security Changes (IMPORTANT!)

### 1. Change Secret Key
In `app.py`, line 10:
```python
# BEFORE (Development)
app.secret_key = 'jkw_construction_secret_key_2024'

# AFTER (Production)
import os
app.secret_key = os.environ.get('SECRET_KEY', 'your-random-very-long-secret-key-here')
```

Generate random key:
```python
import secrets
print(secrets.token_hex(32))
```

### 2. Disable Debug Mode
In `app.py`, last line:
```python
# BEFORE
app.run(debug=True, host='0.0.0.0', port=5000)

# AFTER
app.run(debug=False, host='0.0.0.0', port=5000)
```

### 3. Change Default Passwords
```bash
# After deployment, login and change:
- admin password (admin123 → strong password)
- staff1 password (staff123 → strong password)
- client1 password (user123 → strong password)
```

### 4. Use Environment Variables
Create `.env` file:
```env
SECRET_KEY=your-very-long-random-secret-key
DATABASE_PATH=database/jkw_construction.db
UPLOAD_FOLDER=static/uploads
MAX_FILE_SIZE=52428800
```

### 5. Setup HTTPS
Most platforms (Render, PythonAnywhere, Heroku) provide free HTTPS.

For custom server:
```bash
# Install Certbot
apt install certbot python3-certbot-nginx

# Get certificate
certbot --nginx -d yourdomain.com
```

### 6. Database Backup
Setup automatic backups:
```bash
# Add to crontab (daily backup at 2 AM)
0 2 * * * cp /path/to/database/jkw_construction.db /path/to/backups/jkw_$(date +\%Y\%m\%d).db
```

### 7. Use Production Database (Optional)
For heavy usage, switch from SQLite to PostgreSQL:
```bash
# Install PostgreSQL
pip install psycopg2-binary

# Update database connection in app.py
```

### 8. Setup Nginx (For custom server)
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /var/www/jkw_construction/static;
    }
}
```

### 9. Run with Gunicorn (Production server)
```bash
# Install
pip install gunicorn

# Run
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# -w 4 means 4 worker processes
```

### 10. Monitor Disk Space
```bash
# Check uploads folder size
du -sh static/uploads

# Set up alerts when folder > 1GB
```

## 📝 Post-Deployment Tasks

1. Test all features:
   - [ ] Login with all 3 roles
   - [ ] Create project
   - [ ] Upload documents to all categories
   - [ ] Download documents
   - [ ] Edit/Delete documents
   - [ ] Add/Edit users

2. Create backups:
   - [ ] Database backup
   - [ ] Uploads folder backup

3. Document access:
   - [ ] Give URL to team
   - [ ] Share login credentials
   - [ ] Create user manual

4. Monitor:
   - [ ] Check logs daily
   - [ ] Monitor disk space
   - [ ] Check upload folder size

## ⚠️ Common Issues

**Issue**: Port 5000 already in use
```bash
# Find process
lsof -i :5000

# Kill process
kill -9 <PID>

# Or use different port
app.run(debug=False, host='0.0.0.0', port=8000)
```

**Issue**: Database locked
```bash
# Close all connections
# Restart application
```

**Issue**: File upload fails
```bash
# Check folder permissions
chmod 755 static/uploads

# Check disk space
df -h
```

## 🎯 Performance Tips

1. **Limit file uploads**: Already set to 50MB
2. **Clean old files**: Delete unused documents monthly
3. **Optimize images**: Compress before upload
4. **Use CDN**: For faster file downloads (advanced)

## 📞 Support

If deployment issues:
1. Check application logs
2. Verify database exists
3. Check file permissions
4. Ensure all dependencies installed
