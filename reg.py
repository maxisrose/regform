from flask import Flask, render_template, request, redirect, session, flash
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
app = Flask(__name__)
app.secret_key = 'SecretStuff'

@app.route('/')

def index():
	if 'first_name' not in session and 'last_name' not in session and 'email' not in session:
		return render_template('index.html')

	elif 'first_name' not in session and 'last_name' not in session:
		return render_template('index.html', mail=session['email'])

	elif 'first_name' not in session and 'email' not in session:
		return render_template('index.html', last=session['last_name'])

	elif 'last_name' not in session and 'email' not in session:
		return render_template('index.html', first=session['first_name'])

	elif 'first_name' not in session:
		render_template('index.html', last=session['last_name'], mail=session['email'])

	elif 'last_name' not in session:
		return render_template('index.html', first=session['first_name'], mail=session['email'])

	elif 'email' not in session:
		return render_template('index.html', first=session['first_name'], last=session['last_name'])

	else:
		return render_template('index.html', first=session['first_name'], last=session['last_name'], mail=session['email'])
	# return render_template('index.html')

@app.route('/submission', methods=['POST'])
def registration():
	count = 0
	session.clear()
	if len(request.form['first_name']) < 1:
		flash("first name cannot be empty!")
	elif not NAME_REGEX.match(request.form['first_name']):
		flash("Names only have letters")
	else:
		session['first_name'] = request.form['first_name']
		count += 1

	if len(request.form['last_name']) < 1:
		flash("last name cannot be empty!")
	elif not NAME_REGEX.match(request.form['last_name']):
		flash("Names only have letters")
	else:
		session['last_name'] = request.form['last_name']
		count += 1

	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		session['email'] = request.form['email']
		count += 1

	if len(request.form['password']) < 8:
		flash("Password needs at least 8 characters!")
	elif request.form['password']!=request.form['pass_conf']:
		flash("Passwords do not match")
	else:
		session['password'] = request.form['password']
		count += 1


	session['pass_conf'] = request.form['pass_conf']

	if count == 4:
		flash("Thank you for Submitting your form!")

	return redirect('/')


app.run(debug=True)