class Users:
 
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
 
 
class Privileges:
 
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
 
    def show_privileges(self):
        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
 
 
class Admin(Users):
 
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the parent class, then add a Privileges instance."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()