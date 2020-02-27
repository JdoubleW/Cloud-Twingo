from flask import Flask, render_template, request, redirect, url_for, jsonify, session, abort # For flask implementation
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
       Development!
    """
    u = users.find_one({'uname' : uname})
    if u:
        output = {'_id': ObjectId('_id'), 'uname': u['uname'], 'passwd': u['passwd']}
    else:
        output = "No such username"
    return jsonify({'result': output})

@app.route('/maf/api/users/<int:_id>', methods=['DELETE'])
def remove_user(_id):
    """
       Function to remove the user.
       Development!
    """
    try:
        # Delete the user
        delete_user = users.delete_one({"_id": str(_id)})

        if delete_user.deleted_count > 0 :
            # Prepare the response
            return "User with id " + _id +" succesfully deleted", 204
        else:
            # Resource Not found
            return "User can not be found ", 404
    except:
        # Error while trying to delete the resource
        # Add message for debugging purpose
        return "", 500

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

@app.route('/maf/api/users', methods=['PUT'])
def edit_user():
    """
       Function to edit an existing user.
       Development!
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


if __name__ == "__main__":
     app.run(host='0.0.0.0')