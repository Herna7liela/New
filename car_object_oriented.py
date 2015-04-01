class Car:
    brand = None
    model = None
    year = None
    
    def toString(self):
        return "BRAND: "+ self.brand
# now can go to terminal
# initiate python3
# import Car
# mycar = Car.Car()


#OR
# from Car import *
# mycar = Car()
# mycar
# mycar.toString()
# mycar.brand = "Renault"
# mycar.toString()
# mycar = Car()
# mycar.brand = "Honda"

# from Car import *
# mycar = Car()
# mycar.brand = "Honda"
# mycar.model = "Ballade"
# mycar.year = 1996
# mycar.toString()
# this will give an error because there is an integer and need to make it a string in the above code by saying str(self.year)
