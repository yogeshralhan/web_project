# Main Page 

import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import *
from flask import request,redirect,url_for
from db1 import *

app= Flask(__name__)
app.config['SECRET_KEY']='hard to guess'
#app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
#First Page (register-login)

@app.route('/first')
def first():
    return render_template('first.html')


#Register New User Page

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method=='GET':
		return render_template('register.html')
	else:

	        name=request.form['Name']
	        email=request.form['Email']
	        password=request.form['Password']
	        confirm=request.form['Confirm_Password']
	try :

		if (registration.objects.get(email_db=email)):
			flash(" email already exists ")
			return redirect(url_for('register'))
	except DoesNotExist:
		if (password==confirm):
			reg=registration(name_db=name,email_db=email,password_db=password).save()
			flash("Registration Successful !")
			return redirect(url_for('login'))
		else:
			flash("Password Mismatch")
			return redirect(url_for('register'))





#Login Existing User PAge

@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		email1=request.form['EMAILID']
		pass1= request.form['PASSWORD']







if __name__ == '__main__':
	app.run(debug=True)
