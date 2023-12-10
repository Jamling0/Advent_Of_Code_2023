def preprocess():
    maze = open('aocd10.txt', 'r').read().split('\n')
    maze = [[*_] for _ in maze]

    return maze


def pt1():
    maze = preprocess()

    # finding S
    loop = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                loop.append([i, j])

    direct = None
    up_down = []
    # checking above the S
    if loop[-1][0] != 0:
        if maze[loop[-1][0] - 1][loop[-1][1]] == '|':
            loop.append([loop[-1][0] - 1, loop[-1][1]])
            direct = 'N'
            up_down.append(1)
        elif maze[loop[-1][0] - 1][loop[-1][1]] == 'F':
            loop.append([loop[-1][0] - 1, loop[-1][1]])
            direct = 'E'
            up_down.append(1)
        elif maze[loop[-1][0] - 1][loop[-1][1]] == '7':
            loop.append([loop[-1][0] - 1, loop[-1][1]])
            direct = 'W'
            up_down.append(1)

    # checking below the S
    if loop[-1][0] != len(maze) and direct is None:
        if maze[loop[-1][0] + 1][loop[-1][1]] == '|':
            loop.append([loop[-1][0] + 1, loop[-1][1]])
            direct = 'S'
            up_down.append(-1)
        elif maze[loop[-1][0] + 1][loop[-1][1]] == 'L':
            loop.append([loop[-1][0] - 1, loop[-1][1]])
            direct = 'E'
            up_down.append(-1)
        elif maze[loop[-1][0] + 1][loop[-1][1]] == 'J':
            loop.append([loop[-1][0] + 1, loop[-1][1]])
            direct = 'W'
            up_down.append(-1)

    # checking left of S
    if loop[-1][1] != 0 and direct is None:
        if maze[loop[-1][0]][loop[-1][1] - 1] == '-':
            loop.append([loop[-1][0], loop[-1][1] - 1])
            direct = 'W'
            up_down.append(0)
        elif maze[loop[-1][0]][loop[-1][1] - 1] == 'L':
            loop.append([loop[-1][0], loop[-1][1] - 1])
            direct = 'N'
            up_down.append(1)
        elif maze[loop[-1][0]][loop[-1][1] - 1] == 'F':
            loop.append([loop[-1][0], loop[-1][1] - 1])
            direct = 'S'
            up_down.append(-1)

    # checking right of S
    if loop[-1][1] != len(maze[0]) and direct is None:
        if maze[loop[-1][0]][loop[-1][1] + 1] == '-':
            loop.append([loop[-1][0], loop[-1][1] + 1])
            direct = 'E'
            up_down.append(0)
        elif maze[loop[-1][0]][loop[-1][1] - 1] == 'J':
            loop.append([loop[-1][0], loop[-1][1] + 1])
            direct = 'N'
            up_down.append(1)
        elif maze[loop[-1][0]][loop[-1][1] - 1] == '7':
            loop.append([loop[-1][0], loop[-1][1] + 1])
            direct = 'S'
            up_down.append(-1)

    # following loop
    while loop[-1] != loop[0]:
        if direct == 'N':
            loop.append([loop[-1][0] - 1, loop[-1][1]])
            if maze[loop[-1][0]][loop[-1][1]] == '|':
                direct = 'N'
                up_down.append(1)
            elif maze[loop[-1][0]][loop[-1][1]] == 'F':
                direct = 'E'
                up_down.append(1)
            elif maze[loop[-1][0]][loop[-1][1]] == '7':
                direct = 'W'
                up_down.append(1)
            else:
                break
        elif direct == 'S':
            loop.append([loop[-1][0] + 1, loop[-1][1]])
            if maze[loop[-1][0]][loop[-1][1]] == '|':
                direct = 'S'
                up_down.append(-1)
            elif maze[loop[-1][0]][loop[-1][1]] == 'L':
                direct = 'E'
                up_down.append(-1)
            elif maze[loop[-1][0]][loop[-1][1]] == 'J':
                direct = 'W'
                up_down.append(-1)
            else:
                break
        elif direct == 'E':
            loop.append([loop[-1][0], loop[-1][1] + 1])
            if maze[loop[-1][0]][loop[-1][1]] == '-':
                direct = 'E'
                up_down.append(0)
            elif maze[loop[-1][0]][loop[-1][1]] == 'J':
                direct = 'N'
                up_down.append(1)
            elif maze[loop[-1][0]][loop[-1][1]] == '7':
                direct = 'S'
                up_down.append(-1)
            else:
                break
        elif direct == 'W':
            loop.append([loop[-1][0], loop[-1][1] - 1])
            if maze[loop[-1][0]][loop[-1][1]] == '-':
                direct = 'W'
                up_down.append(0)
            elif maze[loop[-1][0]][loop[-1][1]] == 'L':
                direct = 'N'
                up_down.append(1)
            elif maze[loop[-1][0]][loop[-1][1]] == 'F':
                direct = 'S'
                up_down.append(-1)
            else:
                break

    return (len(loop) // 2), loop, up_down


def pt2():
    maze = preprocess()

    _, loop, up_down = pt1()

    # if S = J
    up_down.insert(0, 1)
    up_down.append(1)

    # if S = F
    # up_down.insert(0, -1)
    # up_down.append(-1)

    # if S = 7
    # up_down.insert(0, -1)
    # up_down.append(-1)

    # if S = L
    # up_down.insert(0, 1)
    # up_down.append(1)

    pairs = {'S': ['|', '7', 'F', 'S'], 'F': ['|', '7', 'F', 'S'], '|': ['|', 'F', 'S'], '7': ['|', '7', 'F', 'S']}

    within_ctr = 0
    count = 0
    waiting_for = 0
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if [x, y] not in loop:
                if within_ctr:
                    count += 1
                    maze[x][y] = '1'
                else:
                    maze[x][y] = '0'
            elif maze[x][y] in pairs:
                if within_ctr:
                    if maze[x][y] in pairs.get(maze[x][y]) and up_down[loop.index([x, y])] == waiting_for:
                        within_ctr = 0
                        waiting_for = 0
                else:
                    if maze[x][y] == 'S':
                        waiting_for = 1
                    else:
                        waiting_for = up_down[loop.index([x, y])] * -1
                    within_ctr = 1

    file = open('output.txt', 'w')
    for _ in maze:
        for i in _:
            file.writelines(i)
        file.writelines('\n')

    return count


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())