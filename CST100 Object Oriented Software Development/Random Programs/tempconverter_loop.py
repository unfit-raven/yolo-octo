# Temp converter, loop 5 times

print("This program will convert Celsius temperatures to Fahrenheit, "
      "or Fahrenheit to Celsius. It will run 5 times.")

for i in range(5):
    choice = input("Please enter 'C' for Celsius or 'F' for Fahrenheit: ").lower()
    user_temp = eval(input("Please enter a temperature: "))

    if choice == "c":
        celsius = user_temp
        temperature = celsius * 9 / 5 + 32
        print(temperature)
    elif choice == "f":
        fahrenheit = user_temp
        temperature = (fahrenheit - 32) * 5 / 9
        print(temperature)

print("Program ended.")