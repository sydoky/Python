# my_dict = {'name': 'Alex',
#            'age': 25,
#            'weight': 80,
#            'height': 175,
#            'occupation': 'Driver'
#            }
# print(my_dict['height'])
#
# my_dict['last_name'] = 'Brown'
# print(my_dict)
#
# del my_dict['height']
# print(my_dict)
#
# my_dict.clear()
# print(my_dict)
#
# print(my_dict['height'])


my_dict = {'apple': 'apple is a good choice',
           'peach': 'peach is a good choice',
           'watermelon': 'watermelon is a good choice',
           'orange': 'orange is a good choice',
           'banana': 'banana is a good choice'
           }

# print(my_dict)

# while True:
#     dictionary = input('Please enter your favorite fruit: ')
#
#     if dictionary == 'quit':
#         print("The game is over")
#
#     my_favorite = my_dict.get(dictionary, "This is not your favorite fruit" + dictionary)
#     print(my_favorite)
#     break

for i in range(10):
    for snacking in my_dict:
        print(snacking + 'is ' + my_dict[snacking])

