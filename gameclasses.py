#!/usr/bin/env python3


class Game:

    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            print("Minimum question value is 1 - setting to 1")
            self._noOfQuestions = 1
        elif value > 10:
            print("Maximum question value is 10 - setting to 10")
            self._noOfQuestions = 10
        else:
            self._noOfQuestions = value


class BinaryGame(Game):

    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input(
                "Convert the number {0} to binary: ".format(base10))

            while True:
                try:
                    userAnswer = int(userResult, base=2)
                    if userAnswer == base10:
                        print(
                            "That's correct! {0} = {1} "
                            .format(userResult, base10))
                        score += 1
                        break
                    else:
                        print(
                            "That's incorrect.  The correct answer is {:b}"
                            .format(base10))
                        break
                except:
                    print(
                        "Casting failed for answer - you must enter a binary "
                        "number.  You entered: {0}".format(userResult))
                    print("Try again")
                    userResult = input(
                        "Convert the number {0} to binary".format(base10))
                    continue

        return score


class MathGame(Game):

    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1: "+", 2: "-", 3: "*", 4: "**"}
        questionString = ""

        for i in range(self.noOfQuestions):
            for j in range(0, 5):
                numberList[j] = randint(1, 9)

            for j in range(0, 4):
                if j > 0 and symbolList[j - 1] == '**':
                    symbolList[j] = operatorDict[randint(1, 3)]
                else:
                    symbolList[j] = operatorDict[randint(1, 4)]

        questionString = str(numberList[0])

        for i in range(0, 4):
            questionString += symbolList[i] + " " + str(numberList[i + 1])

        result = eval(questionString)
        questionString.replace("**", "^")

        userResult = input("Solve the equation: {0}: ".format(questionString))

        print("Debug***")
        print(
            "User Result: {0}, Actual Result: {1}".format(userResult, result))
        print("{0}, {1}".format(type(userResult), type(result)))

        while True:
            try:
                answer = int(userResult)
                if answer == int(result):
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
                print(
                    "Casting failed for answer - you must enter a number."
                    " You entered: {0}".format(userResult))
                print("Try again")
                userResult = input(
                    "Solve the equation: {0}: ".format(questionString))
                continue

        return score
