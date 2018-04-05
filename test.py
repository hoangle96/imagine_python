# check to see a given string, s, is an operator
def isOperator(s):
    return s in ["+", "-", "/", "*", "^", "%", "=", ">", "<", "!=", "(", ")"]


# check to see a given string, s, is a reserved word
def isReserved(s):
    return s in ["get", "output", "goto", "stop", "let", "if"]


# parsing the given plain program from file "test.txt" to tokens. The program will read each line of the input file
# and split the line by spaces between each word to produce an array of string
# for each element of the array, check whether the element is in the token array,
# If yes, it will skip the element. If not, it will be added to the tokens element.
# If the element is "cmt", the element itself will be added, but the rest of the line will be ignored.
tokens = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        frll = frl.replace("\n", "").split(" ")
        for i in frll:
            if i not in tokens:
                if i == "cmt":
                    tokens.append(i)
                    break
                tokens.append(i)
print(tokens)


# Parsing the given plain program from file "test.txt" to the symbol table. The program will read each line of the
# input file and split the line by spaces between each word to produce an array of string for each element of the
# array, check whether the element is in the duplicate array. If yes, it will skip the element. If not, it will be
# checked against different cases. If the element is "goto" or "cmt", the program will ignore it. If the element is
# the first element in the array, it will be a line number. If it is not an operator and a reserved word,
# to the tokens element, it will be checked to be whether a number, which will be a constant, or a variable. If it is
# a constant or a variable, it will be added from the highest memory locations to the lower ones.
min = 0
max = 99

table = []
dup = []
with open('test.txt', "r") as f:
    for frl in f.readlines():
        frll = frl.replace("\n", "").split(" ")
        for i in frll:
            if i not in dup:
                if i == "goto" or i == "cmt":
                    break
                if frll.index(i) == 0:
                    table.append(["L", frll[0], min])
                    min += 1
                elif not (isOperator(i)) and not (isReserved(i)):
                    if i.isdigit():
                        table.append(["C", i, max])
                        max -= 1
                    elif i.isalpha() or i.isalnum():
                        table.append(["V", i, max])
                        max -= 1
                    dup.append(i)
for i in table:
    print(i)
