import random

words = ["python", "java", "recursion", "developer", "inheritance", "polymorphism"]

print("Welcome to Word Scramble Game!")
print("the words are related to computer languages")

while True:
    word = random.choice(words)
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled_word = "".join(scrambled)

    print("\nUnscramble this word:", scrambled_word)

    guess = input("Your guess: ").lower()

    if guess == word:
        print("Correct! Well done!")
    else:
        print("Wrong! The correct word was:", word)

    again = input("\nPlay again? (yes/no): ").lower()
    if again=="yes":
        print("\nAgain game Starts")
    elif again == "no":
        print("Thanks for playing!")
        break
    elif again!="no" and again!="yes":
        print("Invaild")
        break