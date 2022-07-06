#Quiz by SoftyDuck
from curses import color_content
import time

# Variables
score = 0
correct = "You are correct! 1 point has been added!"

print("Score: " + str(score))
print("Welcome to Game Quiz!")
time.sleep(3)
print("Lets begin!")
time.sleep(2)

# Question One
print("""
Question 1:
Which game is the best game?

A: Minecraft
B: Among us
C: fortnite
""")
question_1 = input("Choose one from above (A, B or C): ")
if question_1 == "B" or "b":
    print(correct)
    score = score + 1
elif question_1=="A" or "a" or "B" or "b":
    print("You got the question wrong. The correct answer as B. 1 Point removed")
    score = score - 1
else:
    print("That is an invalid answer. The correct answer as B. 1 Point removed")
    score = score - 1
time.sleep(3)

# Question 2
print("Question 2:")
print("Which best describes Among Us?")
time.sleep(2)
print("""
Question 2:
Which best describes Among Us?
A: an game where you have to find the imposter. You can compelete tasks. You turn into a ghost when you get killed. If your an imposter, you have to kill everyone.
B: a happy game where everyone has fun!
C: a shooter game.
""")
print("C: a shooter game.")
question_2 = input("Choose one from above (A, B or C):")
if question_2 == "A" or "a":
    print(correct)
    score = score + 1
elif question_2=="B" or "b" or "C" or "c":
    print("You got the question wrong. The correct answer was A. 1 Point removed.")
    score = score - 1
else:
    print("Thats an invalid answer. The correct answer was A. 1 Point removed.")
    score = score - 1
time.sleep(3)

# Question 3
print("""
Question 3:
What is Minecraft?

A: a shooter game where you can shoot anything
B: a battle royal game simular to Fortnite
C: a simple sandbox game where you can build what you want!
""")
question_3 = input("Choose one from above (A, B or C): ")
if question_3 == "C" or "c":
    print(correct)
    score = score + 1
elif question_3=="A" or "a" or "B" or "b":
    print("You got the question wrong. The correct answer was A. 1 Point removed.")
    score = score - 1  
else:
    print("Thats an invalid answer. The correct answer was A. 1 Point removed.")
    score = score - 1
time.sleep(3)

# Question 4
print("""
Question 4:
is the imposter sus?

A: Yes
B: No
""")
question_4 = input("Choose one from above (A or B): ")
if question_4 == "A" or "a":
    print(correct)
    score = score + 1
elif question_4== "B" or "b" or "C" or "c":
        print("You got it wrong :(, I'm taking 1 point")
        score = score - 1
else:
    print("Thats an invalid answer, I'm taking 1 point")
    score = score - 1
time.sleep(3)

# question 5
print("""
Question 5:
Which best describes Fortnite?
A: a sandbox game
B: a battle royal shooter game with building.
c: a horror game.
""")
question_5 = input("Choose one from above (A or B): ")
if question_5 == "B" or "b":
    print(correct)
    score = score + 1
elif question_5== "A" or "a" or "C" or "c":
    print("You got the question wrong! 1 point has been removed.")
    score = score - 1  
else:
    print("Thats an Invalid answer. 1 point has been removed.")
    score = score - 1
# Ending

def congrats():
    print("Thank you for taking this quiz. You got the score of: " + str(score))

congrats()
time.sleep(4)
print("Closing Quiz...")
time.sleep(2)
