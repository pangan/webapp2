from flask import Blueprint, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, validators

amirblue2=Blueprint('amirblue2',__name__, template_folder='templates')

@amirblue2.route('/amir2', methods=['GET', 'POST'])
def amir2():
    form = MyForm(request.form)
    print form.errors
    if request.method == 'POST' and form.validate():
        print form.username.data

        flash('Thanks for registering')
        return "OK"
    return render_template('form.html', form=form)

class MyForm(Form):
	username = StringField('Username', [validators.Length(min=2, max=3)])