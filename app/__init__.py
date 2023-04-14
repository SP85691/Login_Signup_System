from flask import Flask, render_template, url_for, request
from .database import db

app = Flask(__name__)

# db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

       
    return render_template('login.html')

