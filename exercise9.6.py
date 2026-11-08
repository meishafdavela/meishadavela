class Restaurant:
    """A simple model of a restaurant."""
 
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 
    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
 
    def open_restaurant(self):
        """Print a message saying the restaurant is open."""
        print(f"{self.restaurant_name} is open. Come on in!")
 
 
class IceCreamStand(Restaurant):
    """A kind of restaurant that sells ice cream."""
 
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the parent class, then add flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mango']
 
    def display_flavors(self):
        """Display the flavors that are available."""
        print("We have these flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
 
 
stand = IceCreamStand('Sweet Spot', 'dessert')
stand.describe_restaurant()
stand.display_flavors()