def parseToken(s):
    sl = s.replace("\n", " ").split(" ")
    tokens = []
    for i in sl:
        if i == "cmt":
            break
        tokens.append(i)
    return tokens

def isOperator(s):
    return s in ["+", "-", "/", "*", "^", "%"]

def isReversed(s):
    return s in ["get", "output", "goto", "stop", "let", "if"]

tokens = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        frll = frl.replace("\n", "").split(" ")
        for i in frll:
            if i == "cmt":
                break
            tokens.append(i)
print(tokens)