

'''
n = int(input("Enter your favorite number: "))
for t in range(n):
    for r in range(1, n + 1):

        for s in range(n + 1 - r):
            print("*", end=" ")
        print()



    for r in range(1, n + 1):

        for s in range(r):
            print("*", end=" ")

        print()

n = int(input("Enter your favorite number: "))
t = 0
while t < n:
    t += 1
    for r in range(1, n + 1):

        for s in range(n + 1 - r):
            print("*", end=" ")
        print()



    for r in range(1, n + 1):

        for s in range(r):
            print("*", end=" ")

        print()
'''

#ask a user to input a target number and a number X. Loop from 0 to target number and count the number how many numbers are dividable by X

n = int(input("Please enter your favorite number: "))
x = int(input("Enter number X: "))
counter = 0
#loop from 0 to z
for numbers in range(1, n + 1):
    if numbers % x == 0:
        counter += 1
print(counter)

'''
def is_prime(n):
    #n = int(input("Enter your number: "))
    prime = True
    for num in range(2, n):
        if n % num == 0:
            prime = False
            break
    return prime
    if prime:
        print("Prime")
    else:
        print("Your number is not prime")

n = int(input("Let's find out prime numbers: "))
print("Your prime numbers are ")
for number in range(1, n):
    if is_prime(number):
        print(number, number ** 2, number ** 3, number ** 4, number ** 5)
#prime number
'''
'''
def is_prime(n):
    #n = int(input("Enter your number: "))
    prime = True
    for num in range(2, n):
        if n % num == 0:
            prime = False
            break
    return prime

counter = 0
for prime_num in range(100, 1000):
    if is_prime(prime_num):
        counter +=1
print(counter)
print(is_prime(143))'''


'''    if prime:
        print("Prime")
    else:
        print("Your number is not prime")'''
'''
n = int(input("Let's find out prime numbers: "))
print("Your prime numbers are ")

i = n + 1
while True:
    if is_prime(i):
        print(i)
        break
    i += 1

i = n - 1
while True:
    if is_prime(i):
        print(i)
        break
    i -= 1
'''



























