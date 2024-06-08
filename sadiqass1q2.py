def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_conversion():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Choose a conversion (1/2/3): ")

        if choice == '3':
            print("Exiting the temperature conversion tool. Goodbye!")
            break

        if choice in ['1', '2']:
            try:
                temp = float(input("Enter the temperature to convert: "))
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
                continue

            if choice == '1':
                result = celsius_to_fahrenheit(temp)
                print(f"Result: {temp}°C = {result}°F")
            elif choice == '2':
                result = fahrenheit_to_celsius(temp)
                print(f"Result: {temp}°F = {result}°C")
        else:
            print("Invalid choice! Please choose a valid conversion option.")

if __name__ == "__main__":

    temperature_conversion()