import parse as parse

tokens = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        tokens = parse.parseToken(frl)
print(tokens)