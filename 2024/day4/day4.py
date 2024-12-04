from operator import countOf


def preprocess():
    file = open("aocd4_input.txt", 'r')  # open('aocd4_input.txt', 'r')
    data = file.read().split()

    return data

def hori_right(two_d_data, row, col):
    is_found = False

    if two_d_data[row][col + 1] == 'M':  # l->r hori
        if two_d_data[row][col + 2] == 'A':
            if two_d_data[row][col + 3] == 'S':
                is_found = True

    return is_found

def diagonal_bot_right(two_d_data, row, col):
    is_found = False

    if two_d_data[row + 1][col + 1] == 'M':  # bot right diag
        if two_d_data[row + 2][col + 2] == 'A':
            if two_d_data[row + 3][col + 3] == 'S':
                is_found = True

    return is_found

def vert_down(two_d_data, row, col):
    is_found = False

    if two_d_data[row + 1][col] == 'M':  # l->r hori
        if two_d_data[row + 2][col] == 'A':
            if two_d_data[row + 3][col] == 'S':
                is_found = True

    return is_found

def diagonal_bot_left(two_d_data, row, col):
    is_found = False

    if two_d_data[row + 1][col - 1] == 'M':  # bot right diag
        if two_d_data[row + 2][col - 2] == 'A':
            if two_d_data[row + 3][col - 3] == 'S':
                is_found = True

    return is_found

def hori_left(two_d_data, row, col):
    is_found = False

    if two_d_data[row][col - 1] == 'M':  # l->r hori
        if two_d_data[row][col - 2] == 'A':
            if two_d_data[row][col - 3] == 'S':
                is_found = True

    return is_found

def diagonal_top_left(two_d_data, row, col):
    is_found = False

    if two_d_data[row - 1][col - 1] == 'M':  # bot right diag
        if two_d_data[row - 2][col - 2] == 'A':
            if two_d_data[row - 3][col - 3] == 'S':
                is_found = True

    return is_found

def vert_up(two_d_data, row, col):
    is_found = False

    if two_d_data[row - 1][col] == 'M':  # l->r hori
        if two_d_data[row - 2][col] == 'A':
            if two_d_data[row - 3][col] == 'S':
                is_found = True

    return is_found

def diagonal_top_right(two_d_data, row, col):
    is_found = False

    if two_d_data[row - 1][col + 1] == 'M':  # bot right diag
        if two_d_data[row - 2][col + 2] == 'A':
            if two_d_data[row - 3][col + 3] == 'S':
                is_found = True

    return is_found

def day4_p1():
    data = preprocess()

    xmas_ctr = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "X":
                if col <= len(data[0]) - 4 and hori_right(data, row, col): # r
                    xmas_ctr += 1
                if col <= len(data[0]) - 4 and row <= len(data) - 4 and diagonal_bot_right(data, row, col): # r d
                    xmas_ctr += 1
                if row <= len(data) - 4 and vert_down(data, row, col): # d
                    xmas_ctr += 1
                if row <= len(data) - 4 and col >= 3 and diagonal_bot_left(data, row, col): # l d
                    xmas_ctr += 1
                if col >= 3 and hori_left(data, row, col): # l
                    xmas_ctr += 1
                if row >= 3 and col >= 3 and diagonal_top_left(data, row, col): # l u
                    xmas_ctr += 1
                if row >= 3 and vert_up(data, row, col): # u
                    xmas_ctr += 1
                if row >= 3 and col <= len(data[0]) - 4 and diagonal_top_right(data, row, col): # r u
                    xmas_ctr += 1

    return xmas_ctr

def d_r_xmas(two_d_data, row, col):
    is_found = False

    if two_d_data[row + 1][col + 1] == 'A':
        if two_d_data[row + 2][col + 2] == 'S':
            is_found = True

    return is_found

def d_l_xmas(two_d_data, row, col):
    is_found = False

    if two_d_data[row + 1][col - 1] == 'A':
        if two_d_data[row + 2][col - 2] == 'S':
            is_found = True

    return is_found

def u_l_xmas(two_d_data, row, col):
    is_found = False

    if two_d_data[row - 1][col - 1] == 'A':
        if two_d_data[row - 2][col - 2] == 'S':
            is_found = True

    return is_found

def u_r_xmas(two_d_data, row, col):
    is_found = False

    if two_d_data[row - 1][col + 1] == 'A':
        if two_d_data[row - 2][col + 2] == 'S':
            is_found = True

    return is_found

def day4_p2():
    data = preprocess()

    xmas_ctr = 0
    a_coord_lst = []

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "M":
                if col <= len(data[0]) - 3 and row <= len(data) - 3 and d_r_xmas(data, row, col): # d r
                    a_coord_lst.append((row + 1,col + 1))
                if row <= len(data) - 3 and col >= 2 and d_l_xmas(data, row, col): # d l
                    a_coord_lst.append((row + 1,col - 1))
                if row >= 2 and col >= 2 and u_l_xmas(data, row, col): # u l
                    a_coord_lst.append((row - 1,col - 1))
                if row >= 2 and col <= len(data[0]) - 3 and u_r_xmas(data, row, col): # u r
                    a_coord_lst.append((row - 1,col + 1))


    dupes = dict((i, a_coord_lst.count(i)) for i in a_coord_lst)

    return countOf(dupes.values(), 2)


if __name__ == '__main__':
    print(preprocess())
    print(day4_p1())
    print(day4_p2())