#Перше завдання
list = []

userKil = int(input("Введіть кількість елементів списку: "))

for i in range(userKil):
    elem = input(f"Введіть елемент номер {i + 1}: ")
    list.append(elem)

def mainPrint (list):
    print("Main list =[ ", end='')
    for i in range(len(list)):
        print("'"+list[i], end="' ")
    print("]")

def reversePrint (list):
    print("Reverse list =[ ", end='')
    for i in range(len(list) - 1, -1, -1):
        print("'"+list[i], end="' ")
    print("]")

print("Кількість елементів списку:", len(list))

mainPrint(list)
reversePrint(list)

#Друге завдання
def pairprint(list):
    pairList = []
    secElem = 0
    for i in range(1, len(list), +2):
        secElem = list[i]
        pairList.append(secElem)

    print("Pair list =[ ", end='')
    for i in range(len(pairList)):
        print("'"+pairList[i], end="' ")
    print("]")

pairprint(list)