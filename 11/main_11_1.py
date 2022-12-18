input = """Monkey 0:
  Starting items: 64
  Operation: new = old * 7
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 1:
  Starting items: 60, 84, 84, 65
  Operation: new = old + 7
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 2:
  Starting items: 52, 67, 74, 88, 51, 61
  Operation: new = old * 3
  Test: divisible by 5
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 3:
  Starting items: 67, 72
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 2

Monkey 4:
  Starting items: 80, 79, 58, 77, 68, 74, 98, 64
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 5:
  Starting items: 62, 53, 61, 89, 86
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 4
    If false: throw to monkey 6

Monkey 6:
  Starting items: 86, 89, 82
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 7:
  Starting items: 92, 81, 70, 96, 69, 84, 83
  Operation: new = old + 4
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 5"""

lines = list(map(str.strip, input.split("\n")))

current_monkey = None
monkeys = {}

for line in lines:
  if line[:6] == 'Monkey':
    current_monkey = int(line[7:-1])
    monkeys[current_monkey] = {
      'items': {},
      'operation': {},
      'test_divisible_by': None,
      'if_true': None,
      'if_false': None,
      'inspected': 0
    }

  elif line[:14] == 'Starting items':
    monkeys[current_monkey]['items'] = list(map(int,line[16:].split(', ')))
  elif line[:9] == 'Operation':
    monkeys[current_monkey]['operation'] = line[17:]
  elif line[:4] == 'Test':
    monkeys[current_monkey]['test_divisible_by'] = int(line[19:])
  elif line[:7] == 'If true':
    monkeys[current_monkey]['if_true'] = int(line[25:])
  elif line[:8] == 'If false':
    monkeys[current_monkey]['if_false'] = int(line[26:])


for _ in range(20):
  for key, monkey in monkeys.items():
    for item in monkey['items']:
      monkey['inspected'] += 1
      new = int(eval(monkey['operation'], {'old': item}))
      new = new // 3
      if (new % monkey['test_divisible_by'] == 0 ):
        monkeys[monkey['if_true']]['items'].append(new)
      else:
        monkeys[monkey['if_false']]['items'].append(new)
    monkey['items'] = []

inspected = []
for key, monkey in monkeys.items():
  inspected.append(monkey['inspected'])

inspected = sorted(inspected)

print (inspected[-1]*inspected[-2])







