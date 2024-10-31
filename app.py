from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# לדמות בסיס נתונים (במציאות תשתמש ב-BD כמו SQLite)
users = {}
tasks = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('calendar'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username not in users:
            users[username] = []
        session['username'] = username
        return redirect(url_for('calendar'))
    return render_template('login.html')

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    
    if request.method == 'POST':
        task = request.form['task']
        date = request.form['date']
        tasks.setdefault(username, []).append((task, date))
    
    user_tasks = tasks.get(username, [])
    return render_template('calendar.html', tasks=user_tasks)

@app.route('/delete', methods=['POST'])
def delete_task():
    username = session['username']
    task_to_delete = request.json['task']
    tasks[username] = [task for task in tasks[username] if task[0] != task_to_delete]
    return jsonify(success=True)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
