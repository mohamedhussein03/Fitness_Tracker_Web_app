class UserInfo:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.gender = input("Enter your gender: ")
        self.age = int(input("Enter your age: "))
        self.weight = float(input("Enter your weight (in kg): "))
        self.height = float(input("Enter your height (in meters): "))
        self.daily_calories_intake = int(input("Enter your daily calorie intake: "))
        self.water_intake = int(input("Enter your daily water intake (in liters): "))
        self.weight_goal = float(input("Enter your weight goal (in kg): "))

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


# Create an instance of the UserInfo class
user_info = UserInfo()

# Display the user's information
user_info.display_info()
