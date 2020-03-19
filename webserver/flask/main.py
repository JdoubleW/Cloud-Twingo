from flask import Flask, render_template, url_for, request, session, redirect, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from flask_login import current_user
import authomatic, json
from config import CONFIG

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


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True, host='0.0.0.0', port=5000)
