class Temperature:
    def __init__(self, value, unit="C"):
        self.value = value
        self.unit = unit.upper()
        if self.unit not in {"C", "F", "K"}:
            raise ValueError("Unit must be 'C', 'F', or 'K'")

    def to_celsius(self):
        if self.unit == "C":
            return self.value
        elif self.unit == "F":
            return (self.value - 32) * 5 / 9
        elif self.unit == "K":
            return self.value - 273.15

    def to_fahrenheit(self):
        if self.unit == "C":
            return (self.value * 9 / 5) + 32
        elif self.unit == "F":
            return self.value
        elif self.unit == "K":
            return (self.value - 273.15) * (9 / 5) + 32

    def to_kelvin(self):
        if self.unit == "C":
            return self.value + 273.15
        elif self.unit == "F":
            return (self.value - 32) * (5 / 9) + 273.15
        elif self.unit == "K":
            return self.value

    def convert(self, unit):
        unit = unit.upper()
        if unit == "C":
            return Temperature(self.to_celsius(), "C")
        elif unit == "F":
            return Temperature(self.to_fahrenheit(), "F")
        elif unit == "K":
            return Temperature(self.to_kelvin(), "K")
        else:
            raise ValueError("Target unit must be 'C', 'F', or 'K'")
        
    def is_freezing(self):
        return self.to_celsius() <= 0

    def is_boiling(self):
        return self.to_celsius() >= 100

    def __add__(self, other):
        if not isinstance(other, Temperature):
            raise TypeError("Can only add Temperature objects")

        if self.unit == "C":
            result_value = self.to_celsius() + other.to_celsius()
        elif self.unit == "F":
            result_value = self.to_fahrenheit() + other.to_fahrenheit()
        elif self.unit == "K":
            result_value = self.to_kelvin() + other.to_kelvin()
        else:
            raise ValueError("Invalid unit for operation")
        
        return Temperature(result_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Temperature):
            raise TypeError("Can only subtract Temperature objects")
    
        if self.unit == "C":
            result_value = self.to_celsius() - other.to_celsius()
        elif self.unit == "F":
            result_value = self.to_fahrenheit() - other.to_fahrenheit()
        elif self.unit == "K":
            result_value = self.to_kelvin() - other.to_kelvin()
        else:
            raise ValueError("Invalid unit for operation")
        
        return Temperature(result_value, self.unit)

    def __repr__(self):
        return f"{self.value:.2f}°{self.unit}"
