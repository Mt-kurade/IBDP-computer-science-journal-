''' 
Instructions:

Create a Python game where two players (Player A and Player B) roll a pair of dice until one of them reaches or exceeds 50 points. The rolls and scores are stored using tuples.
Use random.randint(1, 6) to simulate a dice roll.
Use a while loop to keep rolling until either player reaches 50 points.

In each round:
· Both players roll two dice.

· Store each player's roll as a tuple (e.g., (3, 5)).

· Sum the tuple to get their round score.

Keep a running total of each player's score.

Announce the winner when someone reaches 50 points.
'''

'''
Logic breakdown:
1. Set player a and player b's score as zero 
2. Repeat rounds until either player's score or exceeds 50 points
    a. Both players roll dice (each die gives a random number between 1 and 6)
    b. Sotres each player's dice results as a tuples 
    c. Add the two numbers in the typle to get the players round score. 
    d. Add the round score to the player's total score. 

3. After each round, check if either player's score is 50 or more, if so, end the game and announce the winner.
'''

import random
player_a_score = 0
player_b_score = 0

while player_a_score < 50 and player_b_score < 50:
    player_a_roll = (random.randint(1, 6), random.randint(1, 6))
    player_a_round_score = sum(player_a_roll)
    player_a_score += player_a_round_score

    print(f"Player A rolled {player_a_roll} for a round score of {player_a_round_score}. Total score: {player_a_score}")


    player_b_roll = (random.randint(1, 6), random.randint(1, 6))
    player_b_round_score = sum(player_b_roll)
    player_b_score += player_b_round_score

    print(f"Player B rolled {player_b_roll} for a round score of {player_b_round_score}. Total score: {player_b_score}")
if player_a_score >= 50 and player_b_score >= 50:
    if player_a_score > player_b_score:
        print("Player A wins!")
    elif player_b_score > player_a_score:
        print("Player B wins!")
    else:
        print("It's a tie!")
elif player_a_score >= 50:
    print("Player A wins!")
else:
    print("Player B wins!")

