
def elements(numbers): #numbers will present a lщt of numbers
    Odd = 0
    Even = 0
    for number in numbers:
        if number % 2 == 0: #if it's dividable by 2, it means the # is even.
            Even += 1
        else:
            Odd += 1
    if Odd < Even:
        print("There are more Even numbers than Odd ones")
    elif Even < Odd:
        print("There are more Odd numbers than Even ones")
    else:
        print("You are on a different planet")

elements([1, 2, 3, 4, 5, 6, 7, 10, 14, 15, 18, 20, 25, 37, 45, 28])



