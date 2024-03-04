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

user_info = UserInfo()

# Display the user's information
user_info.display_info()
