def printOutput(fromTemp, toTemp, ctemp, temp):
    #If either ctemp or temp are None - that means the Kelvin temp is below zero
    #which is impossible
    if ctemp == None or temp == None:
        print("Error: Colder than absolute zero!")
    else:
        print ("{0} {1} = {2:8.2f} {3}".format(ctemp, fromTemp, temp, toTemp))