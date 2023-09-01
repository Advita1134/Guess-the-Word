

import numpy as np

tries = 10
word_choices = np.array(["desk", "pen", "pencil", "marker"])
word = np.random.choice(word_choices)
total_letters = 0
correct_letters = "_" * len(word)

print("The length of the word you're guessing is", len(word))

while True:
    guess = input("Type a letter that you thinks is in the word. ")

    
    if (guess in word) == True:
        place = word.find(guess)
        place2 = place + 1
        print( f"This letter is in your word. It is the {place2} st/nd/rd place" )
        total_letters = total_letters + 1
        correct_letters = correct_letters[:place] + guess + correct_letters[place2:]
        print(correct_letters)
        
    elif (guess in word) == False:
        tries = tries - 1
        print("This letter is incorrect. Try again. You have", tries, "tries")
        print(correct_letters)
        
        if tries == 0:
            print("You ran out of tries. You lost.")
            break
    
    if total_letters == len(word):
        print("You won! Great job!")
        break

