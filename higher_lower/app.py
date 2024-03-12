from art import logo, vs
from data import data
import random
import os


def random_account():
    return random.choice(data)


def format_data(account):
    name = account.get('name')
    description = account.get('description')
    country = account.get('country')
    return f'{name}, a {description}, from {country}'


def check(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'a'
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
        while account_a == account_b:
            account_b = random_account()
        print(f'Compare A: {format_data(account_a)}.')
        print(vs)
        print(f'Against B: {format_data(account_b)}')
        answer = input('Who has more followers? Type "A" or "B": ').lower()
        iscorrect = check(
            answer, account_a.get('follower_count'), account_b.get('follower_count')
        )

        os.system('cls')
        print(logo)
        if iscorrect:
            score += 1
            print(f'Yes. You are right! Current score: {score}')
        else:
            game_isrunning = False
            print(f'Sorry, that is wrong. Final score: {score}')


if __name__ == '__main__':
    game()
