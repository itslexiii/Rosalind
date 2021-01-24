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

    def describe_restaurant(self):
        print('This restaurant is called ' + self.restaurant_name.title() + ', and provides ' + self.cuisine_type + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now opening.')


while True:
    print('Please enter basic information about your restaurant.')
    print('(Enter Q to quit.)')
    name = input('Restaurant name: ')
    if name == 'Q':
        break
    type = input('Cuisine type: ')
    if name == 'Q':
        break
    restaurant = Restaurant(name, type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


#%%