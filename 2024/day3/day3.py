import re


def day3_p1():
    file = open("aocd3_input.txt", 'r')  # open('aocd2_input.txt', 'r')
    data = file.read()

    muls = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))", data)

    muls_sum = 0

    for i in muls:
        i = i.replace("mul(", "")
        i = i.replace(")", "")
        i = list(map(int, i.split(',')))
        muls_sum += i[0] * i[1]

    return muls_sum


def day3_p2():
    file = open("aocd3_input.txt", 'r')  # open('aocd2_input.txt', 'r')
    data = file.read()

    muls = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\))", data)
    muls_new = []

    for i in range(len(muls)):
        for j in range(len(muls[i])):
            if muls[i][j] != "":
                muls_new.append(muls[i][j])

    do = True

    muls_sum = 0

    for i in muls_new:
        if do and len(i) > 7:
            i = i.replace("mul(", "")
            i = i.replace(")", "")
            i = list(map(int, i.split(',')))
            muls_sum += i[0] * i[1]
        elif len(i) == 4:
            do = True
        elif len(i) == 7:
            do = False

    return muls_sum

if __name__ == '__main__':
    print(day3_p1())
    print(day3_p2())



