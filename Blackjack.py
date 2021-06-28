import random
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def deck_gen():
    deck = []
    cards = 0
    i = 0
    
    suit_list = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for suit_name in suit_list:

        cards = card_gen(suit_name)
        deck += cards

    return deck

def card_gen(suit):
    deck = []
    value = 0
    i = 0

    for i in range(13):
        card = []

        if i == 0:
            rank = "Ace"
            value = 1

        elif i == 10:
            rank = "Jack"
            value = 10
            
        elif i == 11:
            rank = "Queen"
            value = 10
            
        elif i == 12:
            rank = "King"
            value = 10
        else:
            rank = str(i + 1)
            value = i + 1

        card.append(suit)
        card.append(rank)
        card.append(value)
        
        deck.append(card)
        
        i += 1
    return deck

def draw_card(deck):
    
    card = random.choice(deck)
    deck.remove(card)
    return card

def main():
    display_title()

    money = db.load_money()
    deck = deck_gen()
    choice = "y"

    while choice.lower() == "y":
        print("Money: " +str(money))
        bet = input("bet: ")
        card = draw_card(deck)

        print(str(deck[0][1])+ " of " +str(deck[0][0]))
        

        choice = input("Play again? (y/n): ")

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()