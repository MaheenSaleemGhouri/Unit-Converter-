from random import choice
import streamlit as st


st.header('💫 "Unit Converter"')


if choice == 1:
    length = float(input("Enter Your Length in meters: "))
    print("1 - Kilometers\n2 - Feet")
    length_choice = int(input("Enter Your Choice: "))
    
    if length_choice == 1:
        print(f"{length / 1000} kilometers")
    elif length_choice == 2:
        print(f"{length * 3.28084} feet")
    else:
        print("Invalid choice")

elif choice == 2:
    temperature = float(input("Enter Temperature in Celsius: "))
    print(f"{temperature * 9/5 + 32} Fahrenheit")

elif choice == 3:
    weight = float(input("Enter Weight in Kilograms: "))
    print(f"{weight * 2.20462} Pounds")

elif choice == 4:
    volume = float(input("Enter Volume in Liters: "))
    print(f"{volume * 0.264172} Gallons")

elif choice == 5:
    time = float(input("Enter Time in Seconds: "))
    print(f"{time / 60} Minutes")

elif choice == 6:
    data = float(input("Enter Data in Bytes: "))
    print(f"{data / 1024} Kilobytes")

elif choice == 7:
    currency = float(input("Enter Currency in Dollars: "))
    print(f"{currency * 0.014} Euros")

elif choice == 8:
    area = float(input("Enter Area in Square Meters: "))
    print(f"{area * 10.7639} Square Feet")

elif choice == 9:
    speed = float(input("Enter Speed in Kilometers per Hour: "))
    print(f"{speed * 0.621371} Miles per Hour")

elif choice == 10:
    power = float(input("Enter Power in Watts: "))
    print(f"{power * 0.00134102} Horsepower")

elif choice == 11:
    pressure = float(input("Enter Pressure in Pascals: "))
    print(f"{pressure * 0.000145038} Pounds per Square Inch")

elif choice == 12:
    energy = float(input("Enter Energy in Joules: "))
    print(f"{energy * 0.000239006} Calories")

elif choice == 13:
    force = float(input("Enter Force in Newtons: "))
    print(f"{force * 0.224809} Pounds")

elif choice == 14:
    density = float(input("Enter Density in Kilograms per Cubic Meter: "))
    print(f"{density * 0.001} Grams per Cubic Centimeter")

elif choice == 15:
    angle = float(input("Enter Angle in Degrees: "))
    print(f"{angle * 0.0174533} Radians")

elif choice == 16:
    information = float(input("Enter Information in Bits: "))
    print(f"{information * 0.125} Bytes")

else:
    print("Invalid Choice")  # hr unit me laga k do
