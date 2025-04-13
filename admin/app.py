from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'supersecretkey')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Для простоты: один пользователь (позже можно расширить через базу данных)
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Пользователь "admin" по умолчанию
USERS = {"admin": {"password": os.getenv('ADMIN_PASSWORD', 'adminpass')}}

@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = USERS.get(username)
        if user and user['password'] == password:
            login_user(User(username))
            return redirect(url_for('dashboard'))
        flash('Неверный логин или пароль', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        # Здесь мы будем сохранять новые ключи API в .env или базу
        flash('Настройки сохранены!', 'success')
    return render_template('settings.html')

@app.route('/posts')
@login_required
def posts():
    # Здесь позже будет вывод списка постов
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
