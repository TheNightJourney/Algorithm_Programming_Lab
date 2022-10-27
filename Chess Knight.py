
empty = [["" for i in range(8)] for i in range(8)]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
for i in range(8):
    for j in range(8):
        empty[j][i] = alphabet[i] + str(8 - j)

coord = input("Please select a coordinate : ")
i = alphabet.index(coord[0])
j = 8 - int(coord[1])

empty[j][i] = "KN"
if j + 1 <= 7:
    if i + 2 <= 7:
        empty[j + 1][i + 2] = "XX"
    if 0 <= i - 2:
        empty[j + 1][i - 2] = "XX"
    if j + 2 <= 7:
        if i + 1 <= 7:
            empty[j + 2][i + 1] = "XX"
        if 0 <= i - 1:
            empty[j + 2][i - 1] = "XX"
if 0 <= j - 1:
    if i + 2 <= 7:
        empty[j - 1][i + 2] = "XX"
    if 0 <= i - 1:
        empty[j - 1][i - 2] = "XX"
    if 0 <= j - 2:
        if i + 1 <= 7:
            empty[j - 2][i + 1] = "XX"
        if 0 <= i - 1:
            empty[j - 2][i - 1] = "XX"

for i in empty:
    print(i)

# i love kenneth jayadi yu