# Temp converter


def main():

    print("This program will convert temperatures from Celsius to Fahrenheit"
          " or vice versa.")

    def temp_converter():
        choice = input("Please enter C for Celsius or F for Fahrenheit: ").lower()
        user_temp = int(input("Please enter the temperature as an integer: "))

        if choice == "c":
            celsius = user_temp
            temperature = celsius * 9 /5 + 32
            print(temperature)
        elif choice == "f":
            fahrenheit = user_temp
            temperature = (fahrenheit - 32) * 5 / 9
            print(temperature)

    temp_converter()

main()


        
    


