import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'boxsetReviews'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@datacentriccluster-snqmw.mongodb.net/boxsetReviews?retryWrites=true&w=majority'

mongo = PyMongo(app)
    

@app.route('/')
def index():
    return render_template("index.html", review=mongo.db.review.find())

@app.route('/add_new') 
def add_new():
    return render_template("typeofshow.html", genre=mongo.db.genre.find())


@app.route('/add_boxset') 
def add_boxset():
    return render_template("addseries.html", addboxset=mongo.db.addboxset.find())

@app.route('/add_user') 
def add_user():
    return render_template("userinfo.html", user=mongo.db.user.find())

@app.route('/home_page') 
def home_page():
    return render_template("home.html", homepage=mongo.db.homepage.find())


if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=5000,
        debug=True)
