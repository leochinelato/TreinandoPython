from art import logo

print(logo)
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "left" or "right".'
).lower()

if choice1 == 'right':
    print('You fell into a hole. Game Over.')
elif choice1 == 'left':
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
    ).lower()
    if choice2 == 'swim':
        print('You got attacked by an angry trout. Game Over.')
    elif choice2 == 'wait':
        choice3 = input(
            'You arrive at the island unharmed. There is a house with 3 choice3s. One red, one yellow and one blue. Which colour do you choose?'
        ).lower()
        if choice3 == 'blue':
            print('You enter a room of beasts. Game Over.')
        elif choice3 == 'red':
            print('It\'s a room full of fire. Game Over.')
        elif choice3 == 'yellow'.lower():
            print('You found the treasure! You Win!')
