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
    email = data.get('email')
    password = data.get('pwrd')
    user = SQLModel.get_by_attrs(('email', 'pwrd'), 'users', 'email', email)
    try:
        user_pw = user[0][1]
        user_nick = user[0][0]
        if password == user_pw:
            stuff = SQLModel.get_by_attrs(('login', 'pwrdHash', 'type', 'name'), 'users', 'login', login)
            return jsonify(stuff)
        else:
            return 'fail'
    except:
        return 'fail'


@app.route('/loginForFuture', methods=['POST'])
def logindsqw():
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
    return 'ok'


@app.route('/removeProg')
def delete_prog():
    bp_id = request.args.get('id')
    SQLModel.delete_by_attrs('baking_progs', 'id', bp_id)
    return 'ok'


@app.route('/getEmployees')
def get_employees():
    stuff = SQLModel.get_by_attrs(cols=('email', 'type', 'name', 'id'), attr_cols='1', attr_values='1', table='users')
    return jsonify(stuff)


@app.route('/addEmployee')
def add_employee():
    name = request.args.get('name')
    email = request.args.get('email')
    type = request.args.get('type')
    pwrd = request.args.get('pwrd')
    SQLModel.insert('users', ('name', 'email', 'type', 'pwrd'),
                    (name, email, type, pwrd))
    return 'ok'


@app.route('/editEmployee')
def edit_employee():
    name = request.args.get('name')
    email = request.args.get('email')
    type = request.args.get('type')
    pwrd = request.args.get('pwrd')
    emp_id = request.args.get('id')
    SQLModel.update_by_attrs('users', ('name', 'email', 'type', 'pwrd'),
                             (name, email, type, pwrd), 'id', emp_id)
    return 'ok'


@app.route('/removeEmployee')
def delete_employee():
    bp_id = request.args.get('id')
    SQLModel.delete_by_attrs('users', 'id', bp_id)
    return 'ok'


@app.route('/addSemiFinished')
def add_dough():
    name = request.args.get('name')
    type = request.args.get('type')
    is_dough = request.args.get('isDough')
    SQLModel.insert('semi_finished', ('name', 'type', 'is_dough'),
                    (name, type, is_dough))
    return 'ok'


@app.route('/editSemiFinished')
def edit_dough():
    name = request.args.get('name')
    type = request.args.get('type')
    is_dough = request.args.get('isDough')
    if type == 'NONE':
        type = None
    SQLModel.update_by_attrs('semi_finished', ('name', 'type'),
                             (name, email, type, pwrd), 'id', emp_id)
    return 'ok'


@app.route('/getSemiFinished')
def get_doughs():
    stuff = SQLModel.get_by_attrs(cols=('type', 'name', 'is_dough', 'id'), attr_cols='1', attr_values='1', table='semi_finished')
    return jsonify(stuff)


@app.route('/removeSemiFinished')
def delete_dough():
    d_id = request.args.get('id')
    SQLModel.delete_by_attrs('semi_finished', 'id', d_id)
    return 'ok'



@app.route('/getRecipes')
def get_recipes():
    stuff = SQLModel.get_by_attrs(cols=('name', 'dough', 'amount', 'weight', 'description', 'id', 'oven_type'),
                                  attr_cols='1', attr_values='1', table='recipes')
    return jsonify(stuff)


@app.route('/editRecipe')
def edit_recipe():
    name = request.args.get('name')
    dough = request.args.get('dough')
    amount = request.args.get('amount')
    weight = request.args.get('weight')
    description = request.args.get('description')
    rec_id = request.args.get('id')
    oven_type = request.args.get('ovenType')
    SQLModel.update_by_attrs('recipes', ('name', 'dough', 'amount', 'weight', 'description', 'oven_type'),
                             (name, dough, amount, weight, description, oven_type), 'id', rec_id)
    return 'ok'


@app.route('/addRecipe')
def add_recipe():
    name = request.args.get('name')
    dough = request.args.get('dough')
    amount = request.args.get('amount')
    weight = request.args.get('weight')
    oven_type = request.args.get('ovenType')
    description = request.args.get('description')
    SQLModel.insert('recipes', ('name', 'dough', 'amount', 'weight', 'description', 'oven_type'),
                    (name, dough, amount, weight, description, oven_type))
    return 'ok'


@app.route('/removeRecipe')
def remove_recipe():
    rec_id = request.args.get('id')
    SQLModel.delete_by_attrs('recipes', 'id', rec_id)
