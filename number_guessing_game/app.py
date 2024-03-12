from random import randint
from art import logo


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "hard":
        return 5
    return 10


def choose_number():
    print("I'm thinking of a number between 1 and 100.")
    return randint(1, 100)


def guess_number():
    return int(input('Make a guess: '))


if __name__ == '__main__':
    print(logo)
    answer = choose_number()
    attemps = choose_difficulty()
    for a in range(attemps):
        guess = guess_number()
        if guess == answer:
            print(f"YOU WIN! The answer was {answer}")
            break
        elif guess > answer:
            print('Too high.')
        else:
            print('Too low.')

        print(f'You have {attemps-(a+1)} attemps remaining to guess the number')
        print('Guess again.')
