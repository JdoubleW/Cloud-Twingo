from flask import Flask, render_template, url_for, request, session, redirect, make_response, jsonify, abort, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient, errors
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from flask_login import current_user
import authomatic, json
from config import CONFIG
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.maf  # Select the database
users = db.users  # Select the collection name
authomatic = Authomatic(CONFIG, 'the white rabbit goes to the black wolf', report_errors=False)

@app.route('/')
def index():
    return render_template('index.html')

#    logged_user = session['username']
#    print('De volgende gebruiker is ingelogd: ' + logged_user)
#    print(users.find_one({"username": logged_user}))

@app.route('/login', methods=['POST', 'GET'])
def loginpage():
    if request.method == 'GET':
        return render_template('login.html')

    else:
        user_info = users.find_one({'email': request.form['email']})

        if user_info:
            pass_in_form = request.form['wachtwoord']
            pass_in_db = user_info['password']
            if check_password_hash(pass_in_db, pass_in_form):
                session['logged_in'] = True
                session['email'] = request.form['email']
                return redirect(url_for('profile'))
        return 'Invalid username/password combination'


@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()
            if users.find_one({'email': result.user.email}):
                session['logged_in'] = True
                session['email'] = result.user.email
                return redirect(url_for('profile'))

        # The rest happens inside the template.
        return render_template('verify.html', result=result)

    # Don't forget to return the response.
    return response

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        naam = request.form['naam']
        adres = request.form['adres']
        postcode = request.form['postcode']
        stad = request.form['stad']
        existing_user = users.find_one({'email': email})

        if existing_user is None:
            password = request.form['wachtwoord']
            hash_pswd = generate_password_hash(password)
            users.insert({'naam': naam, 'email': email, 'password': hash_pswd, 'adres': adres, 'postcode': postcode, 'stad': stad})
            session['email'] = request.form['email']
            session['logged_in'] = True
            session['email'] = request.form['email']
            return redirect(url_for('profile'))

        return 'That email already exists!'

    return render_template('register.html')

@app.route('/verify', methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        email = request.form['email']
        naam = request.form['naam']
        adres = request.form['adres']
        postcode = request.form['postcode']
        stad = request.form['stad']
        existing_user = users.find_one({'email': email})

        if existing_user is None:
            password = request.form['wachtwoord']
            hash_pswd = generate_password_hash(password)
            users.insert({'naam': naam, 'email': email, 'password': hash_pswd, 'adres': adres, 'postcode': postcode, 'stad': stad})
            session['email'] = request.form['email']
            session['logged_in'] = True
            session['email'] = request.form['email']
            return redirect(url_for('profile'))

        return 'That email already exists!'

    return render_template('verify.html')

@app.route("/profile")
def profile():
    email = session['email']
    user = users.find_one({'email': email})
    naam = user["naam"]
    print(naam)
    return render_template('profile.html', naam=naam)

@app.route("/profile/settings")
def settings():
    email = session['email']
    user = users.find_one({'email': email})
    naam = user["naam"]
    mail = user["email"]
    adres = user["adres"]
    postcode = user["postcode"]
    stad = user["stad"]
    print(naam)
    return render_template('settings.html', naam=naam, mail=mail, adres=adres, postcode=postcode, stad=stad)

@app.route("/profile/workout")
def workout():
    user = session['naam']
    return render_template('workout.html')

@app.route("/logout")
def logout():
    session.clear()
    return render_template('index.html')

################################################################################################################
############################################# POSTMAN CONFIGURATIE##############################################
################################################################################################################
################################################################################################################

@app.route('/maf/api/users', methods=['GET'])
def get_all_users():
    """
       Function to get all users.
       Done!
    """

    output = []
    for u in users.find():
        output.append({'naam': u['naam'], 'email': u['email'], 'adres': u['adres'],
                       'postcode': u['postcode'], 'stad': u['stad']})
    return jsonify({'result': output})


@app.route('/maf/api/users/<email>', methods=['GET'])
def get_one_user(email):
    """
       Function to get a user based on username.
       Done!
    """

    u = users.find_one({'email': email})
    _id = ObjectId(u['_id'])
    str_id = str(_id)

    if u:
        output = {'_id': str_id, 'naam': u['naam'], 'email': u['email'], 'adres': u['adres'], 'postcode': u['postcode'], 'stad': u['stad']}

    else:
        output = "No such username"

    return jsonify({'result': output})


@app.route('/maf/api/users/<email>', methods=['DELETE'])
def remove_user(email):
    """
       Function to remove the user.
       Done!
    """
    if request.method == 'DELETE':
        u = users.find_one({'email': email})
        if u:
            db_response = users.delete_one({'email': u['email']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'gebruiker verwijderd'}
                return response
            else:
                return jsonify({'error': 'Error gegenereerd'})
        else:
            return jsonify({'ok': False, 'message': 'geen gebruiker gevonden'}), 400


@app.route('/maf/api/users', methods=['POST'])
def create_user():
    """
       Function to create a new user.
       Done!
    """
    if not request.json or not 'naam' in request.json:
        return jsonify({'Error': 'Values are missing.'}), 400

    try:
        naam = request.json["naam"]
        wachtwoord = request.json["password"]
        hash_ww = generate_password_hash(wachtwoord)
        mail = request.json["email"]
        adres = request.json["adres"]
        postcode = request.json["postcode"]
        stad = request.json["stad"]
        users.insert_one({
            'naam': naam,
            'email': mail,
            'password': hash_ww,
            'adres': adres,
            'postcode': postcode,
            'stad': stad
        })
        return jsonify({'message': 'User has been succesfully added'}), 201

    except errors.DuplicateKeyError:
        return jsonify({'Error': 'A user with this username already exists!'}), 500


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True, host='0.0.0.0', port=5000)
