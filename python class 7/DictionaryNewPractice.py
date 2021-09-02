# fruits = {'apple': 'apple is healthy',
#           'banana': 'banana is tasty',
#           'pineapple': 'pineapple is to acidic'
# }
# print(fruits)
# #
# # fruits['orange']= 'orange has a lot of vitamin C'
# # print(fruits)
# #
# # fruits.update({'coconut': 'Coconuts grow in tropical climate'})
# # print(fruits)
#
# cars = {'BMW': 'BMW is very fast',
#         'Volvo': 'Volvo is safe',
#         'Mercedes': 'Mercedes is classy'
# }
#
# fruits.update(cars)
# print(fruits) #update method. This method I cannot use it because it does not store any variable.
#
#
# locations = {}
# for i in (fruits, cars):
#     locations.update(i)
# print(locations) #iterating and using update method. This method I can use in anywhere because it stores in a variable

#check a key exists in my dictionary or not

# print(fruits['BMW'])
#
#
#
# checking = input("Please enter your key: ")
#
# if checking.upper() in fruits:
#     print("This key {} is presented in your dictionary".format(checking))
# else:
#     print("This key is not presented in your dictionary")

#
# cars = {'BMW': 'BMW is very fast',
#         'Volvo': 'Volvo is safe',
#         'Mercedes': 'Mercedes is classy'
# }
#
# my_cars = tuple(cars)
# print(my_cars)
#
# my_cars2 = tuple(cars.items())
# print(my_cars2)
#
# for i in my_cars2:
#     key, values = i
#     print(key, values)

# food_price_in_usd = {'meet': 30,
#                      'apples': 5,
#                      'popcorn': 6,
#                      'chips': 3}
# # counter = 0
# # for i in food_price_in_usd.values(): #in order to get all the values, I need to target each key for that reason I use .values
# #     counter += i
# # print(counter)
#
# if 'popcorn' in food_price_in_usd:
#     del food_price_in_usd['popcorn']
# print(food_price_in_usd)



# 1: 1
# 2: 4
# 3: 9
# 4: 16

num = int(input("Please enter your number: "))

square_dict = {}
# square_dict = dict() - we can also do this way

for i in range(1, num+1): #1 is the starting and num+1 for ending point
    square_dict[i] = i*i
print(square_dict)













