def letter_counting(word, character):
    counter = 0
    for letter in word:
        if letter == character:
            counter += 1
    print("counter", counter)

letter_counting("banana", "n")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list[3])


print("---------------------")

data=[4,5,6,104,110,120,135,145,155,165,175,185,195,350,380]

min_valid=100
max_valid=200

# print(len(data)-1)  #-1 is because

for i in range(len(data)-1, -1, -1):
    print(data[i])

for i in range(14, -1, -1):
        print(data[i])

