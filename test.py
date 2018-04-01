def parseToken(s):
    sl = s.replace("\n", " ").split(" ")
    tokens = []
    for i in sl:
        if i == "cmt":
            break
        tokens.append(i)
    return tokens

def isOperator(s):
    return s in ["+", "-", "/", "*", "^", "%", "="]

def isReserved(s):
    return s in ["get", "output", "goto", "stop", "let", "if"]

tokens = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        frll = frl.replace("\n", "").split(" ")
        for i in frll:
            if i == "cmt":
                tokens.append(i)
                break
            tokens.append(i)
print(tokens)

min = 0
max = 99

table = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        frll = frl.replace("\n", "").split(" ")
        # table.append(["L", frll[0], min])
        # min += 1
        for i in frll:
            if frll.index(i) == 0:
                table.append(["L", frll[0], min])
                min += 1
            elif i == "cmt":
                break
            elif not(isOperator(i)) and not(isReserved(i)):
                if i.isdigit():
                    table.append(["C", i, max])
                    max -= 1
                elif i.isalpha() or i.isalnum():
                    table.append(["V", i, max])
                    max -= 1

for i in table:
    print(i)

print(isReserved("get"))

