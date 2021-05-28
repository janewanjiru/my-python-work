class Car:
    def __init__(self,carColor,carMileage,carModel):
        self.carColor=carColor
        self.carMileage=carMileage
        self.carModel=carModel
    def carMileage(self):
        return f"The carColor {self.carColor},has a mileage of {self.carMileage}"
    def carModel(self):
        return f"My {self.carModel},has a speed of 180km/hr"
