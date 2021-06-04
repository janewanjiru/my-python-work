class Car:
    def __init__(self,car_color,car_mileage,car_model):
        self.color=car_color
        self.mileage=car_mileage
        self.Model=car_model
    def carMileage(self):
        return f"The carColor {self.car_color},has a mileage of {self.car_mileage}"
    def carModel(self):
        return f"My {self.car_model},has a speed of 180km/hr"

        