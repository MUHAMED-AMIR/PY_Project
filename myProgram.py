class Vehicle:
       def __init__(self, number_of_wheels, type_of_tanks, seating_capacity, maximum_velocity):
                         self.type_of_tank = type_of_tanks
                         self.number_of_wheels = number_of_wheels
                         self.seating_capacity = seating_capacity
                         self.maximum_velocity = maximum_velocity

       def drive(self):
             print('The Vehicle is in driving mode now')

class ElectricCar(Vehicle):
       def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
          Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)

vios = Vehicle('4', 'petrol', 5, 180 )
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capacity)
print(vios.maximum_velocity)

BlueSG= ElectricCar('4',  5,  150)
BlueSG.drive()