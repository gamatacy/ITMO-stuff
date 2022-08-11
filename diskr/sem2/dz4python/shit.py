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


def zeros(row, zeroIndex):
    zero = []
    for i in range(len(row)):
        if row[i] == 0 and i >= zeroIndex:
            zero.append(i)
    return zero

def logicOr(A, B):
    result = []
    for i in range(len(A)):
        if A[i] + B[i] > 0:
            result.append(1)
        else:
            result.append(0)
    return result

resultArray = []

for i in range(len(matrix)):
    ij1 = zeros(matrix[i],i+1)
    #print("IJ1 ",end='')
    #print(ij1)


    for j in range(len(ij1)):
        result = matrix[i]
        bufferArray = []
        flag = False
        CONSTresult = logicOr(result, matrix[ij1[j]])
        result = CONSTresult
        bufferArray.append(i)
        bufferArray.append(ij1[j])
        ij2 = zeros(result, ij1[j])
        if result.count(0) == 0:
            resultArray.append(bufferArray)
            break
        #print(ij2)
        for g in range(len(ij2)):
            if result[ij2[g]] == 0:
                result = logicOr(result, matrix[ij2[g]])
                bufferArray.append(ij2[g])
            if result.count(0) == 0:
                resultArray.append(bufferArray)
                bufferArray = []
                bufferArray.append(i)
                bufferArray.append(ij1[j])
                result = CONSTresult

for i in range(len(resultArray)):
    for j in range(len(resultArray[i])):
        resultArray[i][j] += 1
        #resultArray[i][j] = keys[str(resultArray[i][j])]
    print(resultArray[i])


'''
for i in range(len(resultArray)):
    print(" ψ" + str(i+1) + " = { ",end='')
    for j in range(len(resultArray[i])):
        print(keys[str(resultArray[i][j])] + ", ", end='')
    print(" }")
'''

INTAR = [[1, 6, 14, 15, 18],
    [1,6,17,18],
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
    [12, 13, 14, 15, 18]
]

resultInts = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*17


for i in range(len(INTAR)-1):
    print(str('0,'*(i+1)), end='')
    for j in range(i+1,len(INTAR)):
        A = set(INTAR[i])
        B = set(INTAR[j])
        resultInts[i][j] = len(A)+len(B)-len(A.intersection(B))
        print(str(len(A)+len(B)-len(A.intersection(B)))+",",end='')
    print()