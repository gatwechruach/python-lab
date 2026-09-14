name = input("Gatwech Ruach Karkuon: ")
number = float(input("Enter a number: "))
print("Square:", square(number))
print(greet(name))
if is_even(number):
    print("The number is even.")
else:
    print("The number is odd.")
    print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))