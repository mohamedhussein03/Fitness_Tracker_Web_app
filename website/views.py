from flask import Blueprint, render_template, request, flash, jsonify,redirect
from flask.helpers import url_for
from flask_login import login_required, current_user
from .models import Attribute,User
from . import db
import json

Data = Blueprint('Data', __name__)

@Data.route('/', methods=['GET', 'POST'])
def home_page():
   return render_template("welcome.html")

@Data.route('/User_data', methods=['GET', 'POST'])

@login_required
def home():
    if request.method == 'POST': 
        height = request.form.get('height')
        weight = request.form.get('weight')
        age = request.form.get('age')
        gender= request.form.get('gender')
        calorie_intake = request.form.get('calorie_intake')
        water_intake = request.form.get('water_intake')
        weight_goal = request.form.get('weight_goal')
        
        
        user_found=Attribute.query.filter_by(user_id=current_user.id).first()
        if user_found:    
            user_found.height=height
            user_found.weight=weight
            user_found.age=age 
            user_found.gender=gender
            user_found.calorie_intake=calorie_intake
            user_found.water_intake=water_intake
            user_found.weight_goal=weight_goal
            if int(height)<0 :flash('Height must be greater than 0', category='error')
            elif int(weight)<0 :flash('Weight must be greater than 0', category='error')
            elif int(age)<0 :flash('Age must be greater than 0', category='error')
            elif int(calorie_intake)<0 :flash('Calorie intake must be greater than 0', category='error')
            elif int(water_intake)<0 :flash('Water intake must be greater than 0', category='error')
            elif int(weight_goal)<0 :flash('Weight goal must be greater than 0', category='error')
            else:
             db.session.commit() 
             return redirect(url_for('Calculations.home'))
        else:  
           new_attribute = Attribute(height=height, weight=weight, age=age,gender=gender,calorie_intake=calorie_intake,water_intake=water_intake,weight_goal=weight_goal, user_id=current_user.id)
           db.session.add(new_attribute)
           db.session.commit()
           flash('Attributes added!', category='success')
           return redirect(url_for('Calculations.home'))
    return render_template("User_data.html", user=current_user)


@Data.route('/subscribtion', methods=['GET', 'POST'])
def price_page():
   return render_template("subscribtion.html")
   