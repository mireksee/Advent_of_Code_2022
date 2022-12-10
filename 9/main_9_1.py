input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

commands = input.strip().split("\n")

H = [0,0]
T = [0,0]

mT = {(0,0)}

for command in commands:
    direction, how_many = command.split(" ")
    how_many = int(how_many)

    for _ in range(how_many):
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0

        H[0] += dx
        H[1] += dy

        rx = H[0] - T[0]
        ry = H[1] - T[1]

        if abs(rx) > 1 or abs(ry) > 1:
            T[0] += 0 if rx == 0 else int(rx / abs(rx))
            T[1] += 0 if ry == 0 else int(ry / abs(ry))

            mT.add(tuple(T))

print(len(mT))