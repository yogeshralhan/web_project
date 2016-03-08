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

@app.route('/out')

def out():
	return render_template('out.html')

@app.route('/common')

def common():
	return render_template('common.html')
	

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
        






@app.route('/buy',methods=['GET','POST'])

def buy():
	print "1"
	if request.method=='GET':
		return render_template('buy.html')
	else:
		quantity1=request.form['Quantity']
		address1=request.form['Address']
		contact1=request.form['Contact']

		buy=purchase_db(quantity=quantity1,address=address1,contact=contact1).save()
		
		# n=input_db.objects.get(count=count1)
		# m=purchase_db.objects.get(quantity=quantity1)

		if(int(quantity1) > 5):
			print "in1"
			return redirect(url_for('out'))
		else:	
			print "in8"
			v="Purchase Done"
			return render_template('buy.html',v=v)


			
			


#Login Existing User PAge

@app.route('/login',methods=['GET','POST'])

def login():

	if request.method=='GET':
		return render_template('login.html')
	else:
		print "Reached here"
		email1=request.form['Email']
		pass1= request.form['Password']
		print email1

		if(email1=='yogesh@gmail.com' and  pass1=='yogesh'):
			print "ders"
			return redirect('add_item')

		else:


			try:
				print "kkdfsf"
				if(registration.objects.get(email_db=email1,password_db=pass1)):


					print "Sffsf"

				# user = User()
				# user.id = email1
				# flask_login.login_user(user)
					return render_template('common.html')
				
			
			except DoesNotExist:
				flash("Please Register Email")
				return redirect(url_for('first'))



	



@app.route('/add_item',methods=['GET','POST'])
#@flask_login.login_required
def add_item():
		print "hey 0"
		#current_email= flask.ext.login.current_user.id
		if request.method=='GET':
			return render_template('add_item.html')
		else:
			print "hey 1"
			name11=request.form['pname']
			image1=request.form['pimage']
			price11=request.form['pprice']
			size11=request.form['psize']
			brand11=request.form['pbrand']
			color11=request.form['pcolor']
			count1=request.form['pcount']
			print name11
			#image11=request.form['Image']
	
			print "hey 2"#item=Bookmark_db.objects.get(name=name,price=price)
			inputs=input_db(name=name11,image=image1,price=price11,brand=brand11,color=color11,size=size11,count=count1).save()
			print "hey 3"
			print "hey 4"
			list1=[]
			for each in input_db.objects():
				list1.append(each.to_mongo())
			return render_template('common.html',l=list1)
			#name=name11,price=price11,brand=brand11,color=color11,size=size11)
			




	# if request.method=='POST':
	# 	username=request.form('Username')
	# 	user= {'nickname' : username  }
	# 	return render_template('user_page1.html',title='User HomePage',user=user)






if __name__=='__main__':
	app.run(debug=True)
