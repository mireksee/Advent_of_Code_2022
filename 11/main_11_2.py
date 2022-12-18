import math;

input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

lines = list(map(str.strip, input.split("\n")))

current_monkey = None
monkeys = []

for line in lines:
  if line[:6] == 'Monkey':
    current_monkey = int(line[7:-1])
    monkeys.append({
      'items': {},
      'operation': {},
      'test_divisible_by': None,
      'if_true': None,
      'if_false': None,
      'inspected': 0
    })

  elif line[:14] == 'Starting items':
    monkeys[current_monkey]['items'] = list(map(int,line[16:].split(', ')))
  elif line[:9] == 'Operation':
    op = line[17:]
    monkeys[current_monkey]['operation'] = lambda old,op=op:eval(op)
  elif line[:4] == 'Test':
    monkeys[current_monkey]['test_divisible_by'] = int(line[19:])
  elif line[:7] == 'If true':
    monkeys[current_monkey]['if_true'] = int(line[25:])
  elif line[:8] == 'If false':
    monkeys[current_monkey]['if_false'] = int(line[26:])

lcm = 1
for monkey in monkeys:
  lcm *= (lcm* monkey['test_divisible_by'])//math.gcd(lcm, monkey['test_divisible_by'])

for i in range(10000):
  for x in range(len(monkeys)):
    for item in monkeys[x]['items']:
      monkeys[x]['inspected'] += 1
      new = monkeys[x]['operation'](item)%lcm

      if (new % monkeys[x]['test_divisible_by'] == 0 ):
        monkeys[monkeys[x]['if_true']]['items'].append(new)
      else:
        monkeys[monkeys[x]['if_false']]['items'].append(new)
    monkeys[x]['items'] = []

inspected = []
for monkey in monkeys:
  inspected.append(monkey['inspected'])

inspected = sorted(inspected)

print (inspected[-1]*inspected[-2])







