#!/usr/bin/python3
import convertfunctions as cf
import utility as ut

while True:
    print('''
        Convert Menu:
        1 - Kelvin to Fahrenheit
        2 - Kelvin to Celsius
        3 - Fahrenheit to Kelvin
        4 - Fahrenheit to Celsius
        5 - Celsius to Kelvin
        6 - Celsius to Fahrenheit

        quit - Exit Program
        ''')
    
    #Get selection from user
    type = input("Enter selection: ")
    if type == 'quit':
        quit()

    #Make sure selection is within range and is a number
    try:
        if int(type) < 1 or int(type) > 6:
            print("Select a number between 1 and 6")
            continue
    except ValueError:
        print("Please enter a number!")
        continue

    #Get temp to convert - make sure this is a number!
    ctemp = input("Enter temp to convert: ")
    try:
        int(ctemp)
    except ValueError:
        print("Please enter a number!")
        continue

    if type == "1":
        temp = cf.KelvinToFahrenheit(int(ctemp))
        ut.printOutput("Kelvin", "Fahrenheit", ctemp, temp)

    elif type == "2":
        temp = cf.KelvinToCelsius(int(ctemp))
        ut.printOutput("Kelvin", "Celsius", ctemp, temp)

    elif type == "3":
        temp = cf.FahrenheitToKelvin(int(ctemp))
        ut.printOutput("Fahrenheit", "Kelvin", ctemp, temp) 

    elif type == "4":
        temp = cf.FahrenheitToCelsius(int(ctemp))
        ut.printOutput("Fahrenheit", "Celsius", ctemp, temp) 

    elif type == "5":
        temp = cf.CelsiusToKelvin(int(ctemp))
        ut.printOutput("Celsius", "Kelvin", ctemp, temp) 

    elif type == "6":
        temp = cf.CelsiusToFahrenheit(int(ctemp))
        ut.printOutput("Celsius", "Fahrenheit", ctemp, temp) 

    input("Press enter to continue...")
