import random

# from random import choice


number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)

for card in cards:
    print(card)
