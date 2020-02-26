from flask import Flask, render_template, request, redirect, url_for, jsonify, session, abort # For flask implementation
from pymongo import MongoClient

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.maf  # Select the database
users = db.users  # Select the collection name


@app.route('/maf/api/users', methods=['GET'])
def get_all_users():
    output = []
    for u in users.find():
        output.append({'user_id': u['user_id'], 'uname': u['uname'], 'passwd': u['passwd']})
    return jsonify({'result': output})

@app.route('/maf/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    u = users.find_one({'user_id' : user_id})
    if u:
        output = {'user_id': u['user_id'], 'uname': u['uname'], 'passwd': u['passwd']}
    else:
        output = "No such id"
    return jsonify({'result': output})

@app.route('/maf/api/users', methods=['POST'])
def create_user():
    if not request.json or not 'uname' in request.json:
        abort(400)
    new = []
    get = users.find()
    user = {
        'uname': request.json['uname'],
        'passwd': request.json['passwd']
    }
    new.append(user)
    return jsonify({'user': user}), 201


if __name__ == "__main__":
     app.run(host='0.0.0.0')