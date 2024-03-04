import flask
from flask import jsonify

from . import db_session
from .users import User
from .jobs import Job

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'team_leader'))
                 for item in jobs]
        }
    )