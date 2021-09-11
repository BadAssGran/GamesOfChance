# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:50:42 2021

@author: Teodora
"""

import random

money = 100

#Game of chance project

#A function which emulates a coin flip.
# The player can "call it" by passing either "heads" or "tails" to the function parameter.
def coin_flip(call_heads_or_tails, bet):
    #call_heads_or_tails(str) - either "heads" or "tails"
    #bet(int) - the amount of money the player bets
    money_available = money
    def sanitize_input(str1):
        new_call = ""
        letters = "headstil"
        for char in str1.lower():
            if char in letters:
                new_call += char
        return new_call
                
    if sanitize_input(call_heads_or_tails) not in ["heads", "tails"]:
        print("Not a valid call.")
        while True:
            call_heads_or_tails = sanitize_input(input("Please call heads or tails: "))
            if call_heads_or_tails in ["heads", "tails"]:
                break
    print(f"Your call is {call_heads_or_tails}.")  
    print(f"You have {money_available} available.")     
    if bet < 0 or bet > money_available:
        print("You cannot bet less than 0 or more than you have.")
        while True:
            bet = int(input("Please enter an amount to bet: "))
            if bet >= 0 and bet <= money_available:
                break 
    print(f"You bet {bet}.")
    
    
    def is_winner(call, result): 
        won = False
        if result % 2 == 0:
            print("The result is - heads!")
            if call == "heads":
                won = True
        else:
            print("The result is - tails!")
            if call == "tails":
                won = True
        return won    
    
    print("Tossing a coin...")    
    result = random.randint(1, 100)
    winner = is_winner(call_heads_or_tails, result)
      
    if winner:
        print("You win!")
        money_available += bet
        print(f"You have {money_available}.")
        return bet
    else:
        print("Sorry, you lose!")
        money_available -= bet
        print(f"You have {money_available}.")     
        return -bet


#A function simulating playing a two-die game (Cho-Han). The player
# wins if they correctly guess whether the sum of the two dice is odd or even.
# The function takes a parameter with the player's guess.

def cho_han_game(odd_or_even, bet):
    
    print("Playing Cho-Han. Rolling two dice...")
    money_available = money 
    
    def sanitize_input(str2):
        call = ""
        letters = "odevn"
        for char in str2.lower():
            if char in letters:
                call += char
        return call
    
    odd_or_even = sanitize_input(odd_or_even)
    if odd_or_even not in ["odd", "even"]:
        print("Your call is not valid.")
        while True:
            odd_or_even = sanitize_input(input("Please call odd or even: "))
            if odd_or_even in ["odd", "even"]:
                break
    print(f"Your call is {odd_or_even}.")        
    if bet < 0 or bet > money_available:
        print(f"You cannot bet less than 0 or more than {money_available}.")
        while True:
            bet = int(input("Please enter an amount to bet: "))
            if 0 <= bet <= money_available:
                break
    print(f"You bet {bet}.")
    def sum_dice():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Dice 1 : {dice1}, dice 2 : {dice2}.")
        return dice1 + dice2
    
    def is_winner(sum1):
        won = False
        if sum1 % 2 == 0:
            if odd_or_even == "even":
                won = True
        else:
            if odd_or_even == "odd":
                won = True
        return won
    
    dice_sum = sum_dice()
    winner = is_winner(dice_sum)
    
    if winner:
        print("You win!")
        money_available += bet
        print(f"You won {bet}. You have {money_available} available.")
        return bet
    else:
        print("Sorry, you lose.")
        money_available -= bet
        print(f"You have {money_available} left.")
        return -bet


#In the card game below two players bet, and the one who draws the higher card wins. In a draw no one wins.
def card_game(player_1_bet, player_2_bet):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    print("Playing a card game. Each player draws a card. The higher card wins!")

    hearts = [card + " of Hearts" for card in cards] #creates a list of all cards in the suite of Hearts
    diamonds = [card + " of Diamonds" for card in cards]
    spades = [card + " of Spades" for card in cards]
    clubs = [card + " of Clubs" for card in cards]

    full_deck = hearts + diamonds + spades + clubs #concatenates the 4 lists of the suites to create a list of all cards in a deck
    two_cards_draw = random.sample(full_deck, 2) # two cards are drawn simultaneously from the deck
    player_1_card = two_cards_draw[0] #the first card is assigned to Player 1
    player_2_card = two_cards_draw[1] #the second card is assigned to player 2
    
    money_available = money
    def good_bet(amt): #checks if the amount bet is valid
        if amt > 0 and amt <= money_available:
            return True
        return False
    
    if good_bet(player_1_bet) == False:
        print(f"Player 1's bet is invalid. You cannot bet less than 0 or more than {money_available}.")
        while True: #below asking for a valid input
            player_1_bet = int(input("Player 1 please enter a valid bet: "))
            if good_bet(player_1_bet) == True:
                break
    if good_bet(player_2_bet) == False:
        print(f"Player 2's bet is invalid. You cannot bet less than 0 or more than {money_available}.")
        while True:
            player_2_bet = int(input("Player 2 please enter a valid bet: "))
            if good_bet(player_2_bet) == True:
                break
            
    print(f"Player 1's card is {player_1_card}.\nPlayer 2's card is {player_2_card}.")
            
    if player_1_card[0] == player_2_card[0]: #if the cards have the same value - it's a draw
        print("It's a draw! No one wins the bet.")
        return 0
    else:
        if cards.index(player_1_card[0]) < cards.index(player_2_card[0]): #checking which card has the
                                                                            # higher index in the list cards - the higher index belongs to the higher card
            print(f"Player 2 wins.\nPlayer 2 won {player_2_bet}.\nPlayer 2 has " + str(money_available + player_2_bet))
            return player_2_bet
        else:
            print(f"Player 1 wins.\nPlayer 1 won {player_1_bet}.\nPlayer 1 has " + str(money_available + player_1_bet))
            return player_1_bet
        
        
# Simulation of a simplifed European roulette game.
# It is only possible to bet on a single number, red/black, high/low, or odd/even.

def roulette(call, bet):
    print("Playing roulette...\nNo more bets!")
    money_available = money
    
    call = str(call)
    
    roulette_nums = [num for num in range(37)]
    possible_calls = ["red", "black", "odd", "even", "high", "low"] + [str(num) for num in roulette_nums]
    
    def good_call(str1):
        new_call = ""
        for char in str1.lower():
            if char.isalnum():
                new_call += char 
        return new_call
    
    call = good_call(call)
    if call not in possible_calls:
        print("Your call is not valid.")
        while True:
            call = good_call(input("Please enter your call: "))
            if call in possible_calls:
                break
    
    if bet < 0 or bet > money_available:
        print(f"You can't bet less than 0 or more than {money_available}.")
        while True:
            bet = int(input("Please enter an amount to bet: "))
            if money_available >= bet >= 0:
                break
    
    print(f"Your call is {call}.\nYou bet {bet}.")
    
    black_numbers = [num for num in range(2, 11, 2)] + [num for num in range(11, 18, 2)] + [num for num in range(20, 29, 2)] + [num for num in range(31, 36, 2)]
    red_numbers = [num for num in roulette_nums[1:] if num not in black_numbers]
    
    winning_bet = random.randint(0, 37)
    
    if winning_bet in black_numbers:
        color_winner = "black"
        print(f"{winning_bet}, black.\nBlack wins.")
    elif winning_bet in red_numbers:
        color_winner = "red"
        print(f"{winning_bet}, red.\nRed wins.")
    else:
        color_winner = ""
        print(f"{winning_bet} wins.")
        
    if winning_bet in roulette_nums and winning_bet % 2 == 0:
        odd_even_winner = "even"
        print("Even wins.")
    elif winning_bet in roulette_nums and winning_bet % 2 == 1:
        odd_even_winner = "odd"
        print("Odd wins.")
        
    big_win = False 
    small_win = False
    
    if call == str(winning_bet):
        big_win = True
        
    if call == color_winner:
        small_win = True
        
    if call == odd_even_winner:
        small_win = True
        
    if call == "low" and winning_bet in [num for num in range(1, 19)]:
        small_win = True
        print("Low wins.")
    elif call == "high" and winning_bet in [num for num in range(19, 37)]:
        small_win = True
        print("High wins.")
        
        
    if big_win:
        print("Wow! A big win!\nYou won " + bet*35)
        return bet*35
    
    elif small_win:
        print(f"You win!\nYou won {bet}")
        return bet
    else:
        print("Sorry, you lose!")
        return - bet
    
    
    
    

#Call your game of chance functions here

# Testing the coin flip game:

#print(coin_flip("heads", 10)) #passes
#print(coin_flip("heads!", 10)) #passes - correctly sanitized input
#print(coin_flip("heads", -10)) #passes after correct amount of money is entered
#print(coin_flip("dragon", 10)) #passes after correct call is entered
#print(coin_flip("heads", 150)) #passes after a correct amount is enetered


# Testing Cho-Han

#print(cho_han_game("odd", 10)) # passes
#print(cho_han_game("odd???", 10)) # passes - correctly sanitized input
#print(cho_han_game("odd", -10)) # passes after a correct amount is bet
#print(cho_han_game("dragon", 10)) #passes after a correct call is entered
#print(cho_han_game("odd", 1000)) # passes after a correct amount is entered

# Testing the card game

#print(card_game(10, 10)) # passes
#print(card_game(-10, 10)) #passes after a correct input is entered
#print(card_game(10, 1000)) #passes after a correct bet is entered

# Testing the roulette game

#print(roulette("odd", 10)) #passes
#print(roulette("odd", -10)) #passes after a correct amount is entered
#print(roulette("biscuit?", 10)) #passes after correct amount is entered
#print(roulette("high", 1000)) #passes after a correct amount is bet

