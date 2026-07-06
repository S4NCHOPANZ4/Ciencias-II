v = 5 
e = 7

matrix = [[0 for _ in range(e)] for _ in range(v)]


def addRelation(matrix, edge, vertfrom, vertTo):
    matrix[vertfrom][edge] = 1
    matrix[vertTo][edge] = -1
    return

nodes = [(0,1), (1,2), (2,3), (3,4), (2,4), (0,3), (4,0)]

for i in range(len(nodes)):
    addRelation(matrix,i,nodes[i][0], nodes[i][1])



def printMatrix(matrix):
    for i in matrix:
        print(i,"\n")

printMatrix(matrix)