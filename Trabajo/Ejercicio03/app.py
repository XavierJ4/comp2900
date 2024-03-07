def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

fahrenheit = 78

print("La temperatura", fahrenheit, "Fahrenheit equivale a", fahrenheit_a_celsius(fahrenheit), "Celsius.")
