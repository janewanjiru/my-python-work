class Dog:
    def __init__(self,dogColor,dogName,dogBreed,):
        self.dogColor=dogColor
        self.dogName=dogName
        self.dogBreed=dogBreed
    def running(self):
        return f"My dog is {self.dogName},she is {self.dogBreed}"
    def bark(self):
        return f"My dog is {self.dogColor} ,she is {self.dogBreed}"    