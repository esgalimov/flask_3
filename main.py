from flask import Flask
from data import db_session
from data.users import User
from flask import render_template, make_response, request, redirect
from data.jobs import Jobs
import datetime
from forms.user import RegisterForm
from forms.login_form import LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def job_list():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template('index.html', jobs=jobs, title='Журнал работ')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.name.data,
            position=form.name.data,
            speciality=form.name.data,
            email=form.email.data,
            address=form.email.data,

        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/log')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/log')
def log():
    return 'success'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
