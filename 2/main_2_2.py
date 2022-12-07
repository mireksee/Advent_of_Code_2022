input = """A Y
B X
C Z"""

rounds = input.split("\n")

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
rules = {
    "A X": 3, # Rock Rock
    "A Y": 6, # Rock Paper
    "A Z": 0, # Rock Scissors
    "B X": 0, # Paper Rock
    "B Y": 3, # Paper Paper
    "B Z": 6, # Paper Scissors
    "C X": 6, # Scissors Rock
    "C Y": 0, # Scissors Paper
    "C Z": 3  # Scissors Scissors
}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
rules2 = {
    "A X": "Z", # Rock lose
    "A Y": "X", # Rock draw
    "A Z": "Y", # Rock win
    "B X": "X", # Paper lose
    "B Y": "Y", # Paper draw
    "B Z": "Z", # Paper win
    "C X": "Y", # Scissors lose
    "C Y": "Z", # Scissors draw
    "C Z": "X"  # Scissors win
}

points = {"X": 1, "Y": 2, "Z": 3}

totalScore = 0

for round in rounds:
    player1, _ = round.split(" ")
    player2 = rules2[round]
    totalScore += rules[player1 + " " + player2]
    totalScore += points[player2]

print(totalScore)