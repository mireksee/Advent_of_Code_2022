input = """30373
25512
65332
33549
35390"""

forest = input.strip().split("\n")

rows = []
cols = []

for trees in forest:
    row = [int(x) for x in trees]
    rows.append(row)
    for index, col in enumerate(row):
        if not(index in range(len(cols))):
            cols.append([])
        cols[index] += [col]

result = 0

for index_row, row in enumerate(rows):
    for index_col, value in enumerate(row):
        if index_row == 0 or index_row == len(row)-1 or index_col == 0 or index_col == len(cols[0])-1: #on the edge
            result += 1
            continue
        else:
            left = max(row[:index_col])
            if left < value:
                result += 1
                continue
            right = max(row[index_col+1:])
            if right < value:
                result += 1
                continue
            top  = max(cols[index_col][:index_row])
            if top < value:
                result += 1
                continue
            bottom  = max(cols[index_col][index_row+1:])
            if bottom < value:
                result += 1
                continue

print(result)