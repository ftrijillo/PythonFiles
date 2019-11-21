#!/usr/bin/env python3

from gameclasses import Game


class BinaryGame(Game):

    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input(
                "Convert the number {0} to binary".format(base10))

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
                        "Casting failed for answer - you must enter a binary"
                        " number.  You entered: {0}".format(userResult))
                    print("Try again")
                    userResult = input(
                        "Convert the number {0} to binary".format(base10))
                    continue

        return score
