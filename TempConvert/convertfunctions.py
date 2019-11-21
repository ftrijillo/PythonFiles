def KelvinToFahrenheit(Temperature):
    if Temperature < 0:
        return None
    else:
        return ((Temperature-273)*1.8)+32

def KelvinToCelsius(Temprature):
    if Temprature < 0:
        return None
    else:
        return ((Temprature - 273.15))

def FahrenheitToKelvin(Temprature):
    temp = ((Temprature - 32) * 5//9) + 273.15
    if temp < 0:
        return None
    else:
        return temp

def FahrenheitToCelsius(Temprature):
    return ((Temprature - 32) * 5//9)

def CelsiusToKelvin(Temprature):
    temp = ((Temprature + 273.15))
    if temp < 0:
        return None
    else:
        return temp

def CelsiusToFahrenheit(Temprature):
    return ((Temprature * 9//5)+32)