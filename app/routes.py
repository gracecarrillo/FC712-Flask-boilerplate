from flask import render_template, redirect, flash, url_for
from flask_wtf import form
from app import app
from app.forms import LoginForm

##########################
# URL routes live here   #
##########################

# home
@app.route('/',methods=['GET', 'POST'])
def index():
    user = { 'username':'Grace' }
    return render_template('index.html', title='Login', user = user, form=form)


# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # when user sends POST request by pressing the submit button
        flash(f'Login requested for user {form.username.data}, remember_me= {form.remember_me.data}')

        # save data on txt file 
        with open(f'app/users_data/{form.username.data}_credentials.txt', 'w') as file:
            file.write(f'{form.username.data}:{form.password.data}')

        return redirect(url_for('index'))
    return render_template('login.html', title='Home', form=form)