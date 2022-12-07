input = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

for i in range(0, len(input)-3):
    substring = input[i:4+i]
    if len(set(substring)) == len(substring):
        print(4+i)
        break