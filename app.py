from flask import Flask, render_template, request, redirect, url_for, session
from src.database.execute import DBClient
from src.database.queries import insert_user, select_user_by_email, insert_task, select_tasks_by_user

app = Flask(__name__)
app.secret_key = "supersecretkey"
db = DBClient()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        db.execute_commit(insert_user(username, password, email))
        return redirect(url_for('login.html'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = db.execute_one(select_user_by_email(email))
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('index.html'))
        return redirect(url_for('login.html'))
    return render_template('login.html')

@app.route('/index')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login.html'))
    user_id = session['user_id']
    tasks = db.execute_all(select_tasks_by_user(user_id))
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    if 'user_id' not in session:
        return redirect(url_for('login.html'))
    user_id = session['user_id']
    task_name = request.form.get('task_name')
    db.execute_commit(insert_task(user_id, task_name))
    return redirect(url_for('index.html'))




if __name__ == '__main__':
    app.run(debug=True)
