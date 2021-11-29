#Implement DFS on 2D array

def DFS(matrix):
    height = len(matrix)
    length = len(matrix[0])
    #create bool array to keep track of visited nodes
    visited = [[False for col in row] for row in matrix]

    node_stack = [[0,0]]

    while len(node_stack):

        current_node = node_stack.pop()
        row = current_node[0]
        col = current_node[1]

        if not visited[row][col]:
            visited[row][col] = True

            #check left of current node
            if col > 0 and not visited[row][col - 1]:
                node_stack.append([row, col - 1])
            #check right of current node
            if col < length - 1 and not visited[row][col + 1]:
                node_stack.append([row, col + 1])
            #check above current node
            if row > 0 and not visited[row - 1][col]:
                node_stack.append([row - 1, col])
            #check below current node
            if row < height - 1 and not visited[row + 1][col]:
                node_stack.append([row + 1, col])
            
            print(matrix[row][col])

two_dimensional_array = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
]

DFS(two_dimensional_array)