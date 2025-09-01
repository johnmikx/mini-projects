from deck import Deck
from hand import Hand

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you wanna play? "))
            except:
                print("You must enter a number.")
        
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print('*' * 30)
            print(f'Game {game_number} of {games_to_play}')
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""

            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input("Please choose 'Hit or 'Stand (or H/S): ").lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ['hit', 'h']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)
        
        print("\nThanks for playing!")
    
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! 🤣")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You WIN! 🥳")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have blackjack! It's a Tie! 😍")
                return True
            elif player_hand.is_blackjack():
                print("You have BLACKJACK. You WIN! 😲")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has BLACKJACK. Dealer wins! 🤣")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You WIN! 😲")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("TIE HAHA! 😂")
            else:
                print("Dealer Wins! 🥺")
            return True
        return False