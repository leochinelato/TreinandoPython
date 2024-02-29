from random import choice
import os
from art import logo


def deal_card():
    '''
    Deal and return a random card from the list
    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    '''
    Take a list of cards and return score calculated from the cards
    '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw :|'
    elif computer_score == 0:
        return 'You lose, opponent has a BlackJack :('
    elif user_score == 0:
        return 'You win with a BlackJack.'
    elif user_score > 21:
        return 'You lose with over 21... :('
    elif computer_score > 21:
        return 'You win. Opponent went over.'''
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'You lose :('

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for c in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}\nYour score: {user_score}')
        print(f"\nComputer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_option = input('Do you want a another card? [y/n]: ')
            if user_option in 'yY':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f' Your final hand: {user_cards} and your score: {user_score}')
    print(f" Computer's final hand: {computer_cards}, score: {computer_score}")
    print(compare(user_score,computer_score))

if __name__ == '__main__':
    while input('Do you want to play a game of Blackjack? Type "y" or "n": ') in 'Yy':
        os.system('clear')
        play_game()