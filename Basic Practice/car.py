# Car class.

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
