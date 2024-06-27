#this function is defined to multiply two matrices

def multiplyMatrix(matrix1,matrix2) -> list:
    if len(matrix1) == len(matrix2[0]):
        matrix3 = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix1))]
        
        for i in range(len(matrix1)):
            for j in range(len(matrix3)):
                for k in range(len(matrix2)):
                    matrix3[i][j] += matrix1[i][j]*matrix2[k][i]
        
        return matrix3
    else:
        return None
    


matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,2,3],
    [4,5,6]
]


result = multiplyMatrix(matrix1,matrix2)

if result is not None:
    for row in result:
        for element in row:
            print(element, end=' ')
        print()
else:
    print('Rows of matrix1 is not equal to columns of Matrix2')

        