from flask import Flask
from data import db_session
from data.users import User
from flask import render_template
from data.jobs import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def job_list():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    print(jobs[0].team_leader)
    return render_template('index.html', jobs=jobs, title='Журнал работ')


def main():
    db_session.global_init("db/blogs.db")

    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()