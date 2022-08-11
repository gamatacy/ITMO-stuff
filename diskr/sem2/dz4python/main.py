# Мне стыдно за это...


# Матрица соединений G'
matrix = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
          [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0],
          [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
          [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
          [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]]

keys = {
    "1": "U1-6",
    "2": "U2-7",
    "3": "U2-9",
    "4": "U2-10",
    "5": "U3-10",
    "6": "U4-6",
    "7": "U4-7",
    "8": "U4-9",
    "9": "U4-11",
    "10": "U5-7",
    "11": "U5-9",
    "12": "U5-10",
    "13": "U5-12",
    "14": "U6-10",
    "15": "U7-9",
    "16": "U7-11",
    "17": "U8-12",
    "18": "U10-12",
}

RESULTARRAY = []

# Константа - индекс семейства
FAMILYINDEX = 0
USEDROW = 0

# Дизъюнкция
def logicOr(A, B):
    result = []
    for i in range(len(A)):
        if A[i] + B[i] > 0:
            result.append(1)
        else:
            result.append(0)
    return result


def arrayToString(array):
    term = ''
    for i in range(len(array)):
        term += str(array[i])
    return term


def arrayStripDot(array):
    term = ''
    for i in range(len(array)):
        term += "." + str(array[i])
    return term


def zeroCheck(row, zeroIndex):
    k = 0

    for i in range(zeroIndex, len(row)):
        if row[i] == 0:
            k += 1
            return i

    for i in range(len(row)):
        if row[i] == 1:
            k += 1

    if k == 18:
        return True
    else:
        return False


def loop(family, zeroIndex):
    result = logicOr(matrix[USEDROW], matrix[zeroIndex])
    indexForWrite = []
    indexForWrite.append(USEDROW + 1)
    indexForWrite.append(zeroIndex+1)
    print("Записываем дизъюнкцию " + " M" + arrayStripDot(indexForWrite)[:-2]+ " v " + str(indexForWrite[-1]) + " = " + " " * (20 - len(arrayStripDot(indexForWrite))) + arrayToString(result) + " v " + arrayToString(matrix[zeroIndex]),end="")
    print(" = " + arrayToString(result))
    # OUT
    family += ", " + str(zeroIndex + 1)
    while (True):
        ret = zeroCheck(result, zeroIndex)
        if ret == True:
            print("В строке M" + arrayStripDot(indexForWrite) + " все единицы. Построено ψ" + str(len(RESULTARRAY)+1) + " " + family + " }"+'\n')
            return family
        elif ret == False:
            zeros = []
            for i in range(len(result)):
                if result[i] == 0:
                    zeros.append(i+1)
            print("Строки "+ arrayStripDot(indexForWrite)[1:] + " не закроют нули на " + arrayStripDot(zeros)[1:] + " позиции(-ях)" +"\n")
            return False
        else:
            if ret > zeroIndex:
                indexForWrite.append(ret+1)
                print("Записываем дизъюнкцию " + " M" + arrayStripDot(indexForWrite)[:-3] + " v " + str(indexForWrite[-1]) +" = " + " " * (20 - len(arrayStripDot(indexForWrite))) + arrayToString(result) + " v " + arrayToString(matrix[ret]), end='')
                result = logicOr(result, matrix[ret])
                print(" = " + arrayToString(result))
                #OUT
                family += ", " + str(ret + 1)
            else:
                continue


def main(rowIndex):
    zeroIndexs = []

    # OUT
    family =  str(rowIndex + 1)

    for i in range(len(matrix[rowIndex])):
        if matrix[rowIndex][i] == 0 and i > rowIndex:
            zeroIndexs.append(i)

    for j in range(len(zeroIndexs)):
        loopResult = loop(family, zeroIndexs[j])

        if loopResult == False:
            continue
        else:
            #loopResult += " }"
            RESULTARRAY.append(loopResult)


for i in range(len(matrix)):
    main(i)
    USEDROW += 1

for i in range(len(RESULTARRAY)):
    print(RESULTARRAY[i])


LASTSET = sorted([7, 9, 10, 15, 16, 1, 6, 14, 18])

INTAR = [
        [1, 6, 14, 15, 18],
        [2, 3, 4, 6, 7, 15, 18],
        [2, 6, 7, 15, 16],
        [2, 7, 10, 15, 16],
        [3, 4, 6, 7, 8, 15, 18],
        [4, 5, 6, 7, 8, 15, 18],
        [6, 7, 8, 9, 15],
        [6, 9, 14, 15],
        [7, 8, 9, 10, 15],
        [7, 9, 10, 15, 16],
        [8, 9, 10, 11, 15],
        [9, 10, 11, 12, 15],
        [9, 12, 14, 15],
        [10, 11, 12, 13, 15, 18],
        [10, 13, 15, 16],
        [12, 13, 14, 15, 18]]

for i in range(len(INTAR)):
    for g in range(len(INTAR[i])):
        if INTAR[i][g] in LASTSET:
            INTAR[i][g] = 0

#for i in range(len(INTAR)):
    #print(" ψ " + str(i+1) + RESULTARRAY[i] + "\n")
    #print(str(INTAR[i]) + "\n")



#ENDRESULT = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*11

for i in range(len(INTAR)-1):
    print(str('0,'*(i+1)), end='')
    for j in range(i+1,len(INTAR)):
        A = set(INTAR[i])
        B = set(INTAR[j])
        #ENDRESULT[i][j] = len(A)+len(B)-len(A.intersection(B))
        #print(str(len(A)+len(B)-len(A.intersection(B)))+",",end='')
    #print()


shit =  [[2, 3, 4],
        [2],
        [3, 4,8],
        [4, 5,8],
        [8],
        [8,11],
        [11, 12],
        [12],
        [11, 12, 13],
        [13],
        [12, 13]]

for i in range(len(shit)-1):
    print(str('0,'*(i+1)), end='')
    for j in range(i+1,len(shit)):
        A = set(shit[i])
        B = set(shit[j])
        #ENDRESULT[i][j] = len(A)+len(B)-len(A.intersection(B))
        #print(str(len(A)+len(B)-len(A.intersection(B)))+",",end='')
    #print()