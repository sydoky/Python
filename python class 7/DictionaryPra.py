#Map
location={0:"You are sitting infront of a computer learning python. The game is over!",
          1:"You are standing at the Road",
          2:"You are at the Top of a HIll",
          3:"You are inside a Building",
          4:"You are in the valley Beside a stream",
          5:"You are in the Forest"}

exit= [{"Q":0},
      {"W":2,"E":3,"N":5,"S":4,"Q":0},
      {"N":5,"Q":0},
      {"W":1,"Q":0},
      {"N":1,"W":2,"Q":0},
      {"W":2,"S":1,"Q":0}]


full_exit = {"QUIT": "Q",
             "NORTH": "N",
             "SOUTH": "S",
             "EAST": "E",
             "WEST": "W"}

# {0:{"Q":0},
#       1:{"W":2,"E":3,"N":5,"S":4,"Q":0},
#       2:{"N":5,"Q":0},    #this is my another way to make function work converting list into dictionary
#       3:{"W":1,"Q":0},
#       4:{"N":1,"W":2,"Q":0},
#       5:{"W":2,"S":1,"Q":0}}

loc=1 #
while True:
     available_exits=", ".join(exit[loc].keys())

     print(location[loc])

     if loc==0:
         break #it's quit
     direction=input("Available exits are " +available_exits+" :").upper()

     if len(direction)>1:
         for word in full_exit:
             if word in direction:
                 direction = full_exit[word]

     print()

     if direction in exit[loc]:
         loc=exit[loc][direction]
     else:
         print("You can't go there")