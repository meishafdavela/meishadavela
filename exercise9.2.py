class Restaurant:
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open. Come on in!")
 
 
restaurant_1 = Restaurant('Pagi Sore', 'Indonesian')
restaurant_2 = Restaurant('Sushi Tei', 'Japanese')
restaurant_3 = Restaurant("Domino's Pizza", 'Italian')
 
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()