class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print("The " + self.restaurant_name.title() + " is open. Come inside!")

    def describe_restaurant(self):
        print("The " + self.restaurant_name + " serves " + self.cuisine_type.title() + " cuisine.")

    def number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, increment_served):
        self.number_served += increment_served

    def set_number_served(self, number):
        self.number = number

restaurant = Restaurant('jollibee', 'fast food')
restaurant.describe_restaurant()

restaurant.number_served(10)
print(restaurant.number_served)

restaurant.number_served = 0
restaurant.set_number_served(24)
restaurant.open_restaurant()
restaurant.set_number_served(32)
print(restaurant.number_served)

restaurant.number_served = 0
restaurant.increment_number_served(46)
print(restaurant.number_served)