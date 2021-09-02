import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + self.suit


class Deck:
    def __init__(self):
        self.cards = []
        self.create()
        self.shuffle()


    def create(self):
        for suit in ['♣', '♦', '♥', '♠']:
            for value in range(1, 14):
                if value not in [1, 11, 12, 13]:
                    self.cards.append(Card(suit, value))
                elif value == 1:
                    self.cards.append(Card(suit, "A"))
                elif value == 11:
                    self.cards.append(Card(suit, "J"))
                elif value == 12:
                    self.cards.append(Card(suit, "Q"))
                elif value == 13:
                    self.cards.append(Card(suit, "K"))
    def shuffle(self):
        counter = 0
        while counter < len(self.cards):
            random_card_index = random.randint(counter, len(self.cards)-1)  # The randint() method returns an integer number selected element from the specified range
            temp_card = self.cards[counter]
            self.cards[counter] = self.cards[random_card_index]
            self.cards[random_card_index] = temp_card
            counter += 1

    def draw(self):
        random_card_index = random.randint(0, len(self.cards)-1)
        return self.cards.pop(random_card_index)

    def __str__(self): # to print the entire deck of cards
        deck = ""
        for card in self.cards:
            deck += str(card) + ", "
        deck = deck[:-2]
        deck = str(len(self.cards)) + " cards: " + deck
        return deck

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return "name " + self.name + ", money $" + str(self.money)

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        deck = Deck() # deck is a variable name, Deck reference to our class
        while True:
            print("--")
            card = deck.draw() #refering to 41 line
            print("card is :", card)
            bet1 = float(input("player 1" + str(self.player1) + ("Please, place your bet "))) #float makes a decimal point.
            choice1 = input("player 1" + str(self.player1) + ("Please, choose high or low "))
            bet2 = float(input("player 2" + str(self.player2) + ("Please, place your bet ")))
            choice2 = input("player 2" + str(self.player2) + ("Please, choose high or low "))
            if choice1.lower() in ["h", "high", "higher"]: #make our code more flexible input h, high, higher
                choice1 = "higher"
            if choice1.lower() in ["l", "low", "lower"]:
                choice1 = "lower"
            if choice2.lower() in ["h", "high", "higher"]:
                choice2 = "higher"
            if choice2.lower() in ["l", "low", "lower"]:
                choice2 = "lower"
            next_card = deck.draw()
            print("next card is :", next_card)
            card1_value = card.value
            if card1_value == "A":
                card1_value = 1
            if card1_value == "J":
                card1_value = 12
            if card1_value == "Q":
                card1_value = 13
            if card1_value == "K":
                card1_value = 14
            card2_value = next_card.value
            if card2_value == "A":
                card2_value = 1
            if card2_value == "J":
                card2_value = 12
            if card2_value == "Q":
                card2_value = 13
            if card2_value == "K":
                card2_value = 14
            result = "equal"
            if card2_value > card1_value:
                result = "higher"
            if card2_value < card1_value:
                result = "lower"
            if result == "equal":
                print("Both players lose")
            elif result == "higher":
                if choice1 == choice2 == "higher":
                    print("Both players win")
                elif choice1 == "higher":
                    print("Player1 wins")
                elif choice2 == "higher":
                    print("Player2 wins")
                else:
                    print("Both players lose")
            elif result == "lower":
                if choice1 == choice2 == "lower":
                    print("Both players win")
                elif choice1 == "lower":
                    print("Player1 wins")
                elif choice2 == "lower":
                    print("Player2 wins")
                else:
                    print("Both players lose")


player1 = Player("Mike", 300.00)
print(player1)
player2 = Player("Dusan", 1000.00)
print(player2)

'''deck1 = Deck()
print(deck1)
card1 = deck1.draw()
print(deck1)
print(card1)
'''

game = Game(player1, player2)
game.play()
