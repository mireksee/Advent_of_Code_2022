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

def get_len_by(trees, value):
    for index, tree in enumerate(trees):
        if tree >= value:
           return len(trees[:index+1])
    return len(trees)

for index_row, row in enumerate(rows):
    for index_col, value in enumerate(row):
        if index_row == 0 or index_row == len(row)-1 or index_col == 0 or index_col == len(cols[0])-1: #on the edge
            continue
        else:
            product = get_len_by(list(reversed(row[:index_col])), value) * get_len_by(row[index_col+1:], value) * get_len_by(list(reversed(cols[index_col][:index_row])), value) * get_len_by(cols[index_col][index_row+1:], value)

            if (result < product):
                result = product

print(result)