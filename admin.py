from users import Users
 
 
class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
 
    def show_privileges(self):
        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
 
 
class Admin(Users):
 
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()