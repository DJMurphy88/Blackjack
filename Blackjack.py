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

        card.append(rank)
        card.append(suit)
        card.append(value)
        
        deck.append(card)
        
        i += 1
    return deck

def draw_card(deck):
    
    card = random.choice(deck)
    deck.remove(card)
    return card

def initial_draw(deck, player_hand, dealer_hand):
    i = 1
    while i < 2:
        card = draw_card(deck)
        player_hand.append(card)
        card = draw_card(deck)
        dealer_hand.append(card)


def check_bet(money):
    # check to see if user input is valid
    while True:
        try:
            bet = float(input("Bet: "))
        except ValueError:
            print("must be valid decimal number. Please try again.")
            continue
        if bet > money:
            print("Must be an amount less than " +str(money)+".")

        elif bet < 5:
            print("The minimum bet is 5. Please try again.")

        elif bet > 1000:
            print("The maximum bet is 1000. Please try again.")
        else:
            return bet

def print_hand(hand):
    i = 0
    for row in hand:
        print(hand[i][0]+ " of " +hand[i][1])
        i += 1
    print()

def player_turn(hand, deck, score):

    choice = input("Hit or stand? (hit/stand): ")

    while choice.lower == "hit":
        card = draw_card(deck)
        hand.append(card)
        score += card[2]
        print_hand(hand)

        choice = input("Hit or stand? (hit/stand): ")
    return score


def dealer_turn():
    pass

def main():
    display_title()

    money = int(db.load_money())
    deck = deck_gen()

    dealer_hand = []
    player_hand = []

    player_score = 0
    dealer_score = 0

    continue_game = "y"

    while continue_game.lower() == "y":
        print("Money: " +str(money))
        bet = check_bet(money)
        
        initial_draw(deck, player_hand, dealer_hand)

        print("DEALER'S SHOW CARD")
        print(dealer_hand[0][0]+ " of " +dealer_hand[0][1])
        print()

        print("YOUR CARDS")
        print_hand(player_hand)

        player_score = player_turn(player_hand, deck)
        
        print(player_score)
        

        continue_game = input("Play again? (y/n): ")

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()