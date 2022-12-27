class Car:
    '''The model of a Car
    attributes: make, model, year, odometer_reading
    behaviour: travel
    '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.trips = 0
    
    def describe_car(self):
        '''decribe the car'''
        print(f"The car is a {self.make} {self.model} from {self.year}.")

    def car_name(self):
        return f"{self.make} {self.model} {self.year}"

    def read_odometer(self):
        '''print the car's odometer reading'''
        print(f"This car has travelled {self.odometer_reading} km.")
    
    def update_odometer(self, distance):
        '''increment the odometer reading by distance'''
        if distance > 0:
            self.odometer_reading = self.odometer_reading + distance
            self.trips = self.trips + 1
        else: 
            print(f"Distance cannot be negative. Odometer not updated.")
    
    def display_trips(self):
        '''how many trips are done?'''
        return self.trips
class Battery:
    def __init__(self,battery_size=100):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This is a {self.battery_size} kwh battery")
        print(f" the range on the battery is {self.get_range()} km.")
    def get_range(self):
        if self.battery_size >=75:
            self.range =200
        elif self.battery_size >=25 and self. battey_size < 75 :
            self.range=100
        else :
            self.range=5
        return self.range



class ElectricCar(Car):
    def __init__(self,make,model,year):
        super(). __init__(make,model,year)
        self.battery=Battery()
    def describe_car(self):
        print(f" This electric car is a {self.car_name()}.")
        self.battery.describe_battery()