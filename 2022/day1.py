def day1():
    file = open('adventofcode.com_2022_day_1_input.txt', 'r')

    data = []
    index = 0
    data.append([])
    for i in file:
        data[index].append(int(i[0:-1]))
        if i == '\n':
            index += 1
            data.append([])
            pass
    print(data)
    pass


if __name__ == '__main__':
    day1()