# Try while True and use function in a loop.


def joinname(fn, ln):
    print('Hello! '+fn+' '+ln+'.')


while True:
    print('Please tell me your name.')
    print('Enter Q to quit.')
    fn = input('First name: ')
    if fn == 'Q':
        print('End.')
        break
    ln = input('Last name: ')
    if fn == 'Q':
        print('End.')
        break
    joinname(fn, ln)

#%%

# Try Class. Following example on textbook.

class Dog():

    def __init__(self, name, age):  # self suffix variable can be used by all methods within the class.
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')  # .title() make string in title format.

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


my_dog = Dog('bill', 3)     # Name a class with Upper case, name an object with lower case.
your_dog = Dog('susan', 7)

print("My dog's name is " + my_dog.name.title() + '.')
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + '.')
print('Your dog is ' + str(your_dog.age) + ' years old.')
your_dog.roll_over()


#%%

# Try problem on textbook.

class Restaurant():

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print('This restaurant is called ' + self.restaurant_name.title() + ', and provides ' + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now opening.')

    def read_number_served(self):
        print(self.restaurant_name.title() + ' is now serving ' + str(self.number_served) + ' people.')

    def set_number_served(self, num):
        if num >= 0:
            self.number_served = num
        else:
            print('Error!')

    def increment_number_served(self, add_num):
        self.number_served += add_num



while True:
    print('Please enter basic information about your restaurant.')
    print('(Enter Q to quit.)')
    name = input('Restaurant name: ')
    if name == 'Q':
        break
    type = input('Cuisine type: ')
    if name == 'Q':
        break
    num = int(input('Serving people number: '))
    restaurant = Restaurant(name, type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant.set_number_served(num)
    restaurant.read_number_served()

#%%

# Create a Car class.

class Car():
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + self.color
        return long_name

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:    # Forbid rolling back the odometer
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # Forbid rolling back the odometer
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')


my_new_car = Car('Audi', 'A6', 'Black', 2018)
my_new_car.update_odometer(200)
my_new_car.increment_odometer(-5)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#%%
