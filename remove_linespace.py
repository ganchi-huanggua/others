with open("a.txt", "r", encoding='utf-8') as source:
    with open("b.txt", "w", encoding='utf-8') as target:
        for line in source.readlines():
            target.write(line.strip())
    