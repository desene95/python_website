from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", user="Damian")

@auth.route('/logout', methods=['GET','POST'])
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords must be equal', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 7 characters', category='error')
        else:
            flash('Account created', category='success')
    return render_template("sign_up.html")