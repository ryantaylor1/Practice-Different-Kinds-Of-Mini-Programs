from random import randint

words = ["deliberate", "obligated", "highlight", "infrastructure", "extermination", "strange", "elevator", "extravagant", "melancholy", "processed"]
word = words[randint(0,len(words)-1)]
 
answer = [" _ "] * len(word)
new_answer = ""
wrong_answer = 10
print(answer)


while wrong_answer != 0:
    guess = input("Enter a character: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                answer[i] = guess
                for character in answer:
                    new_answer += character + ""
    else:
        wrong_answer-=1
        print("Incorrect guess")
        print(f"You have {wrong_answer} attempts left")
    print(answer)
    
    if " _ " not in answer:
        print(f"Well Done! You have successfully guessed the word {word}")
        break
    elif wrong_answer == 0:
        print(f"So close! The word was {word}")
