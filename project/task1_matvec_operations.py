from math import sqrt, acos, degrees


#1.vector[]

#return dot product of 2 vectors
def scalar_product(x,y):
    if len(x)!=len(y):
        raise ValueError("error: vector lengths are different")
    
    total=0
    for i in range(len(x)):
        total+=(x[i]*y[i])

    return(total)
#print(scalar_product([1,2],[1,5]))

#returns vector length
def vector_length(x):
    total=0
    for i in range(len(x)):
        total+=(x[i])**2
    ans=sqrt(total)
    return(ans)
#print(vector_length([3,4]))

# returns angle between vectors in degrees
def angle(x,y):
    return(degrees(acos(scalar_product(x,y)/(vector_length(x)*vector_length(y)))))
#print('angle:',angle([0,1],[1,0]))


#2.matrix[ [][]...[] ]

def matrix_addition(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        raise ValueError('error: matrices should be same dimensional')

    result_m=[[0]*len(A[0]) for i in range(len(A))]
    for i in range (len(A)):
        for j in range (len(A[0])):
            result_m[i][j]=A[i][j]+B[i][j]
    return(result_m)

# A = [[1, 1, 1],
#      [4, 5, 6]]

# B = [[1, 1, 1],
#      [4, 5, 6]]

# result = matrix_addition(A, B)

# for row in result:
#     print(row)


def matrix_multiplication(A, B):
    if len(A[0])!=len(B):
        raise ValueError('error:matrices cannot be multiplied')
    
    rm_rows=len(A)
    rm_cols=len(B[0])
    result_m=[[0] * rm_cols for i in range(rm_rows)]


    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result_m[i][j]+=A[i][k]*B[k][j]


    return(result_m)

# A = [[1, 1, 1],
#      [4, 5, 6]]

# B = [[1, 8],
#      [1, 10],
#      [1, 12]]

# result = matrix_multiplication(A, B)

# for row in result:
#     print(row)

def matrix_transpose(A):
    rows=len(A)
    cols=len(A[0])

    result_m=[[0]*rows for i in range(cols)]

    for i in range(len(A[0])):
        for j in range (len(A)):
            result_m[i][j]=A[j][i]
    return(result_m)

# B = [[1, 8],
#      [1, 10],
#      [1, 12]]

# result = matrix_transpose(B)

# for row in result:
#     print(row)