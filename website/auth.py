from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Attribute
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Retrieve user from database based on email
        user = User.query.filter_by(email=email).first()

        if user:
            # Check if the entered password matches the user's password
            if user.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.home_page'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('Data.home'))

    return render_template("sign_up.html", user=current_user)



@auth.route('/home', methods=['GET', 'POST'])  
@login_required
def home_page():
    user=User.query.filter_by(id=current_user.id).first()
    name=user.first_name
    attribute=Attribute.query.filter_by(user_id=current_user.id).first()
    if attribute:
     weight=attribute.weight
     height=attribute.height
     age=attribute.age
     weight_goal=attribute.weight_goal
     calorie_intake=attribute.calorie_intake
     water_intake=attribute.water_intake

    else:
     weight="N/A"
     height="N/A"
     age="N/A"
     weight_goal="N/A"
     calorie_intake="N/A"
     water_intake="N/A"

    return render_template("home.html",name=name,weight=weight,height=height,age=age, user=current_user,weight_goal=weight_goal,calorie_intake=calorie_intake,water_intake=water_intake) 

