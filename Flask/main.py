from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
            
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
     app.run(host='0.0.0.0')
