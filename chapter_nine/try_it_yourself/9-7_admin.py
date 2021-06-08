class Users:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def describe_user(self):
        message = f"The users first name is {self.first.title()} and their last name is " \
                  f"{self.last.title()} and they're {self.age} year's old."
        print(message)

    def greet_user(self):
        message = f"Hi {self.first.title()} {self.last.title()}"
        print(message)


class Admin(Users):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = ["Can add post", "Can edit post", "Can delete post"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


myAdmin = Admin("Isaac", "Jaramillo", 24)
myAdmin.privileges = ['Like post', 'Delete user', 'Ban user']

myAdmin.describe_user()
myAdmin.show_privileges()
