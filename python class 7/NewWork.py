def function(egg, chicken, rooster):
    maximum = None
    if egg > chicken and chicken > rooster:
        maximum = egg
    elif rooster > chicken and chicken > egg:
        maximum = rooster
    else:
        maximum = chicken
    counter = 1

    while counter <= maximum:
        print("Hello")
        counter += 1

function(3, 5, 1)