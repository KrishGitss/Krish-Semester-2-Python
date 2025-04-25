class Converter:
    factors = {"inches": 1, "feet": 12, "yards": 36, "miles": 63360, "kilometers": 39370.1, 
               "meters": 39.37, "centimeters": 0.3937, "millimeters": 0.03937}

    def __init__(self, length, unit):
        if unit not in self.factors:
            raise ValueError("Invalid unit. Choose from: " + ", ".join(self.factors))
        self.length_in_inches = length * self.factors[unit]

    def __getattr__(self, unit):
        if unit in self.factors:
            return lambda: self.length_in_inches / self.factors[unit]
        raise AttributeError(f"'Converter' object has no attribute '{unit}'")

c = Converter(9, 'inches')
print(c.feet())    
print(c.yards())   
print(c.meters())