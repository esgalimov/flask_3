from flask import Flask
from data import db_session, jobs_api
from data.users import User
from flask import render_template, make_response, request, redirect, abort, jsonify
from data.jobs import Jobs
import datetime
from forms.user import RegisterForm
from forms.login_form import LoginForm
from forms.job import JobForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import Api
from data import users_resource, jobs_resource


app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# для кириллицы в json
app.config['JSON_AS_ASCII'] = False


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


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
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            email=form.email.data,
            address=form.address.data,

        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


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


@app.route('/add_job',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.title.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        user = db_sess.query(User).filter(User.id == form.team_leader.data).first()
        user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Add job', type_of_action='Add job',
                           form=form)


@app.route('/edit_job/<int:id>',  methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = JobForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        if current_user.id == 1:
            jod = db_sess.query(Jobs).filter(Jobs.id == id).first()
        else:
            jod = db_sess.query(Jobs).filter(Jobs.id == id).filter(Jobs.user == current_user).first()
        if jod:
            form.title.data = jod.job
            form.work_size.data = jod.work_size
            form.collaborators.data = jod.collaborators
            form.is_finished.data = jod.is_finished
            form.team_leader.data = jod.team_leader
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if current_user.id == 1:
            jod = db_sess.query(Jobs).filter(Jobs.id == id).first()
        else:
            jod = db_sess.query(Jobs).filter(Jobs.id == id).filter(Jobs.user == current_user).first()
        if jod:
            jod.job = form.title.data
            jod.work_size = form.work_size.data
            jod.collaborators = form.collaborators.data
            jod.is_finished = form.is_finished.data
            jod.team_leader = form.team_leader.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('Job.html',
                           title='Edit job',
                           type_of_action='Edit job',
                           form=form
                           )


@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    if current_user.id == 1:
        jod = db_sess.query(Jobs).filter(Jobs.id == id).first()
    else:
        jod = db_sess.query(Jobs).filter(Jobs.id == id).filter(Jobs.user == current_user).first()
    if jod:
        db_sess.delete(jod)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs_api.blueprint)
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
