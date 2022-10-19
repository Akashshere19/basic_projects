'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b'''
'''
b= 60
def f(a,b=b):
    return a+b
b=30
print(f(2)) '''
'''
def minPathSum(self,grid:list[list[int]]):
    for row in range(len(grid)):
               for col in range(len(grid[0])):
                  if row ==0 and col!=0:
                     grid[row][col]+=grid[row][col-1]
                  elif col ==0 and row!=0:
                      grid[row][col]+=grid[row-1][col]
                  elif row !=0 and col!=0:
                      grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
     return grid[row][col] '''                
'''   
grid=[[1,2,3],[4,5,6]]    
for row in range(len(grid)):
               for col in range(len(grid[0])):
                  if row ==0 and col!=0:
                     grid[row][col]+=grid[row][col-1]
                  elif col ==0 and row!=0:
                      grid[row][col]+=grid[row-1][col]
                  elif row !=0 and col!=0:
                      grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
print(grid[row][col])'''



elevation_map = [4,2,0,3,2,5]  
water = 0 
n = len(elevation_map)
lf_max = [0]*n 
rt_max = [0]*n   
lf_max[0] = elevation_map[0]
rt_max[n-1] = elevation_map[n-1]

for i in range(1,n):
   lf_max[i] = max(lf_max[i-1], elevation_map[i])

for i in range(n-2, -1, -1):
    rt_max[i] = max(rt_max[i+1], elevation_map[i])


for i in range(n):
    water += min(lf_max[i],rt_max[i]) - elevation_map[i]
print(water)



#print("Total units of water trapped: ",trapped_water(elevation_map))
