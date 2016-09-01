from flask import Blueprint, render_template, request, flash
from app import app
from flask_wtf import Form
from wtforms import StringField, validators

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	#return "Hello, Flask!"
	form = MyForm(request.form)
	print form.errors
	print form.validate_on_submit()
	if request.method == 'POST' and form.validate():
		print form.username.data

		print "------>>>>"
		return "OK"
	return render_template('form.html', form=form)



class MyForm(Form):
	username = StringField('username', [validators.Length(min=2, max=6)])

