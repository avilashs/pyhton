# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# step 1 :
#     if matrix is not there return 0 
# step 2 :
#     init counter to 0 
# step 3: 
#     loop through the matrix
# step 4: 
#     if val =0:
#         check if there are adjacent 1's 
#         mark those one's to some other value 
# step 5: 
#     continue for these adjacent position
def numIslands(arr):
        def searchIsland(i,j,grid):
            if (
        i < 0 or j < 0 or 
        i >= len(grid) or j >= len(grid[0]) or 
        grid[i][j] != '1'
       ):
                return
    
    
        searchIsland(i+1,j,grid)
        searchIsland(i-1,j,grid)
        searchIsland(i,j+1,grid)
        searchIsland(i,j-1,grid)

    if not arr:
        return 0
    for i in range(0,len(arr)):
        for j in range(len(grid[0])):
            if arr[i][j] == '1':
                #dfs(grid,i,j)
                searchIsland(i,j,arr)
                cnt += 1
    grid[i][j] = '9999'    
    return cnt;






grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(grid));
