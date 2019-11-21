#!/usr/bin/env python3

from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, BinaryGame, MathGame
import sys
import os

try:
    mathInstructions = """
    In this game, you will be given a simple
    arithmetic question.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.
    """

    binaryInstructions = """
    In this game, you will be given a number in base 10.
    Your task is to conver this number to base 2.
    Each correct answer gives you one mark.
    No mark is deducted for wrong answers.
    """

    newUser = True
    userChoice = 0
    bg = BinaryGame()
    mg = MathGame()

    name = input("Please enter your name: ")
    score = int(getUserScore(name))
    print("Current Score: {0}".format(score))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print("Welcome to the Math Game")

    while userChoice != -1:
        game = int(input("Math Game (1) or Binary Game (2)? "))
        while game != 1 and game != 2:
            game = int(input("Math Game (1) or Binary Game (2)? "))

        numPrompt = input(
            "\nHow many questions do you want per game (1 to 10)? ")
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("You did not enter a valid number, please try again")
                numPrompt = input(
                    "\nHow many questions do you want per game (1 to 10)? ")

        if game == 1:
            mg.noOfQuestions = num
            printInstructions(mathInstructions)
            score += mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score += bg.generateQuestions()

        print("\nYour current score is %d" % (score))
        userChoice = int(input("\nPress enter to continue or -1 to end: "))

    updateUserScore(newUser, name, str(score))

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print("An unknown error occured. Program will exit.")
    print(
        "Error: {0} at line {1} in file: {2}"
        .format(e, exc_tb.tb_lineno, fname))
