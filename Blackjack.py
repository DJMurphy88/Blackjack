import random
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

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
            value = 11

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

def draw_card(turn, deck):
    card = random.choice(deck)
    if card[0] == "Ace":
        if turn == "player":
            card[2] = int(input("Ace equals 1 or 11?: "))
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
            print("Must be an equal or less than " +str(money)+".")

        elif bet < 5:
            print("The minimum bet is 5. Please try again.")

        elif bet > 1000:
            print("The maximum bet is 1000. Please try again.")
        else:
            return bet

def check_chips():
    money = float(db.load_money())
    while money < 5:
            print("You do not have enough chips")
            choice = input("Would you like to buy more? (y/n): ")
            if choice == "y":
                try:
                    money += int(input("How many chips? "))
                    db.save_money(money)
                    print()
                except ValueError:
                    print("must be valid decimal number. Please try again.")
    return money         

def print_hand(hand):
    i = 0
    for row in hand:
        print(hand[i][0]+ " of " +hand[i][1] +"("+str(hand[i][2])+")")
        i += 1

def player_turn(hand, score, deck):
    turn = "player"
    while score > 0 and score < 21:
            choice = input("\nHit or stand? (hit/stand): ")
            print()
            if choice == "hit":
                card = draw_card(turn, deck)
                hand.append(card)
                score += card[2]
                print_hand(hand)
            else:
                return score
    if score > 21:
        print("You've gone bust.\n")
        score = 0
    return score
    
def dealer_turn(hand, score, deck):
    turn = "dealer"
    while score > 0 or score < 17:
        card = draw_card(turn, deck)
        hand.append(card)
        score += card[2]
        if score > 21:
            score = 0
            return score
    return score

def main():
    display_title()

    money = check_chips()
    deck = deck_gen()

    continue_game = "y"

    while continue_game.lower() == "y":
        player_hand = []
        dealer_hand = []
        player_score = 0
        dealer_score = 0
        turn = "player"
        game_end = 0

        print("Money: " +str(money))
        bet = check_bet(money)
        money -= bet
        db.save_money(money)

        # Player initial hand 
        card = draw_card(turn, deck)
        player_hand.append(card)
        card = draw_card(turn, deck)
        player_hand.append(card)
        turn = "dealer"

        # Dealer initial hand
        card = draw_card(turn, deck)
        dealer_hand.append(card)
        card = draw_card(turn, deck)
        dealer_hand.append(card)
        turn = "player"

        print("\nDEALER'S SHOW CARD")
        print(dealer_hand[0][0]+ " of " +dealer_hand[0][1])

        print("\nYOUR CARDS")
        print_hand(player_hand)

        player_score = player_hand[0][2] + player_hand[1][2]
        dealer_score = dealer_hand[0][2] + dealer_hand[1][2]

        while game_end == 0:
            if turn == "player":
                player_score = player_turn(player_hand, player_score, deck)
                turn = "dealer"
            
            else:
                if player_score == 0:
                    print_hand(dealer_hand)
                    game_end = 1
                else:
                    dealer_score = dealer_turn(dealer_hand, dealer_score, deck)
                    print_hand(dealer_hand)
                    game_end = 1

        if player_score == 0:
            print("\nYOUR POINTS:\t\tbust")
        else:
            print("\nYOUR POINTS:\t\t" +str(player_score))

        if dealer_score == 0:
            print("DEALER'S POINTS:\tbust")
        else:
            print("DEALER'S POINTS:\t" +str(dealer_score))

        if player_score > dealer_score:
            money += (bet * 1.5)
            print("\nYou won.")       

        elif player_score < dealer_score:
            print("\nSorry. You lose.")
            
        else:
            money += bet
            print("\nIt's a draw.")

        
        print("MONEY: " +str(round(money, 2)))
        print()

        db.save_money(money)

        continue_game = input("Play again? (y/n): ")

    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()