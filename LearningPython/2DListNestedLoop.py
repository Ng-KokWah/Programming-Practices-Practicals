number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# To print each row just use
# for rows in number_grid:
# print(row)

print(number_grid[0][1])

for row in range(len(number_grid)):
    for column in range(len(number_grid[row])):
        print(number_grid[row][column])

# Alternative Way
for rows in number_grid:
    for col in rows:
        print(col)
