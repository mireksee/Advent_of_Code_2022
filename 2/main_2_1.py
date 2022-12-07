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

points = {"X": 1, "Y": 2, "Z": 3}

totalScore = 0

for round in rounds:
    totalScore += rules[round]
    _, player2 = round.split(" ")
    totalScore += points[player2]

print(totalScore)