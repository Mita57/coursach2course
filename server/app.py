from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from passlib.hash import sha256_crypt
from models.BasicModel import SQLModel
import datetime

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    """
    Gets the data from the login form and authorizes the input

    Returns: JSON with auth result info
    """
    data = request.get_json()
    email = data.get('login')
    password = data.get('pwrd')
    user = SQLModel.get_by_attrs(('nickname', 'password'), 'login', login)
    print(user)
    try:
        user_pw = user[0][1]
        user_nick = user[0][0]
        if password == user_pw:
            return jsonify(result=user_nick)
        else:
            return jsonify(result='fail')
    except:
        return jsonify(result='fail')


@app.route('/register', methods=['POST'])
def register():
    """
    Inserts the information about new user unto the database

    Returns:
        Inserts the information about new user unto the database
    """
    post_data = request.get_json()
    print(post_data)
    today = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    email = post_data.get('email')
    password = post_data.get('password')
    nickname = post_data.get('nickname')
    try:
        User.insert((email, nickname, password, 'null', today, 0, 'sas', False, True, 'gaming', False))
        return jsonify(result='good')
    except:
        return jsonify(result='bad')


@app.route('/channel')
def get_channel():
    """
    gets the channel info from the database and returns info about it
    Returns:
        JSON with channel info
    """
    nick = request.args.get('nickname')
    print(nick)
    stuff = User.get_by_attrs(cols=('nickname', 'subs', 'description', 'curr_hub'), attr_cols='nickname', attr_values=nick)
    print(stuff)
    return jsonify(stuff)



if __name__ == '__main__':
    app.run(debug=True)
