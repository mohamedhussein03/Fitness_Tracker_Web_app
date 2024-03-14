import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from math import sqrt

# Create engine
engine = create_engine('sqlite:///fitness_tracker.db', echo=True)
Base = declarative_base()

# Define User class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Float)  # in kg
    weight_goal = Column(Float)  # in kg
    height = Column(Float)  # in cm
    calories_intake_per_day = Column(Integer)
    water_intake_per_day = Column(Integer)
    BMI = Column(Float)
    fat_percentage = Column(Float)
    calories_target = Column(Integer)
    best_weight = Column(Float)
    TBW = Column(Float)  # Total Body Water
    BMR = Column(Float)  # Basal Metabolic Rate
    physique_rating = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', gender='{self.gender}', age='{self.age}', weight='{self.weight}')>"

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define functions
def calculate_BMI(user):
    user.BMI = round(user.weight / ((user.height / 100) ** 2), 2)

def calculate_fat_percentage(user):
    if user.gender.lower() == 'male':
        user.fat_percentage = round((1.20 * user.BMI) + (0.23 * user.age) - 16.2, 2)
    elif user.gender.lower() == 'female':
        user.fat_percentage = round((1.20 * user.BMI) + (0.23 * user.age) - 5.4, 2)

def calculate_calories_target(user):
    if user.weight_goal > user.weight:
        user.calories_target = user.calories_intake_per_day + 500
    elif user.weight_goal < user.weight:
        user.calories_target = user.calories_intake_per_day - 500
    else:
        user.calories_target = user.calories_intake_per_day

def calculate_best_weight(user):
    user.best_weight = round((user.height - 100) - ((user.height - 150) / 4), 2)

def calculate_TBW(user):
    if user.gender.lower() == 'male':
        user.TBW = round((0.50 * user.weight) / (0.10 * user.age), 2)
    elif user.gender.lower() == 'female':
        user.TBW = round((0.45 * user.weight) / (0.10 * user.age), 2)

def calculate_BMR(user):
    if user.gender.lower() == 'male':
        user.BMR = round(88.362 + (13.397 * user.weight) + (4.799 * user.height) - (5.677 * user.age), 2)
    elif user.gender.lower() == 'female':
        user.BMR = round(447.593 + (9.247 * user.weight) + (3.098 * user.height) - (4.330 * user.age), 2)

def output_physique_rating(user):
    BMI_rating = ""
    if user.BMI < 18.5:
        BMI_rating = "Underweight"
    elif 18.5 <= user.BMI < 24.9:
        BMI_rating = "Normal weight"
    elif 24.9 <= user.BMI < 29.9:
        BMI_rating = "Overweight"
    elif user.BMI >= 30:
        BMI_rating = "Obese"
    
    fat_percentage_rating = ""
    if user.gender.lower() == 'male':
        if user.fat_percentage < 8:
            fat_percentage_rating = "Essential fat"
        elif 8 <= user.fat_percentage < 20:
            fat_percentage_rating = "Athletes"
        elif 20 <= user.fat_percentage < 25:
            fat_percentage_rating = "Fitness"
        elif 25 <= user.fat_percentage:
            fat_percentage_rating = "Obese"
    elif user.gender.lower() == 'female':
        if user.fat_percentage < 20:
            fat_percentage_rating = "Essential fat"
        elif 20 <= user.fat_percentage < 33:
            fat_percentage_rating = "Athletes"
        elif 33 <= user.fat_percentage < 39:
            fat_percentage_rating = "Fitness"
        elif 39 <= user.fat_percentage:
            fat_percentage_rating = "Obese"
    
    user.physique_rating = f"BMI: {BMI_rating}, Fat Percentage: {fat_percentage_rating}"

# User input
gender = input("Enter your gender (male/female): ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
weight_goal = float(input("Enter your weight goal in kg: "))
height = float(input("Enter your height in cm: "))
calories_intake_per_day = int(input("Enter your calories intake per day: "))
water_intake_per_day = int(input("Enter your water intake per day in ml: "))

# Create user object
user = User(
    gender=gender,
    name=name,
    age=age,
    weight=weight,
    weight_goal=weight_goal,
    height=height,
    calories_intake_per_day=calories_intake_per_day,
    water_intake_per_day=water_intake_per_day
)

# Calculate user attributes
calculate_BMI(user)
calculate_fat_percentage(user)
calculate_calories_target(user)
calculate_best_weight(user)
calculate_TBW(user)
calculate_BMR(user)
output_physique_rating(user)

# Add user to session and commit
session.add(user)
session.commit()

# Query user
query_user = session.query(User).filter_by(name=name).first()
print("User Details:")
print(f"Name: {query_user.name}")
print(f"Gender: {query_user.gender}")
print(f"Age: {query_user.age}")
print(f"Weight: {query_user.weight} kg")
print(f"Weight Goal: {query_user.weight_goal} kg")
print(f"Height: {query_user.height} cm")
print(f"Calories Intake Per Day: {query_user.calories_intake_per_day}")
print(f"Water Intake Per Day: {query_user.water_intake_per_day} ml")
print(f"BMI: {query_user.BMI}")
print(f"Fat Percentage: {query_user.fat_percentage}")
print(f"Calories Target: {query_user.calories_target}")
print(f"Best Weight: {query_user.best_weight} kg")
print(f"Total Body Water: {query_user.TBW} kg")
print(f"Basal Metabolic Rate: {query_user.BMR} kcal/day")
print(f"Physique Rating: {query_user.physique_rating}")
