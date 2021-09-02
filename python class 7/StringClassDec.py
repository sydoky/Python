import random

class String:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word

    def count_letters(self):
        characters = {}
        for charact in self.word:
            if charact in characters:
                characters[charact] += 1
            else:
                characters[charact] = 1  # set 1 cause it is first time appears in the dictionary
        return characters

    def frequency(self):
        character_counter = self.count_letters()
        maxx = None
        characterr = None
        for charact in character_counter:
            if maxx is None:
                maxx = character_counter[charact]
                characterr = charact
            else:
                if character_counter[charact] > maxx:
                    maxx = character_counter[charact]
                    characterr = charact
        return characterr, maxx

    def show_vowels_we_have(self):
        vowels = "aeiouAEIOU"
        vowel_counter = {}
        character_counter = self.count_letters()
        for charact in character_counter.items():
            if charact[0] in vowels:  # [0] becomes a tuple
                vowel_counter[charact[0]] = charact[1]
        return vowel_counter

    def count_vowels(self):
        vowels = "aeiou"
        vowel_counter = 0
        for charact in self.word:
            if charact.lower() in vowels:
                vowel_counter += 1
        return vowel_counter

    def upper_lower_case_counter(self):
        characterss = 0
        uppercharacter = 0
        for charact in self.word:
            if charact.islower():
                characterss += 1
            elif charact.isupper():
                uppercharacter += 1

        return characterss, uppercharacter  # by adding a comma (,) I make a tuple

    def longest_word(self):
        words = self.word.split()
        maxxx = None
        max_word = None
        for word in words:
            if maxxx is None:
                maxxx = len(word)
                max_word = word
            else:
                if maxxx < len(word):
                    maxxx = len(word)
                    max_word = word
        return maxxx, max_word

    def reverse_word(self):
        empty_string = ""
        for i in range(len(self.word)-1, -1, -1):
            empty_string += self.word[i]  # to add to the end of the string always use +=
        return empty_string

    # [-1] - last character of self.word,   #range(len(self.word), -1)
    # -1 - last character of self.word united states of america from last charact., -1(2) is going to from last to first letter
    # -1(3) is for negative step, so you go backwards

    def is_palindrome(self):
        return self.reverse_word() == self.word

    def has_a_character(self, letter):
        for characte in self.word:
            if characte == letter:
                return True
        return False

    def hangman(self):
        word = ["manzana", "banana", "uvas", "sandia", "gotas de miel", "fresas", "cerezas", "papaya", "naranja", "mandarina"]
        secret_word = word[random.randint(0, len(word)-1)]
        guess = "_" * len(secret_word)  # we create this line so we have the same quantity of _s as our secret word
        shots = 3
        while shots > 0:
            for l in range(len(secret_word)):
                print(guess[l], end=" ")
            print()
            letter = input("elige una letra: ")
            if len(letter) > 1:
                print("Error404. elige solo una letra")
                continue
            if not letter.isalpha():
                print("Por favor, elige una letra")
                continue
            if letter in secret_word:
                print("buena suposición")
                for l in range(len(secret_word)):
                    if secret_word[l] == letter:
                        guess = guess[:l] + letter + guess[l + 1:]
                if secret_word == guess:
                    print("Eres un ganador, babe!")
                    break
                for l in range(len(secret_word)):
                    print(guess[l], end=" ")
                print()
                guess_word = input("Adivina la palabra, chico/a ")
                if guess_word == secret_word:
                    print("Muy bien, chico/a ")
                    break
                else:
                    print("Coño!")
            else:
                print("Error")
                shots -= 1
                print(shots, " de tres tentativas restantes")
                if shots == 0:
                    print("Coño!")


unfortunately = String("unfortunately")
print(unfortunately.count_letters())

united_states_of_america = String("United States of America")
print(united_states_of_america.frequency())

print(united_states_of_america.count_vowels())

print(united_states_of_america.show_vowels_we_have())
print(united_states_of_america.upper_lower_case_counter())
print(united_states_of_america.longest_word())

print(united_states_of_america.reverse_word())
print(united_states_of_america.is_palindrome())
radar = String("radar")
print(radar.is_palindrome())
print(united_states_of_america.has_a_character("z"))
print(united_states_of_america.hangman())