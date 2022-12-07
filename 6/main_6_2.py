input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

for i in range(0, len(input)-3):
    substring = input[i:14+i]
    if len(set(substring)) == len(substring):
        print(14+i)
        break