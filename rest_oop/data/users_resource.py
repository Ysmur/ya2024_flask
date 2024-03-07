from flask import jsonify

from data import db_session
from data.users import User
from flask_restful import reqparse, abort, Api, Resource


def abort_if_user_not_found(user_id):
    if type(user_id) != int:
        abort(400, message=f"Without letters!")
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"Users {user_id} not found")



class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position',
                  'speciality', 'address', 'email')) for item in users]})


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('surname', 'name', 'age', 'position',
                  'speciality', 'address', 'email'))})