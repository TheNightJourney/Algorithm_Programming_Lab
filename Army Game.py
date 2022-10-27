def armygame(x,y):
    cells = x//2
    rows = y//2
    return (x-cells)*(y-rows)

print("Output: ",armygame(1242,2144))