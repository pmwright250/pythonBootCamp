from art import logo,vs
from game_data import data
import random

def compare_follower_count(a,b,guess,score):
    if a['follower_count'] >= b['follower_count'] and guess.upper() == 'A' or b['follower_count'] >= a['follower_count'] and guess.upper() == 'B':
        return score + 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return -1

def game():
    print(logo)
    score = 0
    dict_a = random.choice(data)
    dict_b = random.choice(data)

    print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}")
    print(vs)
    print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}")
    guess = input("Who has more followers? 'A' or 'B':")

    score = compare_follower_count(dict_a,dict_b,guess,score)
    while score > 0:
        dict_a = dict_b
        dict_b = random.choice(data)
        print(logo)
        print(f"You're right! Current score: {score}")
        print(f"Compare A: {dict_a['name']}, a {dict_a['description']}, from {dict_a['country']}")
        print(vs)
        print(f"Against B: {dict_b['name']}, a {dict_b['description']}, from {dict_b['country']}")
        guess = input("Who has more followers? 'A' or 'B':")
        score = compare_follower_count(dict_a, dict_b, guess, score)
    return

game()