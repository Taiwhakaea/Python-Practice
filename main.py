score = 0
play = "yes"

# Ask the user their name and save it
name = input ("ni hao")
# Greet the user and introduce the quiz
print ("ni hao man,", name)
print ("ching.")

# Ask the user a question
answer = input("smash or pass\n").upper()
if answer == "smash".upper():
    print ("sigma")
    score +=4 
elif answer == "":
    print ("stupid")
else:
    print ("incorrect stupid")
print ("ANSWER IS SMASH")
# End the quiz
print ("well done ni hao", score, "points")

