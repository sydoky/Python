#Map
location={0:"You are sitting infront of a computer learning python. The game is over!",
          1:"You are standing at the Road",
          2:"You are at the Top of a HIll",
          3:"You are inside a Building",
          4:"You are in the valley Beside a stream",
          5:"You are in the Forest"}

exit=[{"Q":0}, #exit is basically a list
      {"W":2,"E":3,"N":5,"S":4,"Q":0}, #items are individual dictionary
      {"N":5,"Q":0},
      {"W":1,"Q":0},
      {"N":1,"W":2,"Q":0},
      {"W":2,"S":1,"Q":0}]

loc=1 # we start from 1 which is 1:"You are standing at the Road
while True:                         #we put it loc because we want to start from 1, line 10
     available_exits=", ".join(exit[loc].keys()) #", " is separate the string by a comma, which I can see in output. # join is to convert a list into a string.
     #.join will convert list into a string. #exit is a list now, loc will help to get the key (W,E,N,S,Q), #keys to pick up the keys

     print(location[loc]) #our lock is only one and we start from line 3 "You are standing at the Road"

     if loc==0:
         break #it's quit
     direction=input("Available exits are " +available_exits+" :").upper() #upper will convert into upper case

     print() #for space

     if direction in exit[loc]: #if direction you make in W, E, N, S, Q Here I provide and next line will update the location
         loc=exit[loc][direction] #this line will update the location
     else:
         print("You can't go there")
