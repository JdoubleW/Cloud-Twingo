from flask import Flask, render_template, url_for, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.maf  # Select the database
users = db.users  # Select the collection name


@app.route('/')
def index():
    if 'username' in session:
        return render_template('profile.html')

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    user_info = users.find_one({'username': request.form['username']})

    if user_info:
        pass_in_form = request.form['pass']
        pass_in_db = user_info['password']
        if check_password_hash(pass_in_db, pass_in_form):
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        existing_user = users.find_one({'username': username})

        if existing_user is None:
            password = request.form['pass']
            hash_pswd = generate_password_hash(password)
            users.insert({'username': username, 'password': hash_pswd})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')


@app.route("/logout")
def logout():
    session['username'] = False
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True, host='0.0.0.0')
