from .views import Data
from .auth import auth
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Attribute


Calculations=Blueprint('Calculations', __name__)

@Calculations.route('/calculations', methods=['GET', 'POST'])
@login_required
def home():
   user_record=Attribute.query.filter_by(user_id=current_user.id).first()
   height=user_record.height
   weight=user_record.weight
   age=user_record.age
   gender=user_record.gender
   bmi=weight/((height/100)**2)
#male
   if (gender=='Male'):
      bmr=88.362+(13.397*weight)+(4.799*height)-(5.677*age)
      ideal_weight=50+(0.91*(height-152.4))
      if age<18:
        body_fat=(1.51*bmi)-(0.70*age)-2.2    
        if height<132.7:
            Total_water= -1.927 + 0.465 * weight + 0.045 * height
        elif height>=132.7:
            Total_water= -21.993 + 0.406 * weight + 0.209 *height
      elif age>=18:
            Total_water= 2.447 - (0.09145 * age) + (0.1074 * height) + (0.3362 * weight) 
            body_fat=(1.20*bmi)+(0.23*age)-16.2
      


#female      
   else:
       bmr=447.593+(9.247*weight)+(3.098*height)-(4.330*age)
       ideal_weight=45.5+(0.91*(height-152.4))  
       if age<18:
           body_fat=(1.51*bmi)-(0.70*age)-1.4
           if height<110.8:
               Total_water= 0.076 + 0.507 * weight + 0.013 * height
           elif height>=110.8:
               Total_water= -10.313 + 0.252 * weight + 0.154 * height
       elif age>=18:
           Total_water= -2.097 + (0.1069 * height) + (0.2466 * weight)
           body_fat=(1.20*bmi)+(0.23*age)-5.4


#both
   if 16 <= bmi < 18.5 and body_fat < 10:
            physique="Underweight"
   elif 18.5 <= bmi < 25 and 8 <= body_fat < 20:
            physique= "Fit"
   elif 25 <= bmi < 30 and 18 <= body_fat < 25:
           physique= "Overweight"
   elif bmi >= 30 and body_fat >= 25:
            physique= "Obese"
   else:
            physique= "Normal"       


   height = round(height, 2)
   weight = round(weight, 2)
   bmi = round(bmi, 2)
   bmr = round(bmr, 2)
   ideal_weight = round(ideal_weight, 2)
   body_fat = round(body_fat, 2)
   Total_water = round(Total_water, 2)
   return render_template('User.html', ht=height, wt=weight,age=age,bmi=bmi,gnd=gender,phsq=physique,bmr=bmr,iw=ideal_weight,bf=body_fat,tw=Total_water ,user=current_user)





