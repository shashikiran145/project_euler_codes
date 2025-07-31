# I had no idea how to do this. It is related to dynamic programming (coding concept)
# and optimization problems (math)
# Seems interesting. Should explore more
# The code is mostly taken from other sources. I couldn't figure out how to code efficiently

print("Enter rows of numbers. Press Enter on an empty line to finish:")
matrix = []
while True:
    line = input()
    if line.strip() == "":
        break
    row = list(map(int, line.split()))
    matrix.append(row)
print("\nYou entered:")
triangle = []
#for row in matrix:
    #print(row)


def max_path_sum(triangle):
    # Copy to avoid modifying original
    tri = [row[:] for row in triangle]
    print(tri)

    # Start from second-last row up to the top
    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            tri[row][col] += max(tri[row + 1][col], tri[row + 1][col + 1])

    return tri[0][0]


print("Max path sum:", max_path_sum(matrix))



