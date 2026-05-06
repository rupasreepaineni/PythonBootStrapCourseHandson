#if we want to add a single item to a list then we can just add normal assignment +=, to add multiple items use .append
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,10, 10, 10, 11]
    card = random.choice(cards)
    return card
computer_cards =[]
user_cards=[]
user_score = -1
computer_score = -1

is_game_over = False
for card in range(2):
     # new_card = deal_card()
  # user_cards.append(new_card)
    user_cards.append(deal_card()) # above two lines will be replaced by this
    #to add multiple items use .append
     # *** user_cards+= new_card#if we want to add a single item to a list then we can just add normal assignment +
    computer_cards.append(deal_card())

def adding(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return "BlackJack"
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
""" above code deals with the adding the cards if the score is less by comparing"""



def compare(c_score ,u_score):
    if c_score == u_score:
        return "It's a draw"
    elif c_score == 0:
        return "user own, with a blackjack"
    elif u_score == 0:
        return "computer own with a black jack"
    elif c_score > 21:
        return "You went over, You lost"
    elif u_score > 21:
        return "Opponent went over, You lose"
    elif u_score > c_score:
        return "You went over, You win"
    else:
        return "You won"



"""below code deals with the checking the score and drawing the another card if needed"""

while is_game_over == False:
    user_score = adding(user_cards)
    computer_score = adding(deal_card())
    print(f"the user_cards are {user_cards} and the score is {user_score}")
    print(f"the dealer_cards are {computer_cards[0]}" )
    if user_score ==0 or computer_score ==0 or user_score > 21 :
        is_game_over = True
    else:
        user_another_card =  input("Do you have another card? (y/n)")
        if user_another_card == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True
#if score is 0, we define opposite as the ""blackjack
if computer_score !=0 or computer_score <=18:
    computer_cards.append(deal_card())
    computer_score = adding(computer_cards)

compare(computer_score,user_score)
