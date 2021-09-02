'''
#list
cards = ["cards[52]", '♣', '♦', '♥', '♠', "J", "Q", "K", "player1", "player2"]

cards.insert(8, "A")
cards.append("deck")
print(cards)
print(len(cards))

print(cards[0:2])

print("---------")

cards = ["cards[52]", '♣', '♦', '♥', '♠', "J", "Q", "K", "player1", "player2"]

for items in cards:
    print(cards)

print("---------")



card = {
    "deck": "cards"
}
print(card["deck"])

print("--------")

#tuple
tuple = ("cards[52]", '♣', '♦', '♥', '♠', "J", "Q", "K", "player1", "player2")

tuple2 = tuple

print(tuple)
print(tuple2)

print("--------------------")


#sets

sets = {"cards[52]", '♣', '♦', '♥', '♠', "J", "Q", "K", "player1", "player2"}

print(sets)


print("--------")

card_game = {
    "cards": "cards",
    "deck": "deck",
    "signs": ['♣', '♦', '♥', '♠'],
    "player1": "player1",
    "player2": "player2"

}

for items in card_game:
    print(items)


card_game["hack cards"] = "♣A"
print(card_game)

print(card_game["cards"])

print(card_game.get("signs"))

print(card_game.get("hack cards"))

print(len(card_game))

print(card_game.keys())

print(card_game.values())

print(card_game.items())


print("--------")

#strings

strings = "cards[52]", '♣', '♦', '♥', '♠', "J", "Q", "K", "player1", "player2"

print(strings)


#how to store cards, players, everyting what we have in our class game, how I am going to orginize that
'''

symbols = ("😊" "🥺" 😉 😍 😘 😚 😜 😂 😝 😳 😁 😣 😢 😊 )💯 ⛔

match = (person1, person2, person3, person4, person 5)

draw_pile = []

player1 = {
    "nick_name": "Battle",
    "money": 50.00,
    "currency": "$"
}

