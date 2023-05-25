from collections import deque

print("Island Pattern")

island1 = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

island2 = [
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]


def printIsland(island):
    for i in range(len(island)):
        for j in range(len(island[i])):
            print(island[i][j], end=" ")
        print()

def countNumberOfIsland(matrix):
    totalIslands = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if (matrix[i][j] == 1):
                # expand and count connected islands/1
                # matrix is mutated i.e 1-> 0 after being couted as a part # of other island. 
                # Here, we can perform DFS or BFS to find its all connected land cells.  
                totalIslands +=1
                visitBFS(i,j,matrix)
    return totalIslands

def visitDFS(row,col,matrix):
    #return if it is invalid cell
    if (row < 0 or row >= len(matrix)
        or col < 0 or col >= len(matrix[0])):
        return #base case 1

    if (matrix[row][col] == 0):
        return #base case 2
    #mark the current cell visited
    matrix[row][col] = 0

    #recursively visit all neighboring cells
    visitDFS(row+1,col,matrix) #bottom cell
    visitDFS(row-1,col,matrix) #upper cell
    visitDFS(row,col+1,matrix)
    visitDFS(row,col-1,matrix)

def visitBFS(row,col,matrix):
    neighbors = deque([(row,col)])
    while neighbors:
        currentRow, currentCol = neighbors.popleft()
        #not valid cell
        if (currentRow < 0 or currentRow >= len(matrix) or currentCol < 0 or 
            currentCol >= len(matrix[0])):
            return 
        if (matrix[currentRow][currentCol] == 0):
            return
        matrix[currentRow][currentCol] = 0

        visitBFS(currentRow+1,currentCol,matrix)
        visitBFS(currentRow-1,currentCol,matrix)
        visitBFS(currentRow,currentCol+1,matrix)
        visitBFS(currentRow,currentCol-1,matrix)

def biggestIsland(row,col,matrix):
    



if __name__ == "__main__":
    print(countNumberOfIsland(island1))
    print(countNumberOfIsland(island2))

    # Q1. Number of Islands (easy)
