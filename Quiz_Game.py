print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? : ")

if playing.lower() != "yes":
    print(" :( I hope you would like to play in future.")
    quit()
else:
    print("Okay! Let's Play :) ")

score = 0

#1
answer = input("1. Who is the father of Computer?\nAnswer: ")
if answer.lower() == "charles babbage":
    print("correct answer!")
    score += 1
else:
    print("wrong answer!")

#2
answer = input("2. What does CPU Stand for?\nAnswer:")
if answer.lower() == "central processing unit":
    print("correct answer!")
    score += 1
else:
    print("wrong answer!")

#3
answer = input("3. What does GPU Stand for?\nAnswer:")
if answer.lower() == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("wrong answer!")

#4
answer = input("4. What does RAM Stand for?\nAnswer:")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1

else:
    print("wrong answer!")

#5
answer = input("5. What does 1 byte equals in bits?\nAnswer:").lower()
if answer == "8 bits" or "8bits":
    print("correct!")
    score += 1

else:
    print("wrong answer!")

print("Your Got "+ str(score)+" questions correct")
print("Your Got",round((score/5)*100,2),"%")