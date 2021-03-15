import flask
from flask import jsonify
from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job', 'user.name', 'user.surname', 'work_size',
                                    'collaborators', 'start_date',
                                    'end_date', 'is_finished'))
                 for item in jobs]
        }
    )
