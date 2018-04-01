def parseToken(frl):
    tokens = []
    frll = frl.replace("\n", "").split(" ")
    for i in frll:
        if i == "cmt":
            break
        tokens.append(i)
    return tokens