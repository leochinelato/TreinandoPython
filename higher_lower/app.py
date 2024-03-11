from art import logo, vs
from data import data
import random
import os

def random_account():
    return random.choice(data)


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'


def check(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(logo)
    score = 0
    game_isrunning = True
    account_a = random_account()
    account_b = random_account()

    while game_isrunning:
        account_a = account_b
        account_b = random_account()
        print(f'a: {account_a},\n b: {account_b}')
        while account_a == account_b:
            account_b = random_account()
            print(f'Compare A: {format_data(account_a)}.')
            print(vs)
            print(f'Against B: {format_data(account_b)}')
            answer = input('Who has more followers? Type "A" or "B": ').lower()
            iscorrect = check(answer, account_a['follower_count'], account_b['follower_count'])

            os.system('cls')
            print(logo)
            if iscorrect:
                score += 1
                print(f'Yes. You are right! Current score: {score}')
            else:
                print(f'Sorry, that is wrong. Final score: {score}')
                game_isrunning = False


if __name__ == '__main__':
    game()
