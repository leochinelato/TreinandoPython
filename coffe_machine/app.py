hot_flavours = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

resources = {
    'water': 200,
    'milk': 200,
    'coffee': 100,
}


coins = {
    'Penny': 0.01,
    'Nickel': 0.05,
    'Dime': 0.10,
    'Quarter': 0.25,
}

profit = 0


def report():
    for k, v in resources.items():
        print(f'{k}: {v}')
    print(f'${profit}')


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f'We need {item}.')
            return False
    return True


def insert_coins():
    print('Please insert coins.')
    total = 0
    for k, v in coins.items():
        try:
            money = int(input(f'How many {k.lower()}?: '))*v
            total += money
        except ValueError:
            print('Type a number. Try again.')
            return 0
    return total


def check_transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f'Here is your change: ${change}.')
        global profit
        profit += cost
        return True
    else:
        print('That is not enough money. Refunded.')
        return False


def make_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name} ☕️!!")


def coffee_machine():
    machine_is_running = True
    while machine_is_running:
        menu_option = input('What would you like? (espresso, latte or cappuccino): ')
        if menu_option == 'report'.lower():
            report()
        elif menu_option == 'off'.lower():
            print('Turning off coffee machine...')
            machine_is_running = False
        else:
            try:
                drink = hot_flavours[menu_option]
                if check_resources(drink['ingredients']):
                    payment = insert_coins()
                    if check_transaction(payment, drink['cost']):
                        make_coffee(menu_option, drink['ingredients'])
            except KeyError:
                print('Invalid option. Try again.')


def main():
    coffee_machine()


if __name__ == '__main__':
    main()
