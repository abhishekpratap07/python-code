import random

words = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini"
]
hangman_stages = [
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |
    |___
    """,  # 0 chances left – full hangman
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      /
    |
    |___
    """,  # 1 chance left
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |
    |
    |___
    """,  # 2 chances left
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |
    |
    |___
    """,  # 3 chances left
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |___
    """,  # 4 chances left
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |___
    """,  # 5 chances left
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    |___
    """,  # 6 chances left
]

lives = 6
choosen_words = random.choice(words)
print(choosen_words)

placeholder = ""
wordlength = len(choosen_words)
for positin in range(wordlength):
    placeholder += "_"
print("word guess by game"+placeholder)

game_over = False
correct_letter = []
while not game_over:
    
    guess = input("guess a word").lower()
    
    if guess in correct_letter:
        print(f"you aleready use this word{guess}")
    
    display = ""
    
    for letter in choosen_words:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display+="_"
    print("word to guess"+display)
    
    
    if guess not in choosen_words:
        lives -= 1
        print(f"your lives are left:{lives}")
        if lives == 0:
            game_over = True
            print("***************you lose *************************")
        if "_" not in display:
            game_over = True
            print("***********you win****************************")
    print(hangman_stages[lives]) 
        
        