import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    """
    above class is used to find user
    we need another API endpoint for managing User resource
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field is required!"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field is required!"
    )

    def post(self):
        # parse the data
        new_user_data = UserRegister.parser.parse_args()

        # check if user exists
        if UserModel.find_by_username(new_user_data['username']):
            return {"message" : "Already Existing User."}, 400

        new_user = UserModel(**new_user_data)
        new_user.save_to_db()


        return {"message" : "User created successfully."}, 201
