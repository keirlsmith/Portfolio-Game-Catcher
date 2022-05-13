
def welcome_message():
    print("Welcome to the virtual old school origami game (known in some areas as 'Cootie Catcher'! ")
    print("\nIn this game, player will choose a number from 1-4.")
    print("\nThe player will then choose a color from the list of colors presented")
    print("\nFinally, you will choose an animal, from the list of animals given.")
    print("\nOnce your choices have been made, you will receive a joke, quote, or trivia that coorelates with your choices.")
    print("\nENJOY!")


def playersName():
    name = input("\nFirst, what's your name? ")
    print("\nHi,", name + "!")
    return name


def colors(x):
    while True:
        if x == 1:
            print(""" \n"Singing" one is the lonliest number...""")
            color = input(
                "\nNow, choose one of the 3 colors! Blue, Red, or Green! --")
            colorList = ["Blue", "Red", "Green", "blue", "red", "green"]
            while True:
                if color.islower() not in colorList:
                    print("That's not in your color list!")
                    continue
                else:
                    animals(color)
                    break

        elif x == 2:
            print("\nTwo is probably the best number right?")
            color = input(
                "\nNow, choose one of the 3 colors! White, Purple, or Orange! --")
            colorList = ["White", "Purple", "Orange",
                         "white", "purple", "orange"]
            if color.islower() not in colorList:
                print("\nThat's not in your color list!")
                continue
            else:
                animals(color)
                break
        elif x == 3:
            print("\nThree is probably the best number right?")
            color = input(
                "\nNow, choose one of the 3 colors! Brown, Silver, or Green! --")
            colorList = ["Brown", "Silver",
                         "Green", "brown", "silver", "green"]
            if color not in colorList:
                print("That's not in your color list!")
                continue
            else:
                animals(color)
                break

        elif x == 4:
            print("\nFour is probably the best number right?")
            color = input(
                "\nNow, choose one of the 3 colors! Violet, Gold, Pink! --")
            colorList = ["Violet", "Gold", "Pink", "violet", "gold", "pink"]
            if color in colorList:
                animals(color)
                break
        else:
            print("\nThat's not in your color list!")
            continue


def animals(color):
    while True:
        if color == "Blue" or color == "Silver" or color == "blue" or color == "silver":
            lastRound = input(
                "\nOk, last round! Choose one of these three animals! Cow, Lizard, Whale: ")
            lastList = ["Cow", "Lizard", "Whale", "cow", "lizard", "whale"]
            if lastRound not in lastList:
                print("\nThat animal isn't in your list!")
                continue
            else:
                lastStep(lastRound)

        elif color == "Brown" or color == "Green" or color == "brown" or color == "green":
            lastRound = input(
                "\nOk, last round! Choose one of these three animals! Giraffe, Lion, Snake: ")
            lastList = ["Giraffe", "Lion", "Snake", "giraffe", "lion", "snake"]
            if lastRound.islower() not in lastList:
                print("\nThat animal isn't in your list!")
                continue
            else:
                lastStep(lastRound)

        elif color == "Pink" or color == "White" or color == "pink" or color == "white":
            lastRound = input(
                "\nOk, last round! Choose one of these three animals! Tiger, Kangaroo, Mouse: ")
            lastList = ["Tiger", "Mouse",
                        "Kangaroo" or "tiger", "mouse", "kangaroo"]
            if lastRound not in lastList:
                print("\nThat animal isn't in your list!")
                continue
            else:
                lastStep(lastRound)

        elif color == "Red" or color == "Gold" or color == "red" or color == "gold":
            lastRound = input(
                "\nOk, last round! Choose one of these three animals! Elephant, Horse, Bat: ")
            lastList = ["Elephant", "Horse",
                        "Bat" or "elephant", "horse", "bat"]
            if lastRound.islower() not in lastList:
                print("\nThat animal isn't in your list!")
                continue
            else:
                lastStep(lastRound)

        elif color == "Violet" or color == "Orange" or color == "violet" or color == "orange":
            lastRound = input(
                "\nOk, last round! Choose one of these three animals! Kitten, Salamander, Eagle: ")
            lastList = ["Kitten", "Salamander", "Eagle", "kitten", "salamander", "eagle"]
            if lastRound.islower() not in lastList:
                print("\nThat animal isn't in your list!")
                continue
            else:
                lastStep(lastRound)

        return lastRound


def lastStep(lastRound):
    if lastRound == "Kitten" or lastRound == "Eagle" or lastRound == "kitten" or lastRound == "eagle":
        print("""\nI asked my dog "What's two minus two?" He said nothing""")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Bat" or lastRound == "Giraffe" or lastRound == "bat" or lastRound == "giraffe":
        print("\nDid you know that bats are the only mammals that can fly?")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Elephant" or lastRound == "Snake" or lastRound == "elephant" or lastRound == "snake":
        print("""\n"Never be limited by other people's limited imaginations." - Dr. Mae Jemison""")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Cow" or lastRound == "Mouse" or lastRound == "cow" or lastRound == "mouse":
        print("""\n"Hold fast to dreams, for if dreams die, life is a broken winged bird that cannon fly." - Langston Hughes""")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Salamander" or lastRound == "Tiger" or lastRound == "salamander" or lastRound == "tiger":
        print("""\nWhat did the hat say to the other hat?..."Stay here! I'm going on ahead!" """)
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Horse" or lastRound == "Lizard" or lastRound == "horse" or lastRound == "lizard":
        print("\nThe average person dreams four to six times per night")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Lion" or lastRound == "Kangaroo" or lastRound == "lion" or lastRound == "kangaroo":
        print("\nWhat country's capital is growing the fastest?...Ireland. Every day it's Dublin.")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()
    elif lastRound == "Whale" or lastRound == "whale":
        print("\nIf you spent one night in each hotel in Disney World, it would take you 68 years to sleep in all of them!")
        again = input("\nWould you like to play again? Y/N: ")
        if again == "Y" or again == "y":
            main()
        else:
            quit()


def main():
    welcome_message()
    playersName()

    while True:
        play1 = input("\nWould you like to play a game? Y/N: ")
        if play1 == "Y" or play1 == "y":
            break
        elif play1 != "Y" and play1 and "y" and play1 != "N" and play1 != "n":
            print("\nPlease enter Y to play or N to end the game. ")
            continue
        else:
            print("\nOk. Goodbye!")
            quit()

    while True:
        userNum = int(input("\nPlease enter a number from 1-4: "))
        if userNum == 1:
            print("\nYou have chosen the number 1. Now, let's move on to the next round.")
            colors(1)
            break
        elif userNum == 2:
            print("\nYou have chosen the number 2. Now, let's move on to the next round.")
            colors(2)
            break
        elif userNum == 3:
            print("\nYou have chosen the number 3. Now, let's move on to the next round.")
            colors(3)
            break
        elif userNum == 4:
            print("\nYou have chosen the number 4. Now, let's move on to the next round.")
            colors(4)
            break
        else:
            userNum = input(
                "\nInvalid number. Please enter a number between 1-4 or Q to quit: ")
            if userNum == "Q" or userNum == "q":
                print("\nYou have ended the game.")
                quit()
            else:
                continue


main()
