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
    user = SQLModel.get_by_attrs(('login', 'pwrdHash', 'type', 'name'), 'users', 'login', login)
    try:
        user_login = user[0][0]
        user_pw = user[0][1]
        user_type = user[0][2]
        user_name = user[0][3]
        if sha256_crypt.verify(password, user_pw):
            return jsonify(result=user_login, type=user_type, name=user_name)
        else:
            return jsonify(result='fail')
    except:
        return jsonify(result='fail')


@app.route('/getInventory')
def get_inventory():
    stuff = SQLModel.get_by_attrs(cols=('name', 'amount', 'id'), attr_cols='1', attr_values='1', table='inventory')
    return jsonify(stuff)


@app.route('/addInventory')
def add_inventory():
    name = request.args.get('name')
    amount = request.args.get('amount')
    img = request.args.get('img')
    stuff = SQLModel.insert('inventory', ('name', 'amount'), (name, amount))
    return jsonify(stuff)


@app.route('/editInventory')
def edit_inventory():
    inv_id = request.args.get('id')
    name = request.args.get('name')
    amount = request.args.get('amount')
    img = request.args.get('img')
    SQLModel.update_by_attrs('inventory', ('name', 'amount'), (name, amount), 'id', inv_id)
    return 'Ok'


@app.route('/removeInventory')
def remove_inventory():
    inv_id = request.args.get('id')
    SQLModel.delete_by_attrs('inventory', 'id', inv_id)
    return 'Ok'


@app.route('/getEquipment')
def get_equipment():
    stuff = SQLModel.get_by_attrs(cols=('id', 'name', 'sheets_amount', 'type'), attr_cols='1', attr_values='1',
                                  table='equipment')
    return jsonify(stuff)


@app.route('/addEquipment')
def add_equipment():
    name = request.args.get('name')
    amount = request.args.get('sheetsAmount')
    type = request.args.get('type')
    stuff = SQLModel.insert('equipment', ('name', 'sheets_amount', 'type'), (name, amount, type))
    return jsonify(stuff)


@app.route('/removeEquipment')
def remove_equipment():
    eq_id = request.args.get('id')
    SQLModel.delete_by_attrs('equipment', 'id', eq_id)
    return ('Ok')


@app.route('/editEquipment')
def edit_equipment():
    eq_id = request.args.get('id')
    name = request.args.get('name')
    type = request.args.get('type')
    amount = request.args.get('amount')
    img = request.args.get('img')
    SQLModel.update_by_attrs('inventory', ('name', 'sheets_amount', 'type'), (name, amount, type), 'id', eq_id)
    return 'Ok'


@app.route('/getEmployees')
def get_employees():
    stuff = SQLModel.get_by_attrs(cols=('*'), attr_cols='1', attr_values='1', table='employees')
    return jsonify(stuff)


@app.route('/getProgs')
def get_progs():
    oven_id = request.args.get('id')
    stuff = SQLModel.get_by_attrs(cols=('*'), attr_cols='oven_id', attr_values=oven_id, table='baking_progs')
    return jsonify(stuff)


@app.route('/addProg')
def add_prog():
    name = request.args.get('name')
    oven_id = request.args.get('ovenId')
    temp = request.args.get('temp')
    time = request.args.get('time')
    steam = request.args.get('steam')
    dryness = request.args.get('dryness')
    fan = request.args.get('fan')
    SQLModel.insert('baking_progs', ('name', 'temp', 'time', 'steam', 'dry', 'fan_speed', 'oven_id'),
                    (name, temp, time, steam, dryness, fan, oven_id))
    return 'ok'


@app.route('/editProg')
def edit_prog():
    name = request.args.get('name')
    id = request.args.get('id')
    temp = request.args.get('temp')
    time = request.args.get('time')
    steam = request.args.get('steam')
    dryness = request.args.get('dryness')
    fan = request.args.get('fan')
    SQLModel.update_by_attrs('baking_progs', ('name', 'temp', 'time', 'steam', 'dry', 'fan_speed'),
                    (name, temp, time, steam, dryness, fan), 'id', id)

@app.route('/removeProg')
def delete_prog():
    bp_id = request.args.get('id')
    SQLModel.delete_by_attrs('baking_progs', 'id', bp_id)
    return 'ok'
