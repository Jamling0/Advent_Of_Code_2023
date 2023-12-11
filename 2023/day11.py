def preprocess():
    universe = open('aocd11.txt', 'r').read().split('\n')
    universe = [[*_] for _ in universe]

    return universe


def matrix_ext(matrix, row_pop, col_pop):

    row = 0
    while row < len(row_pop):
        if row_pop[row] == 0:
            matrix.insert(row, ['.' for _ in matrix[0]])
            row_pop.insert(row, 0)
            row += 1
        row += 1

    col = 0
    while col < len(col_pop):
        if col_pop[col] == 0:
            for i in range(len(matrix)):
                matrix[i].insert(col, '.')
            col_pop.insert(col, 1)
            col += 1
        col += 1

    return matrix


def stupid_matrix_ext(matrix, row_pop, col_pop):

    row = 0
    while row < len(row_pop):
        if row_pop[row] == 0:
            for c in range(10 ** 6):
                matrix.insert(row, ['.' for _ in matrix[0]])
                row_pop.insert(row, 0)
                row += 1
        row += 1

    col = 0
    while col < len(col_pop):
        if col_pop[col] == 0:
            for c in range(10 ** 6):
                for i in range(len(matrix)):
                    matrix[i].insert(col, '.')
                col_pop.insert(col, 1)
                col += 1
        col += 1

    return matrix


def visualiser(matrix, output_file):
    file = open(output_file, 'w')
    for _ in matrix:
        for i in _:
            file.writelines(i)
        file.writelines('\n')


def shortest_path(coord_s, coord_d):
    return abs(coord_s[0] - coord_d[0]) + abs(coord_s[1] - coord_d[1])


def pt1():
    universe = preprocess()

    # galaxies = []
    rows_popped = [0] * len(universe)
    cols_popped = [0] * len(universe[0])
    for x in range(len(universe)):
        for y in range(len(universe[x])):
            if universe[x][y] == '#':
                rows_popped[x] = 1
                cols_popped[y] = 1
                # galaxies.append([x, y])

    visualiser(universe, 'output0.txt')

    universe = matrix_ext(universe, row_pop=rows_popped, col_pop=cols_popped)

    galaxies = []
    for x in range(len(universe)):
        for y in range(len(universe[x])):
            if universe[x][y] == '#':
                galaxies.append([x, y])

    visualiser(universe, 'output.txt')

    shortest_paths = []
    galaxies_paired = [[] for _ in galaxies]
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if j not in galaxies_paired[i] and i not in galaxies_paired[j] and i != j:
                shortest_paths.append(abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]))
                galaxies_paired[i].append(j)

    return sum(shortest_paths)


def pt2():
    universe = preprocess()

    galaxies = []
    rows_popped = [0] * len(universe)
    cols_popped = [0] * len(universe[0])
    for x in range(len(universe)):
        for y in range(len(universe[x])):
            if universe[x][y] == '#':
                rows_popped[x] = 1
                cols_popped[y] = 1
                galaxies.append([x, y])

    shortest_paths = []
    galaxies_paired = [[] for _ in galaxies]
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if j not in galaxies_paired[i] and i not in galaxies_paired[j] and i != j:
                increment = 0
                for row in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
                    if rows_popped[row] == 0:
                        increment += 999999

                for col in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
                    if cols_popped[col] == 0:
                        increment += 999999
                shortest_paths.append(abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + increment)
                galaxies_paired[i].append(j)

    return sum(shortest_paths)


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())
