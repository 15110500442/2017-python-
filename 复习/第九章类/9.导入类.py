from car import *
my_new_car = Car('奥迪','TT',2018)
my_tesla = ElectricCar('tesla','model s',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

