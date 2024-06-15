import random

word_list = ['python', 'javascript','chicken','dustbin', 'swift', 'programming', 'hangman']

hangman_stages = [
    # Final state: head, torso, both arms, and both legs
    """
     ------
     |    |
     |    O
     |   \\|/
     |    |
     |   / \\
    -+-
    """,
    # Head, torso, both arms, and one leg
    """
     ------
     |    |
     |    O
     |   \\|/
     |    |
     |   / 
    -+-
    """,
    # Head, torso, and both arms
    """
     ------
     |    |
     |    O
     |   \\|/
     |    |
     |    
    -+-
    """,
    # Head, torso, and one arm
    """
     ------
     |    |
     |    O
     |   \\|
     |    |
     |    
    -+-
    """,
    # Head and torso
    """
     ------
     |    |
     |    O
     |    |
     |    |
     |    
    -+-
    """,
    # Head
    """
     ------
     |    |
     |    O
     |    
     |    
     |    
    -+-
    """,
    # Initial empty state
    """
     ------
     |    |
     |    
     |    
     |    
     |    
    -+-
    """
]

def get_random_word():
    return random.choice(word_list)

def display_game_state(word, guessed_letters, attempts_left):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(hangman_stages[attempts_left])
    
    print(f"\nWord: {display_word}")
    print(f"Guessed Letters: {' '.join(guessed_letters)}")
    print(f"Attempts Left: {attempts_left}")

def play_game():
    word = get_random_word()
    guessed_letters = set()
    attempts_left = 6  
    
    while attempts_left > 0:
        display_game_state(word, guessed_letters, attempts_left)
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Correct!")
            if set(word).issubset(guessed_letters):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            print("Incorrect!")
            attempts_left -= 1
        
        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The word was: {word}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()

play_game()