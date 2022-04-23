import random
import os
import time



class Card:
    def __init__(self, card_suit, card_face_value, card_score_value):
        self.card_suit = card_suit
        self.card_face_value = card_face_value
        self.card_score_value = card_score_value
        
def clear():
    os.system("clear")

# print the actual cards
def print_cards(types_of_cards, face_down_card):
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t _______________"
    if face_down_card:
        sequence += "\t _______________"
    print(sequence)
    
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|               |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        if card.card_face_value == '10':
            sequence = sequence + "\t|  {}           |".format(card.card_face_value)
        else:
            sequence = sequence + "\t|  {}            |".format(card.card_face_value)
    if face_down_card:
        sequence += "\t|               |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|  {}            |".format(card.card_suit)
    if face_down_card:
        sequence += "\t|      * *      |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|    *     *    |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|   *       *   |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|   *       *   |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|       {}       |".format(card.card_suit)
    if face_down_card:
        sequence += "\t|          *    |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|         *     |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|        *      |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|               |"
    if face_down_card:
        sequence += "\t|               |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|            {}  |".format(card.card_suit)
    if face_down_card:
        sequence += "\t|               |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        if card.card_face_value == '10':
            sequence = sequence + "\t|            {} |".format(card.card_face_value)
        else:
            sequence = sequence + "\t|            {}  |".format(card.card_face_value)
    if face_down_card:
        sequence += "\t|        *      |"
    print(sequence)
    
    sequence = ""
    for card in types_of_cards:
        sequence = sequence + "\t|_______________|"
    if face_down_card:
        sequence += "\t|_______________|"
    print(sequence)
    
    print()
    
    
    
    # To play an individual game...
    
