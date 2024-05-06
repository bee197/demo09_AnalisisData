list = [3, 2, 0, 1, 4]
index = 0
while 1:
    index += list[index]
    if index == len(list) - 1:
        print("true")
        break
    if index > len(list) - 1:
        print("false")
        break
    if list[index] == 0:
        print("false")
        break
s = input()
print(int(s))
