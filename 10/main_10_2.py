input="""noop
noop
addx 5
addx 29
addx -28
addx 5
addx -1
noop
noop
addx 5
addx 12
addx -6
noop
addx 4
addx -1
addx 1
addx 5
addx -31
addx 32
addx 4
addx 1
noop
addx -38
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -32
addx 33
addx -20
addx 27
addx -39
addx 1
noop
addx 5
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -16
addx 21
addx -1
addx 1
noop
addx 3
addx 5
addx -22
addx 26
addx -39
noop
addx 5
addx -2
addx 2
addx 5
addx 2
addx 23
noop
addx -18
addx 1
noop
noop
addx 2
noop
noop
addx 7
addx 3
noop
addx 2
addx -27
addx 28
addx 5
addx -11
addx -27
noop
noop
addx 3
addx 2
addx 5
addx 2
addx 27
addx -26
addx 2
addx 5
addx 2
addx 4
addx -3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx -33
noop
noop
noop
noop
addx 31
addx -26
addx 6
noop
noop
addx -1
noop
addx 3
addx 5
addx 3
noop
addx -1
addx 5
addx 1
addx -12
addx 17
addx -1
addx 5
noop
noop
addx 1
noop
noop"""

lines = input.strip().split("\n")

r = {20,60,100,140,180,220}

CRT = [['.' for _ in range(40)] for _ in range(6)] #part2

cycles = 0
register_x = 1
sum_singal_strengths = 0

for line in lines:
    cycle = 1 if line == "noop" else 2

    for i in range(cycle):
        cycles += 1

        tick = cycles - 1 #part2
        CRT[tick // 40][tick % 40] = ('#' if abs(register_x-(tick % 40)) <= 1 else ' ') #part2

        # if cycles in r: #part1
        #     sum_singal_strengths += cycles * register_x #part1

        if cycle > 1 and i == cycle-1:
            _, value  = line.split(" ")
            register_x += int(value)

# print(sum_singal_strengths) #part1

for r in range(6): #part2
    print(''.join(CRT[r])) #part2
