#Task 1: Begin by asking the user to enter the temperature in Fahrenheit.
Start = input("Enter the temperature in Fahrenheit: ")
#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
#Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?
try:
    Fahrenheit = int(Start)
    Celsius = (Fahrenheit - 32) * 5/9
except ValueError:
    print("Invalid input. Please enter a valid temperature.")
#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
#Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."
else:
    print(f"{Fahrenheit} degrees Fahrenheit is {Celsius:.2f} degrees Celsius.")
#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.
finally:
    print("Thank you for using the weather forecast application!")
