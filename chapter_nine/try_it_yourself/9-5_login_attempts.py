class Users:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        message = f"The users first name is {self.first.title()} and their last name is " \
                  f"{self.last.title()} and they're {self.age} year's old."
        print(message)

    def greet_user(self):
        message = f"Hi {self.first.title()} {self.last.title()}"
        print(message)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_one = Users("Isaac", "Jaramillo", 24)
user_two = Users("Dillon", "Waisner", 21)

user_two.describe_user()
user_two.greet_user()

user_one.describe_user()
user_one.greet_user()

user_one.increment_login_attempts()
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.reset_login_attempts()
print(user_one.login_attempts)
