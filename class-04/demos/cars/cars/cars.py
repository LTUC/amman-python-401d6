# Delcare a class in python
class Vehicle:
    """
    Models a vehicle
    """

    production = {}

    def __init__(self, color, wheels=0, drivers=[]):
        """
        The constructor function of our class.
        It is used to initilize the variables for the instance we are creating.
        """
        # self refers to the instance that is created when the contructor is called
        self.color = color
        self.wheels = wheels
        self.drivers = drivers

        Vehicle.production[str(wheels)] = Vehicle.production.get(str(wheels), 0) + 1

    # instance methods
    def drive(self):
        if self.wheels <= 2:
            print("squeak squeak squeak")
        else:
            print("vroom")

    @classmethod
    def produced(cls, wheels):
        """
        Returns the total amount of vehicles produced based on number of wheels
        """
        return cls.production.get(str(wheels), 0)

    @staticmethod
    def get_manufacturer():
        print("D6")


if __name__ == "__main__":
    # create an instance
    darios_ride = Vehicle("red")
    darios_ride1 = Vehicle("pink")
    darios_ride2 = Vehicle("yellow")
    bashars_ride = Vehicle("white", 4, ["Bashar", "Ahmad", "Mona"])

    # we use dot notation to access properties and methods of the class
    print(darios_ride.color)
    print(Vehicle.produced(2))
    print(Vehicle.produced(4))
    print(darios_ride.get_manufacturer())
    print(Vehicle.get_manufacturer())