def blackjack_game(deck):
    
    global card_values
    
    player_hand = []
    dealer_hand = []
    
    player_score = 0
    dealer_score = 0
    
    clear()
    
    
    
    # Initial deal
    
    while len(player_hand) < 2:
        
        player_card = random.choice(deck)
        player_hand.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_score_value
        
        
    # If 2 Aces present, set second Ace value to 1.
    
        if len(player_hand) == 2:
            if player_hand[0].card_score_value == 11 and player_hand[1].card_score_value == 11:
                player_hand[0].card_score_value = 1
                player_score -= 10
                
        print("YOUR HAND: ")
        print_cards(player_hand, False)
        print("YOUR SCORE: ", player_score)
        print("Press enter to continue...")
        
        input()
        
        
        
        # Random deal
        
        dealer_card = random.choice(deck)
        dealer_hand.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_score_value
        
        
        # Print dealer's hand and score above player's hand and score
        
        print("DEALER'S HAND: ")
        if len(dealer_hand) == 1:
            print_cards(dealer_hand, False)
            print("DEALER'S SCORE: ", dealer_score)

        else:
            print_cards(dealer_hand[:-1], True)
            print("DEALER'S SCORE: ", dealer_score - dealer_hand[-1].card_score_value)

            
        print("YOUR HAND: ")
        print_cards(player_hand, False)
        print("YOUR SCORE: ", player_score)
        print("Press enter to continue...")
         
         
    # If 2 Aces present, set second Ace value to 1.  
    
        if len(dealer_hand) == 2:
            if dealer_hand[0].card_score_value == 11 and dealer_hand[1].card_score_value == 11:
                dealer_hand[0].card_score_value = 1
                dealer_score -= 10
        
        input()
    
    # Player gets Blackjack
    
    if player_score == 21:
        print("Blackjack!!  You win!!")
        quit()
    
    clear()
        
        
    # Print dealer's and player's hands
    
    print("DEALER'S HAND: ")
    print_cards(dealer_hand[:-1], True)
    print("DEALER'S SCORE: ", dealer_score - dealer_hand[-1].card_score_value)
    
    print()
    
    print("YOUR HAND: ")
    print_cards(player_hand, False)
    print("YOUR SCORE: ", player_score)
    
    while player_score < 21:
        choice = input("Do you want to hit (H) or stand (S)? ")
        
        
        # Input error prevention
        
        if len(choice) != 1 or (choice.upper() != "H" and choice.upper() != "S"):
            clear()
            print("No, do that later.  Right now, you need to decide whether to hit or stand.")
           
           
        # Player decides to hit.
        
        if choice.upper() == "H":
            player_card = random.choice(deck)
            player_hand.append(player_card)
            deck.remove(player_card)
            
            player_score += player_card.card_score_value
            
            
            # Score of the Ace in the player's hand
            
            ace = 0
            while player_score > 21 and ace < len(player_hand):
                if player_hand[ace].card_score_value == 11:
                    player_hand[ace].card_score_value = 1
                    player_score -= 10
                    ace += 1
                else:
                    ace += 1
                    
            clear()
            
        
            # Continue to print dealer's and player's hands
            
            print("DEALER'S HAND: ")
            print_cards(dealer_hand[:-1], True)
            print("DEALER'S SCORE: ", dealer_score - dealer_hand[-1].card_score_value)
            
            print()
            
            print("YOUR HAND: ")
            print_cards(player_hand, False)
            print("YOUR SCORE: ", player_score)
        
        
        # Player stands
        
        if choice.upper() == "S":
            break
    
    clear()


    # Continue to print dealer's and player's hands
    
    print("*****  The dealer is revealing his hand.... *****")

    print("DEALER'S HAND: ")
    print_cards(dealer_hand, False)
    print("DEALER'S SCORE: ", dealer_score)
    
    print()
    
    print("YOUR HAND: ")
    print_cards(player_hand, False)
    print("YOUR SCORE: ", player_score)
    print("Press enter to continue...")

    print()

    
    # Player gets Blackjack
    
    if player_score == 21:
        print("Blackjack!!  You win!!")
        quit()
        
        
    # Player busts
    
    if player_score > 21:
        print("You busted!!  Game over, pal!!")
        quit()
        
    input()
        
            
    # Dealer hits or stands / Las Vegas rules
    
    while dealer_score < 17:
        clear()
        
        print("***** The dealer has decided to hit. *****")
        
        dealer_card = random.choice(deck)
        dealer_hand.append(dealer_card)
        deck.remove(dealer_card)
        
        dealer_score += dealer_card.card_score_value
        
        
        # Score of the Ace in the dealer's hand
        
        ace = 0
        while dealer_score > 21 and ace < len(dealer_hand):
            if dealer_hand[ace].card_score_value == 11:
                dealer_hand[ace].card_score_value = 1
                dealer_score -= 10
                ace += 1
            else:
                ace += 1
            
            
        # Continue to print dealer's and player's hands
        
        print("DEALER'S HAND: ")
        print_cards(dealer_hand, False)
        print("DEALER'S SCORE: ", dealer_score)
        
        
        print()
        
        print("YOUR HAND: ")
        print_cards(player_hand, False)
        print("YOUR SCORE: ", player_score)
        print("Press enter to continue...")
        
        
        input()
        
        
    # End results
        
    if dealer_score > 21:
        print("Dealer busts!  You win!")
        quit()
        
    if dealer_score == 21:
        print("Dealer has blackjack!  You lose!")
        
    if dealer_score == player_score:
        print("Ooooh....a tie.....")
        
    elif player_score > dealer_score:
        print("You win!")
        
    else:
        print("Dealer wins!")
        
if __name__ == '__main__':
            
            
    # All possible cards in the deck
    
    types_of_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    
    suit_values = {"Hearts": "\u2661", "Diamonds": "\u2662", "Spades": "\u2664", "Clubs": "\u2667"}
    
    types_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    
    card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    
    
    
    # The given deck of cards for the game
    
    deck = []
    for card_suit in types_of_suits:
        for card in types_of_cards:
        
            deck.append(Card(suit_values[card_suit], card, card_values[card]))
            
    blackjack_game(deck)


    
    
    
     