class Car:
    fuel_type = "Petrol"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return f"Milcah is driving a blue {self.make}" 
    
    def get_model(self):
        return f"Its model is {self.model}"

    def get_year(self):
        return f"I {self.make} I am of model {self.model} and I am of year {self.year}"   

    def drive(self):
        return f"Milcah is driving a blue {self.make} which is {self.model} of {self.year}" 


        