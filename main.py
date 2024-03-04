class UserInfo:
    def __init__(self):
        self.name = self.get_name()
        self.gender = self.get_gender()
        self.age = self.get_age()
        self.weight = self.get_weight()
        self.height = self.get_height()
        self.daily_calories_intake = self.get_calories("Enter your daily calorie intake: ")
        self.water_intake = int(input("Enter your daily water intake (in liters): "))
        self.weight_goal = float(input("Enter your weight goal (in kg): "))
        self.TBW=self.calcTBW()
        self.BMR=self.calcBMR()
        self.ideal_weight=self.calc_ideal()
         

    def get_name(self):
        while True:
            name = input("Enter your name: ")
            if name.strip():
                return name.strip()
            else:
                print("Invalid name input. Please enter a name.")

    def get_gender(self):
        while True:
            gender = input("Enter your gender: ").lower()
            if gender in ['male', 'female']:
                return gender
            else:
                print("Invalid gender input. Please choose either (male or female).")

    def get_age(self):
        while True:
            try:
                age = int(input("Enter your age: "))
                if age > 0:
                    return age
                else:
                    print("Invalid age input. Please enter a valid age number.")
            except ValueError:
                print("Invalid age input. Please enter a valid integer.")

    def get_weight(self):
        while True:
            try:
                weight = float(input("Enter your weight (in kg): "))
                if weight > 0:
                    return weight
                else:
                    print("Invalid weight input. Please enter a valid weight (in kg).")
            except ValueError:
                print("Invalid weight input. Please enter a valid number.")

    def get_height(self):
        while True:
            try:
                height = float(input("Enter your height (in meters): "))
                if height > 0:
                    return height
                else:
                    print("Invalid height input. Please enter a valid height (in meters).")
            except ValueError:
                print("Invalid height input. Please enter a valid number.")

    def get_calories(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                
    def calcTBW(self):                                         # height in cm, weight in kg
     if self.age<18 : 
        if self.gender=="male" and self.height<132.7:
            Total_body_water= -1.927 + 0.465 * self.weight + 0.045 * self.height
        elif self.gender=="male" and self.height>=132.7:
            Total_body_water=-21.993 + 0.406 * self.weight + 0.209 * self.height
        elif self.gender=="female" and self.height<110.8:  
            Total_body_water=0.076 + 0.507 * self.weight + 0.013 * self.height
        elif self.gender=="female" and self.height>=110.8:
            Total_body_water=-10.313 + 0.252 * self.weight + 0.154 * self.height
     if self.age>=18:
        if self.gender=="male":
             Total_body_water= 2.447 - (0.09145 * self.age) + (0.1074 * self.height) + (0.3362 * self.weight) 
             
        elif self.gender=="female":
            Total_body_water= -2.097 + (0.1069 * self.height) + (0.2466 * self.weight)
     return Total_body_water
    

    def calcBMR(self):                                        # height in cm, weight in kg
        if self.gender=="male":
            BMR = 88.362 + (13.397 * self.weight ) + (4.799 * self.height ) - (5.677 * self.age )
        elif self.gender=="female":
            BMR = 447.593 + (9.247 * self.weight ) + (3.098 * self.height ) - (4.330 * self.age )
        return BMR
    
    def calc_ideal(self):
         if self.gender=="male":
            ideal_weight = 50 + (0.91 * (self.height - 152.4))
         elif self.gender=="female":
            ideal_weight = 45.5 + (0.91 * (self.height - 152.4))
         return ideal_weight

   


    def display_info(self):
        print("\nUser Information:")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} meters")
        print(f"Daily Calorie Intake: {self.daily_calories_intake} calories")
        print(f"Daily Water Intake: {self.water_intake} liters")
        print(f"Weight Goal: {self.weight_goal} kg")
        print(f"Total Body Water : {round(self.TBW,2)} litres")
        print(f"Basal Metabolic Rate (BMR) : {round(self.BMR,2)} calories/day")
        print(f"Ideal Weight based on given height : {round(self.ideal_weight,2)} kg")

user_info = UserInfo()

# Display the user's information
user_info.display_info()
