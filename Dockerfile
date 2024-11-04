# Dockerfile
FROM python:3.10.15-alpine

# הגדרת תיקיית העבודה
WORKDIR /app

# העתקת requirements.txt
COPY requirements.txt .

# התקנת התלותות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת כל הקבצים
COPY . .

# הפעלת האפליקציה
CMD ["python", "app.py"]
