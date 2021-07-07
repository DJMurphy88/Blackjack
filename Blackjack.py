import random
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def deck_gen():
    deck = []
    cards = 0
    
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

def player_turn(hand, score, deck):
    choice = input("Hit or stand? (hit/stand): ")    
    while score > 0 or score < 21:
        while choice == "hit":
            print(score)
            card = draw_card(deck)
            hand.append(card)
            score += card[2]
            print_hand(hand)           
            if score < 21:
                choice = input("Hit or stand? (hit/stand): ")
            else:
                print("\nYou've gone bust")
                score = 0
                return score
        return score
    
def dealer_turn(hand, score, deck):
    while score > 0 or score < 17:
        print(score)
        card = draw_card(deck)
        hand.append(card)
        score += card[2]
        if score > 21:
            score = 0
            return score
    return score

def main():
    display_title()

    money = int(db.load_money())
    deck = deck_gen()

    continue_game = "y"
    
    while continue_game.lower() == "y":
        dealer_hand = []
        player_hand = []
        print("Money: " +str(money))
        bet = check_bet(money)
        money -= bet
        turn = "player"
        game_end = 0
        
        card = draw_card(deck)
        player_hand.append(card)
        card = draw_card(deck)
        player_hand.append(card)
        card = draw_card(deck)
        dealer_hand.append(card)
        card = draw_card(deck)
        dealer_hand.append(card)

        print("DEALER'S SHOW CARD")
        print(dealer_hand[0][0]+ " of " +dealer_hand[0][1])
        print()

        print("YOUR CARDS")
        print_hand(player_hand)

        player_score = player_hand[0][2] + player_hand[1][2]
        print(player_score)

        dealer_score = dealer_hand[0][2] + dealer_hand[1][2]

        while game_end == 0:
            if turn == "player":
                print("player's turn")
                player_score = player_turn(player_hand, player_score, deck)
                turn = "dealer"
            
            else:
                print("dealer's turn")
                dealer_score = dealer_turn(dealer_hand, dealer_score, deck)
                print_hand(dealer_hand)
                game_end = 1

        if player_score == 0:
            print("YOUR POINTS:\t\tbust")
        else:
            print("YOUR POINTS:\t\t" +str(player_score))

        if dealer_score == 0:
            print("DEALER'S POINTS:\tbust")
        else:
            print("DEALER'S POINTS:\t" +str(dealer_score))

        if player_score > dealer_score:
            money += (bet * 1.5)
            print("You won")       

        elif player_score < dealer_score:
            print("You lost")
            
        else:
            money += bet
            print("It's a draw")

        db.save_money(money)
        print("MONEY: " +str(round(money, 2)))
        print()
        continue_game = input("Play again? (y/n): ")

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()