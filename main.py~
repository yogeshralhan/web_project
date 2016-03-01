# Main Page 

import flask
from flask import Flask
from flask import render_template
from flask import request
from db2 import *

app= Flask(__name__)


@app.route('/first')
def first():
    return render_template('first.html')

@app.route('/register', methods=['GET','POST'])

def register():
	if request.method=='GET':
		return render_template('register.html')
	else:

        name=request.form['Name']
        email=request.form['Email']
        password=request.form['Password']
        confirm=request.form['Confirm_Password']

f=first

if __name__ == '__main__':
	app.run(debug=True)