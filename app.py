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
			username = request.form['username']
			password = request.form['password']

			with sql.connect("database.db", timeout=1) as con:
				cur = con.cursor()

				query = "SELECT * FROM users WHERE username = '"+username+"'"

				user = cur.execute(query).fetchall()
				if username == user[0][1] and password == user[0][2]:
					session['login'] = True
					session['id'] = user[0]
					session['username'] = user[1]
					return redirect(url_for('owners'))
				else:
					return redirect(url_for('home_page'), msg="Username/password is not correct.")
	except Exception as e:
		return redirect(url_for('home_page'), msg="something went wrong!!!")

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

				query = "SELECT * FROM users WHERE username = '"+username+"'"

				user = cur.execute(query).fetchall()
				if len(user) > 0:
					'''This means that the username is already used'''
					msg= "Username already used"
					return render_template('index.html', msg=msg)
				cur.execute("INSERT INTO users (username, password, name, phone, email, prev) VALUES (?, ?, ?, ?, ?, ?)", (username, password, name, phone, email, 'admin'))
				con.commit()
				msg = "Record successfully added"
				con.close()
				return redirect(url_for('owners'), msg=msg)
	except Exception as e:
		con.rollback()
		msg = "error in insert operation"
		con.close()
		return redirect(url_for('home_page'), msg=msg)


@app.route('/owners')
def owners():
	return render_template('owner.html')


@app.route('/products')
def products():
	return ('Products page, Work inprogress!!!')

@app.errorhandler(404)
def page_not_found(e):
	return('four oh four!!!')

app.run(debug=True)

dict1 = {''}