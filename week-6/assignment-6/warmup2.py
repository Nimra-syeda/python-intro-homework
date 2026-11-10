# Warmup-2 Functions that return values

def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius *9/5+32
    return fahrenheit
def fahrenheit_to_celcius(fahrenheit):
    celcius =(fahrenheit-32)*5/9
    return celcius

print(f"0°C = {celcius_to_fahrenheit(0):.1f}°F")
print(f"45°C = {celcius_to_fahrenheit(45):.1f}°F")
print(f"100°F = {fahrenheit_to_celcius(100):.1f}°C")
print(f"50°F = {fahrenheit_to_celcius(50):.1f}°C")