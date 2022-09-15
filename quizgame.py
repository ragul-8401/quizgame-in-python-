print("Welcome to Quiz Game")


Name = input("What is your name? ")
print("Okey" + " " + Name )
playing = input("Do you want to paly? ")

if playing != "yes":
    quit()

print("Okey! Let's play.")
score = 0


#question 1
answer = input("Who created 'Python'? ")
if answer == "Guido van Rossum":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
   

#question 2

answer = input("Who created JavaScript? ")
if answer == "Brendan Eich":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
   

#question 3

answer = input("Who created HTML? ")
if answer == "Tim Berners-Lee":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
 
print("Your Score is" + " " + str(score))

