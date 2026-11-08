class User:
    """A simple model of a user profile."""
 
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
 
    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location.title()}")
 
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")
 
 
class Admin(User):
 
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
 
    def show_privileges(self):
        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
 
 
admin = Admin('meisha', 'davela', 'velly', 'davela@example.com', 'bandung')
admin.describe_user()
admin.show_privileges()