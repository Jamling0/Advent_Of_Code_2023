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
    file = open("example2.txt", 'r')  # open('aocd2_input.txt', 'r')
    data = file.read()

    muls = re.findall("(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\))", data)

    for i in muls:

        i = i.replace("mul(", "")
        i = i.replace(")", "")
        i = list(map(int, i.split(',')))
        muls_sum += i[0] * i[1]
    print(muls)

if __name__ == '__main__':
    print(day3_p1())
    print(day3_p2())



