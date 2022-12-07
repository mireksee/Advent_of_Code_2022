input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

commands = input.strip().split("\n")

folders = {}
paths = []

for command in commands:
    term = command.split(" ")
    if term[0] == "$":
        if term[1] == "cd":
            if term[2] == '..':
                paths.pop();
            else:
                paths.append(term[2])
    elif term[0] != "dir": #file
        current_path = ""
        for path in paths:
            if path != "/" and current_path != "/":
                current_path += "/"
            current_path += path;
            folders[current_path] = folders.get(current_path, 0) + int(term[0])

result = folders.get('/')
limit = 30000000 - (70000000 - result)

for _, size in folders.items():
    if size >= limit:
        result = min(result, size);

print(result)