class Restaurant:
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open. Come on in!")
 
 
restaurant = Restaurant('Pagi Sore', 'Indonesian')
 
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
 
restaurant.describe_restaurant()
restaurant.open_restaurant()