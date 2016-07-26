def bingo(num, list):
    found = False
    for elem in list:
        print(elem)
        if num == elem:
            found = True
            break
    if found:
        print("BINGO")

print("Bingo game:")
bingo(2, [1,2])
print("Bingo game:")
bingo(2, [1,4,5,2])
print("Bingo game:")
bingo(2, [1,3,4,5,6,7,8,9,10])
print("Bingo game:")
bingo(2, [])