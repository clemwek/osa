from flask import (Flask, render_template, flash, request,
					 url_for, redirect, session)
from wtforms import Form, TextField, PasswordField, validators
from passlib.hash import sha256_crypt

import sqlite3 as sql
import gc
from flask import g

app = Flask(__name__)

DATABASE = 'database.db'

@app.route('/')
def home_page():
	# flash("Flash test!!!")
	return render_template('index.html')


@app.route('/signin', methods = ['POST', 'GET'])
def signin():
	try:
		if request.method == 'POST':
			attempted_username = request.form['username']
			attempted_password = request.form['password']

			if attempted_username == 'admin' and attempted_password == 'password':
				return redirect(url_for('owners'))
			else:
				return redirect(url_for('home_page'))
	except Exception as e:
		return redirect(url_for('home_page'))


# class signup(Form):
	# """docstring for ClassName"""
	# username = TextField('Username', [validators.Length(min=4, max=20)])
	# password = PasswordField('password', [validators.Required(), 
	# 	validators.EqualTo('confirm', message='Passwords must match.')])
	# confirm = PasswordField('Repeart password')
	# email = TextField('Email Adress', [validators.Length(min=10, max=50)])
	# phone_number = TextField('Phone number', [validators.Length(min=10, max=15)])
	# name = TextField('Name', [validators.Length(min=5, max=50)])
		

@app.route('/signup/', methods=['POST'])
def signup():
	try:
		msg = 'Not assigned!!!!'

		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']
			confirm = request.form['confirm']
			name = request.form['name']
			phone = request.form['phone_number']
			email = request.form['email']


			with sql.connect("database.db", timeout=1) as con:
				cur = con.cursor()

				cur.execute("INSERT INTO users (username, password, name, phone, email, prev) VALUES (?, ?, ?, ?, ?, ?)", (username, password, name, phone, email, 'admin'))
				con.commit()
				msg = "Record successfully added"
	except Exception as e:
		con.rollback()
		msg = "error in insert operation"
	finally:
		return (msg)
		con.close()


@app.route('/owners')
def owners():
	return ('Work inprogress!!!')


@app.route('/products')
def products():
	return ('Products page, Work inprogress!!!')

@app.errorhandler(404)
def page_not_found(e):
	return('four oh four!!!')

app.run(debug=True)

dict1 = {''}