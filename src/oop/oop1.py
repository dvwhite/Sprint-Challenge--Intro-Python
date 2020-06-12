# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# The base class is the Vehicle class
class Vehicle:
    """The base class for all vehicles"""
    pass


class GroundVehicle(Vehicle):
    """The GroundVehicle subclass of Vehicle"""
    pass


class Car(GroundVehicle):
    """The Car subclass of GroundVehicle"""
    pass


class Motorcycle(GroundVehicle):
    """The Motorcyle subclass of GroundVehicle"""
    pass


class FlightVehicle(Vehicle):
    """The FlightVehicle subclass of Vehicle"""
    pass


class Airplane(FlightVehicle):
    """The Airplane subclass of FlightVehicle"""
    pass


class Starship(FlightVehicle):
    """The Starship subclass of Flightvehicle"""
    pass
