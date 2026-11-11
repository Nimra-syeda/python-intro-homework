# Warmup-2 Functions that return values

def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""

    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    """converts a temperature from Fahrenheit to Celsius"""
    celsius =(fahrenheit-32)*5/9
    return celsius

print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"45°C = {celsius_to_fahrenheit(45):.1f}°F")
print(f"100°F = {fahrenheit_to_celsius(100):.1f}°C")
print(f"50°F = {fahrenheit_to_celsius(50):.1f}°C")