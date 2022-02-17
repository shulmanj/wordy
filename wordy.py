import random
"""
    Wordle knock-off
    
    Jacob Shulman
    February, 2022
"""

def main():
    print("Welcome to Wordy. You have 6 tries to guess a random 5 letter word.")
    words = []
    with open('5letterwords.txt') as f:
        words = f.readlines()
    randomNumber = random.randrange(0, 5786)
    word = str(words[randomNumber].strip())
    
    playGame(word)

def playGame(word):
    # 🟨    🟩   ⬛️
    for i in range(6):
        guess = str(input())

        while len(guess) != 5:
            print("Please enter a 5 letter word:")
            guess = str(input())

        for j in range(5):
            if guess[j] == word[j]:
                print("🟩", end= "")
            elif guess[j] in word:
                print("🟨", end = "")
            else:
                print("⬛️", end = "")
        print()
        if guess == str(word):
            print("Good job! The word was", word)
            return
    if guess != word:
        print("Unlucky. The word was", word)



if __name__ == "__main__":
    main()