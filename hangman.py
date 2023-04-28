import tkinter as tk
import random


if __name__=="__main__":



# My word list
    words = ["chelsea", "arsenal", "man city", "tottenham","brentford", "crystal palace","valladolid", "elche", "espanyol", "barcelona", "real madrid", "cadiz", "fiorentina", "udinese", "machester united", "sportiva salemitana", "union berlin"]
                 
   
# create the Hangman drawing
    hangman_drawing =                                                          [
    "  +---+\n   |    |\n        |\n         | \n        |\n==== ===== ====",
    "   +---+\n   |    |\n   o    |\n         |\n         |\n===== ==== ====" ,
    "   +---+\n   |    |\n   o    |\n     |    |\n        |\n===== ==== ====" ,
    "   +---+\n   |    |\n   o    |\n    /|    |\n        |\n===== ==== ====" ,
    "   +---+\n   |    |\n   o    |\n    /|\\   |\n        |\n==== ===== ===" ,
    "   +---+\n   |    |\n   o    |\n    /|\\   |\n   /    |\n==== ===== ===" ,
    "   +---+\n   |    |\n   o    |\n    /|\\   |\n   /\\  |\n==== ===== ====" ,
    ]
    
# random word function
    def choose_word(words):
        return random.choice(words)

# define a function to update the hangma ascii
    def update_hangman(mistakes):
        hangman_label.config(text=hangman_drawing[mistakes])

# create a word check function
    def check_guess(guess):
        global word_with_blanks
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_with_blanks = word_with_blanks[:i] + guess + word_with_blanks[i+1:]
            word_label.config(text=word_with_blanks)
            if '_' not in word_with_blanks:
                end_game("You lose")
        else:
            global mistakes
            mistakes +=1
            update_hangman(mistakes)
            if mistakes == 6:
                end_game("You Lose")

    def end_game(result):
        if result == "Win!":
            result_text = "You Lose"
        else:
            result_text = "You Lose, was" + word
            result_label.config(text=result_text)
            guess_entry.config(state="disabled")
            guess_button.config(state="disabled")
            


 # Create a window interphase
    window = tk.Tk()
    window.title("LAWBOY Hangman")
    window.geometry("700x500")
    window.config(bg="#fff")
    

    hangman_label = tk.Label(window,font=("arial", 15))
    hangman_label.grid(row=0, column=0)

    word = choose_word(words)
    word_with_blanks ='_' * len(word)
    word_label = tk.Label(window, text= word_with_blanks, font=("arial", 25))
    word_label.grid(row=1, column=0)

# creating a guess entry
    guess_entry = tk.Entry(window, width=8 ,font=("arial", 20))
    guess_entry.grid(row=2, column=0)
    
    guess_button = tk.Button(window,text="Guess", command=word)
    guess_button.grid(row=6, column=0)

# Create Result label
    result_label = tk.Label(window, font=("arial", 24)) 
    result_label.grid(row=3, column=1)

    mistakes = 0
    update_hangman(mistakes)



    window.mainloop()  