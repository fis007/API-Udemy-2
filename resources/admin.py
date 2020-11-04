import sqlite3
from flask_restful import Resource, reqparse
from models.admin import AdminModel

class AdminRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = AdminRegister.parser.parse_args()

        if AdminModel.find_by_adminname(data['adminname']):
            return {"message": "An admin with that adminname already exists"}, 400

        admin = AdminModel(**data)
        admin.save_to_db()

        return {"message": "Admin created successfully."}, 201
