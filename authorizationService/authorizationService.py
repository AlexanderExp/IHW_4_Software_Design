from datetime import datetime
from uuid import uuid4

from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO

from dbModels import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'URI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret_key"

app.config['SESSION_COOKIE_DOMAIN'] = 'localhost'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
socketio = SocketIO(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        role = request.form['role']

        if confirm_password != password:
            error_message = "Пароли не совпадают"
            return render_template('registerPage.html', error_message=error_message)
        if User.query.filter_by(email=email).first():
            error_message = "Пользователь с таким email уже существует"
            return render_template('registerPage.html', error_message=error_message)

        new_user = User(username=username, email=email, password_hash=password,
                        role=role, created_at=datetime.now(),
                        updated_at=datetime.now())
        db.session.add(new_user)
        db.session.commit()
        flash("Регистрация успешна", 'success')

        return render_template('successPage.html')

    return render_template('registerPage.html')


@app.route('/get_info_about_user')
def get_info_about_user():
    return current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and user.password_hash == password:
            session['user_id'] = user.id
            login_user(user)
            return redirect('http://localhost:5800?user_id=' + str(user.id))
        else:
            error_message = 'Пользователя с таким email и паролем не существует'
            return render_template('loginPage.html', error_message=error_message)
    return render_template('loginPage.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def home():
    return redirect(url_for('login'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def generate_unique_chat_id():
    return str(uuid4())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(port=5700)
