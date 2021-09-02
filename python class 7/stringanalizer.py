class String_Analizer:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def count_character(self, char):
        counter = 0
        for character in self.string:
            if character == char:
                counter = counter + 1
        return counter
    def len(self):
        counting_letters = 0
        for _ in self.string:
            counting_letters = counting_letters + 1
        return counting_letters
    '''def upper(self):
        smaller_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        index = 0
        for character in self.string:
            if character in smaller_case:
                result += upper_case[index]
            else:
                result += character
            index += 1
        return result'''
    def upper(self):
        smaller_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = "" #we use this because we copy the original inside the result but only a new copy will be in upper case
        for character in self.string:
            if character in smaller_case:
                index = 0 #we set index 0 which is the index of smaller case a in smaller case list
                for c in smaller_case:
                    if c == character:
                        result += upper_case[index]
                    index += 1
            else:
                result += character
        return result

    def lower(self):
        smaller_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""  # we use this because we copy the original inside the result but only a new copy will be in upper case
        for character in self.string:
            if character in upper_case:
                index = 0  # we set index 0 which is the index of smaller case a in smaller case list
                for c in upper_case:
                    if c == character:
                        result += smaller_case[index]
                    index += 1
            else:
                result += character
        return result

    def index(self, string): #string = "s" or other any letter in print section below when we call the index method
        index = 0
        for c in self.string:
            if c == string: #this line means I found what I am searching for
                return index
            index += 1

    def replace_cha(self, original, new):
        index = 0
        new_string = ""
        for w in self.string:
            if w == original:
                 new_string += new
            else:
                new_string += self.string[index]  # index is the original character
            index += 1
        return new_string

    def is_there_upper(self, capital):
        #index = 0 we don't need index because we don't change anything here
        for l in self.string:
            if l == capital.upper():
                return True
        return False
    def are_there_vowels(self):
        vowels = "aeiouAEIOU"
        for v in self.string:
            if v in vowels:
                return True
        return False
    def all_vowels(self):
        A = False
        E = False
        I = False
        O = False
        U = False
        for v in self.string:
            if v in "Aa":
                A = True
            if v in "Ee":
                E = True
            if v in "Ii":
                I = True
            if v in "Oo":
                O = True
            if v in "Uu":
                U = True
        if A and E and I and O and U:
            return True
        return False
    def no_vowels(self):
        vowels = "aeiouAEIOU"
        for v in self.string:
            if v in vowels:
                return False
        return True
    def cool_no_vowels(self):
        return not self.are_there_vowels()




print("hello world".replace("w", "g"))

print("hello".count("l"))
word = String_Analizer("deep")
print(word.count_character("e"))
word2 = String_Analizer("United States of America")
word3 = String_Analizer("HO HO HO")
word5 = String_Analizer("try")
print(word2.count_character("e"))
print(word2.len())
print(word2.upper())
print(str(word2).upper())
print(word2.upper())
print(word2.lower())
print(word2.string.index("s"))
print(word2.index("S"))
print(word2.index("x"))
print(word2.replace_cha("U", "V"))
print(word2.is_there_upper("i"))
print(word2.are_there_vowels())
print(word3.are_there_vowels())
print(word2.all_vowels())
print(word3.all_vowels())
print(word.all_vowels())
print(word5.no_vowels())
print(word2.no_vowels())
print(word5.cool_no_vowels())
print(word2.cool_no_vowels())