def preprocess():
    file = open('adventofcode.com_2022_day_4_input.txt', 'r')
    # file = open('test.txt', 'r')
    data = file.read()
    d_list = data.split()

    for i in range(len(d_list)):
        d_list[i] = d_list[i].split(',')

    for i in range(len(d_list)):
        for j in range(len(d_list[i])):
            d_list[i][j] = d_list[i][j].split('-')

    for i in range(len(d_list)):
        for j in range(len(d_list[i])):
            # d_list[i][j] = range(int(d_list[i][j][0]), int(d_list[i][j][1])+1)
            for k in range(len(d_list[i][j])):
                d_list[i][j][k] = int(d_list[i][j][k])

    return d_list


def pt_1():
    ass = preprocess()

    pair = 0

    for i in range(len(ass)):
        hsi = ass[i].index(max(ass[i]))
        lsi = ass[i].index(min(ass[i]))
        if (ass[i][hsi][0] >= ass[i][lsi][0]) and (ass[i][hsi][1] <= ass[i][lsi][1]):
            pair += 1
        elif ass[i][0][0] == ass[i][1][0]:
            pair += 1

    return pair


def pt_2():
    ass = preprocess()

    pair = 0

    for i in range(len(ass)):
        range_0 = range(ass[i][0][0], ass[i][0][1] + 1)
        range_1 = range(ass[i][1][0], ass[i][1][1] + 1)
        if ass[i][0][0] in range_1 or ass[i][0][1] in range_1:
            pair += 1
        elif ass[i][1][0] in range_0 or ass[i][1][1] in range_0:
            pair += 1

    return pair



if __name__ == '__main__':
    print(pt_1())

    print(pt_2())