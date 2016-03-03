# Main Page 

import flask
import os
import hashlib
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import *
from flask import request,redirect,url_for
from db1 import *
#from passlib.hash import pbkdf2_sha256   #encrypt & verify password
from flask.ext.login import LoginManager,login_required,current_user,logout_user
import flask.ext.login as flask_login
 
app= Flask(__name__,static_folder="/home/yogesh/web_project/Static")
#print dir(app)
app.config['SECRET_KEY']='hard to guess'
#app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
#First Page (register-login)
#app = Flask(static_folder="/home/yogesh/web_project")
login_manager=LoginManager()
login_manager.init_app(app)


@login_manager.user_loader

def user_loader(email1):
	try:
		if(registration.objects.get(email_db=email1)):
			user=User()
			user.id=email1
			return user
	except DoesNotExist:
		return
	if not registration.objects(email_db=email1):
		return


class User(flask_login.UserMixin):
	pass

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
		
	try:

		if(registration.objects.get(email_db=email)):
			flash(" email already exists ")
			return redirect(url_for('register'))
	
	except DoesNotExist:
	
		if(password==confirm):
			reg=registration(name_db=name,email_db=email,password_db=password).save()
			flash("Registration Successful !")
			return redirect(url_for('login'))
		
		else:
			flash("Password Mismatch")
			return redirect(url_for('register'))

		# if not registration.objects(email_db=email):
		# 	reg=registration(name_db=name,email_db=email,password_db=password).save()
  #           flash('Registration Complete Proceed To Login')
  #           return redirect(url_for('login'))
        





#Login Existing User PAge

@app.route('/login',methods=['GET','POST'])

def login():

	if request.method=='GET':
		return render_template('login.html')
	else:
		email1=request.form['Email']
		pass1= request.form['Password']


		try:
			if(registration.objects.get(email_db=email1)):
				#print registration.objects.get(email_db=email1)
				try:
					if(registration.objects.get(email_db=email1,password_db=pass1)):
						# user = User()
						# user.id = email1
						# flask_login.login_user(user)
						return render_template('user_page2.html')
				except DoesNotExist:
					flash("TRY AGAIN")
					return redirect(url_for('login'))
		
		except DoesNotExist:
			flash("Please Register Email")
			return redirect(url_for('first'))



	if not registration.objects(email_db=email1):
		flash("email not registered please do the registration")

 		return redirect(url_for('first'))



@app.route('/')




	# if request.method=='POST':
	# 	username=request.form('Username')
	# 	user= {'nickname' : username  }
	# 	return render_template('user_page1.html',title='User HomePage',user=user)






if __name__ == '__main__':
	app.run(debug=True)
