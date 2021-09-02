def recursive_function(num):
    if num == 1:
        return num
    else:
        return num * recursive_function(num - 1) # First Part: 1 step: 5 * recursive_function(5-1), 2 step: 4 * recursive_function(4-1)
    #3 step: 3 * recursive_function(3-1). step4: 2 * recursive_function(2-1). step5: 1, return num =1
    # Second part: step 5 will return 1, you go backwards to step #4 2*1=2, step3 3*2=6, step2:4*6=24, step1:5*24
#the number is 5
#5! = 5*4*3*2*1 = 120

number = int((input("Enter your number: ")))
if number < 0:
    print("This is a negative number. It won't work")
elif number == 0:
    print("The factorial of zero is one")
else:
    print("Your factorial of {} is {} ".format(number, recursive_function(number)))
