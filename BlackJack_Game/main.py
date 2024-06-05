################## Our BlackJack House Rules #####################
# The deck is unlimited in size
# There are no Jokers
# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1

# Create a deal card function which returns the random card using the list.
# 11 is the ace
import random
def deal_card():
    """Returns a random card from deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
# Deal the user and computer 2 cards each using deal_card()

def calculate_score(cards):
    if sum(cards)==21 or 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You Lose, Opponent has BlackJack 😱"
    elif user_score == 0:
        return "You Win with a BlackJack 😎"
    elif user_score > 21:
        return "You went over 21,You Lose! 😭"
    elif computer_score > 21:
        return "Opponent went over 21, You Win 😁"
    elif user_score > computer_score:
        return 'You Win 😀'
    else:
        return "You Lose 🙁"
def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
            
    while not is_game_over:

        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards {user_cards}, current score {user_score}")
        print(f" Computer's First card {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            users_choice=input("Type 'y' to add another card , Type 'n' to pass: ")
            if users_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your Score: {user_score}, Computer Score {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you wanna play game ?? Type 'y' for Yes and 'n' for No: ")=='y':
    play_game() 

    



