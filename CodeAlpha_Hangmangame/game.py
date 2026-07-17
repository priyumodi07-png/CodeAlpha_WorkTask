import random
words = ["python", "hangman", "program", "random", "string"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []
print("Welcome to Hangman!")
print("Word to guess:", " ".join(guessed))
while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    used_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over! The word was:", word)
