from flask import Flask, render_template, request, redirect, url_for, jsonify, session, \
    abort  # For flask implementation
from pymongo import MongoClient, errors
from bson.objectid import ObjectId


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.maf  # Select the database
users = db.users  # Select the collection name
counters = db.counters


@app.route('/maf/api/users', methods=['GET'])
def get_all_users():
    """
       Function to get all users.
       Done!
    """
    output = []
    for u in users.find():
        output.append({'uname': u['uname'], 'passwd': u['passwd']})
    return jsonify({'result': output})


@app.route('/maf/api/users/<uname>', methods=['GET'])
def get_one_user(uname):
    """
       Function to get a user based on username.
       Done!
    """

    u = users.find_one({'uname': uname})
    _id = ObjectId(u['_id'])
    str_id = str(_id)
    if u:
        output = {'_id': str_id, 'uname': u['uname'], 'passwd': u['passwd']}
    else:
        output = "No such username"
    return jsonify({'result': output})


@app.route('/maf/api/users/<id>', methods=['DELETE'])
def remove_user(id):
    """
       Function to remove the user.
       Development!
    """
    try:
        users.delete_one({"_id": ObjectId(id)})
        # Prepare the response
        return jsonify({'Succes': "User with id " + id + " successfully deleted"}), 204
    except errors.InvalidId:
            # Resource Not found
        return jsonify({'Warning': "User with id " + id + " can not be found "}), 404



@app.route('/maf/api/users', methods=['POST'])
def create_user():
    """
       Function to create a new user.
       Done!
    """
    if not request.json or not 'uname' in request.json:
        return jsonify({'Error': 'Values are missing.'}), 400
    try:
        uname = request.json['uname']
        passwd = request.json['passwd']
        users.insert_one({
            'uname': uname,
            'passwd': passwd
        })
        return jsonify({'message': 'User has been succesfully added'}), 201

    except errors.DuplicateKeyError:
        return jsonify({'Error': 'A user with this username already exists!'}), 500


@app.route('/maf/api/users/<uname>', methods=['PUT'])
def edit_user(uname):
    """
       Function to edit an existing user.
       Development!
    """
    user = [user for user in users if user['uname'] == uname]
    user[0]['passwd'] = request.json.get('passwd', user[0]['passwd'])
    return jsonify({'user': user[0]})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
