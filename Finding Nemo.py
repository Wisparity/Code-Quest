cases = int(input().rstrip())

letters = []
spaces = 1 

for i in range(cases):
    line = input().rstrip()

    for j in line:
        letters.append(j)
    for k in range(len(letters)):
        if letters[k] == " ":
            spaces +=1
        if letters[k] == "N":
            if letters[k+1] == "I":
                if letters[k+2] == "M":
                    if letters[k+3] == "O":
                        print(spaces)

    letters.clear()
    spaces = 1
