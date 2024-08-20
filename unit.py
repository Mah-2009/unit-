# Conversion factors from meters to other units
cons = {
    "meters": 1.0,
    "kilometers": 1e-3,
    "centimeters": 1e2,
    "millimeters": 1e3,
    "miles": 6.2137e-4,
    "yards": 1.0936,
    "feet": 3.2808,
    "inches": 39.3701
}
con={k.upper().strip(): v for k,v in cons.items()}

def unit(first,second ,value):
    first=first.upper().strip()
    second=second.upper().strip()
    if second not in con:
        raise ValueError("Sorry Check The unit")
    
    meter= value/con[first]
    com=value*con[second]
    return com

first_unit = input("Enter first unit: ")
second_unit = input("Enter second unit: ")
value = float(input("Enter the value: "))

result = unit(first_unit, second_unit, value)
print(f"{value} {first_unit} is {result} {second_unit}")