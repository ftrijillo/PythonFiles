#!/usr/bin/env python3

from os import remove, rename

def printInstructions(instruction):
    print(instruction)

def getUserScore(userName):
    content = []
    users = ""

    try:
        users = open("userScores.txt", "r")
    except IOError:
        users = open("userScores.txt", "w")
        users.close()
        return -1

    for user in users:
        name,score = user.split(",")

        if name == userName:
            return int(score)

        content.append(user.split(","))

    return -1

def updateUserScore(newUser, userName, score):

    if(newUser == True):
        users = open("userScores.txt","a")
        users.write(userName + "," + score)
        users.close()
    else:
        usersTmp = open("userScores.tmp", "w")
        users = open("userScores.txt", "r")
        content = []

        for user in users:
            name, newScore = user.split(",")
            if(name == userName):
                 newScore = str(score)

            usersTmp.write("{0},{1}".format(name,newScore))

        users.close()
        usersTmp.close()

    remove("userScores.txt")
    rename("userScores.tmp", "userScores.txt")
