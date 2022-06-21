#Quiz by SoftyDuck
from curses import color_content
import time
#Variables
score = 0
correct = "You are correct! 1 point has been added!"

print("Score: " + str(score))
print("Welcome to Game Quiz!")
time.sleep(3)
print("Lets begin!")
time.sleep(2)

#Question One
print("Question 1:")
print("Which game is the best game?")
print("A: Minecraft")
print("B = Among us")
print("C is fortnite")
question_1 = input("Choose one from above (A, B or C): ")

if question_1== "B":
    print(correct)
    score = score + 1
else:
    print("You got the question wrong. The correct answer as B. 1 Point removed")
    score = score - 1
time.sleep(3)

#Question 2
print("Question 2:")
print("Which best describes Among Us?")
time.sleep(2)
print("A: an game where you have to find the imposter. You can compelete tasks. You turn into a ghost when you get killed. If your an imposter, you have to kill everyone.")
print("B: a happy game where everyone has fun!")
print("C: a shooter game.")
question_2 = input("Choose one from above (A, B or C): ")

if question_2== "A":
    print(correct)
    score = score + 1
else:
    print("You got the question wrong. The correct answer was A. 1 Point removed.")
    score = score - 1
time.sleep(3)

#Question 3
print("Question 3:")
print("What is Minecraft?")
time.sleep(3)
print("A: a shooter game where you can shoot anything")
print("B: a battle royal game simular to Fortnite")
print("C: a simple sandbox game where you can build what you want!")
question_3 = input("Choose one from above (A, B or C): ")

if question_3== "C":
    print(correct)
    score = score + 1
else:
    print("You got the question wrong. The correct answer was A. 1 Point removed.")
    score = score - 1
time.sleep(3)

#Question 4
print("Question 4:")
print("is the imposter sus?")
time.sleep(2)
print("A: Yes")
print("B: No")
question_4 = input("Choose one from above (A or B): ")

if question_4== "A":
    print(correct)
    score = score + 1
else:
    print("You got it wrong :(, I'm taking 1 point")
    score = score - 1

#question 5
print("Question 5:")
print("Which best describes Fortnite?")
time.sleep(3)
print("A: a sandbox game")
print("B: a battle royal shooter game with building.")
print("C: a horror game")
question_5 = input("Choose one from above (A or B): ")

if question_5== "B":
    print(correct)
    score = score + 1
else:
    print("You got the question wrong! 1 point has been removed.")
    score = score -1

#Ending
print("Thank you for taking this quiz. You got the score of: " + str(score))
time.sleep(4)
print("Closing Quiz...")
time.sleep(2)
