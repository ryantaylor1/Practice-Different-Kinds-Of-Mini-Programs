print("Hello I am the Joke machine, the machine that will make you laugh your guts off")
print("Here is your score:")
score=0
print("Alright first joke:\nWhat is pink and fluffy?")
answer=input().lower()
if answer == "pink fluff":
    print("Wow, well done for getting it right")
    score=+1
else:
    print("WHAT!Where did you get that from?")
    score=-1
print("Next, what is brown and sticky?")
answer2=input().lower()
if answer2 == "a stick":
    print("Way to go!")
    score=+1
else:
    print("Sorry, no")
    score=-1
print("And finally for the last question, What is black and white and red all over?")
answer3=input().lower()
if answer3 == "a newspaper":
    print("Good Job!")
    score=+1
else:
    print("Nowhere near getting it right")
    score=-1
print("Your final score:", score,"\nWell done!")
