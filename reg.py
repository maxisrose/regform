from flask import Flask, render_template, request, redirect, session, flash
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
app = Flask(__first_name__)
app.secret_key = 'SecretStuff'

@app.route('/')

def index():
	return render_template('index.html')

@app.route('/submission')
def registration():
	if len(request.form['first_name']) < 1:
		flash("first name cannot be empty!")
	elif not NAME_REGEX.match(request.form['first_name']):
		flash("Names don't have numbers")

	if len(request.form['first_name']) < 1:
		flash("first name cannot be empty!")
	elif not NAME_REGEX.match(request.form['first_name']):
		flash("Names don't have numbers")

	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")

	if len(request.form['password']) < 8:
		flash("Password needs at least 8 characters!")
	elif not request.form['password']!=request.form['pass_conf']:
		flash("Passwords do not match")


	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['pass_conf'] = request.form['pass_conf']

	return redirect('/')