input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

commands = input.strip().split("\n")

R = [[0,0] for _ in range(10)]

mT = {(0,0)}

for command in commands:
    direction, how_many = command.split(" ")
    how_many = int(how_many)

    for _ in range(how_many):
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0

        R[0][0] += dx
        R[0][1] += dy

        for i in range(9):
            H = R[i]
            T = R[i+1]
            rx = H[0] - T[0]
            ry = H[1] - T[1]

            if abs(rx) > 1 or abs(ry) > 1:
                T[0] += 0 if rx == 0 else int(rx / abs(rx))
                T[1] += 0 if ry == 0 else int(ry / abs(ry))

        mT.add(tuple(R[-1]))

print(len(mT))