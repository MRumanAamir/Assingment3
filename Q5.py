fahrenheit  = int(input("Enter the temperature in fahrenheit: "));
celsius = int(input("Enter the temperature in celsius: "));

fahren_cel = (fahrenheit - 32) * 5//9;
cel_fahren = (celsius * 9/5) + 32;

print("/nAfter conversion");
print("Celsius: ",fahren_cel,"C");
print("Fahreenheit: ",cel_fahren,"F");