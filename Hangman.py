import random

Word_Bank = ["Pain", "Ball", "Mine", "Nape","Cuff","Four","Asus","Valo","Yoru","Lock"]

attempt = []
# Chooses a random word from the list "Word_Bank"
# The asterisk splits the random word into multiple letters.
answer = [*random.choice(Word_Bank)]
# For every variable in "answer", it will replace it with a "_".
word = ["_" for i in answer]
print(word)
lives = 5

print(attempt)


while "_" in word and lives > 0:
    print(f"lives = {lives}")
    print(f"attempt = {' '.join(attempt)}")
    print(f"{' '.join(word)}")
    user = input("Please guess a letter: ").lower()
    # len function is used here to ensure the user only enters one character.
    if len(user) == 1 and user in [*string.ascii_lowercase]:
        attempt.append(user)
        # To change the world if guessed right.
        word = [i if i in attempt else "_" for i in answer]
    elif user in attempt:
        print("You guessed that already... Come on...")
    else:
        print("Nope. That's not how you play.")

    if lives > 0:
        print("You win!")
        print(f"The word is{' '.join(word)}")

    else:
        print("Nice try.")