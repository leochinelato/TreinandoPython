import os
from art import logo
print(logo)

bids = {}
other_bidders = True

def find_highest_bidder(bids_dict):
    highest_bidder = max(bids_dict, key=bids_dict.get)
    highest_bid = max(bids_dict.values())
    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}.')


while other_bidders:
    name = input('What is your name? ')
    bid = float(input("What's your bid? $"))
    option = input('Are there any other bidders? Type "yes" or "no".')
    bids[name] = bid
    os.system('cls')
    if option == 'no':
        find_highest_bidder(bids)
        other_bidders = False