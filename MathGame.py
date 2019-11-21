#!/usr/bin/env python3

from gameclasses import Game


class MathGame(Game):

    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0,0,0,0,0]
        symbolList = []
        operatorDict = {1: " + ", 2: " - ", 3: " * ", 4: " ** "}
        questionString = ""

        for i in range(self.noOfQuestions):
            for j in range(0, 4):
                numberList[j] = randint(1, 9)

            for j in range(1, 4):
                if j == 1:
                    symbolList[j] = operatorDict[randint(1, 4)]
                else:
                    symbolList[j] = operatorDict[randint(1, 4)]
                    while symbolList[j - 1] == "**":
                        symbolList[j] = operatorDict[randint(1, 4)]

        questionString = numberList[0]

        for i in range(1, 4):
            questionString += symbolList[i] + str(numberList[i])

        result = eval(questionString)

        questionString.replace("**", "^")

        userResult = input("Solve the equation: {0}".format(questionString))

        while True:
            try:
                if userResult == result:
                    print(
                        "That's correct! {0} = {1} "
                        .format(questionString, userResult))
                    score += 1
                    break
                else:
                    print(
                        "That's incorrect.  The correct answer is {0}"
                        .format(result))
                    break
            except:
                print("Casting failed for answer - you must enter a number."
                      " You entered: {0}".format(userResult))
                print("Try again")
                userResult = input(
                    "Solve the equation: {0}".format(questionString))
                continue

        return score
