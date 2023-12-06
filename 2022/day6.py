from collections import deque

def preprocess():
    # file = open('test5.txt', 'r')
    file = open('adventofcode.com_2022_day_6_input.txt', 'r')
    data = file.read()
    return data


def pt_1():
    datastream = preprocess()

    buffer = deque(datastream[0:4])
    for i in range(3, len(datastream)):
        if len(buffer) < 4:
            buffer.append(datastream[i])

        if len(buffer) == len(set(buffer)):
            marker = i + 1
            break

        buffer.popleft()

    return marker


def pt_2():
    datastream = preprocess()

    buffer = deque(datastream[0:13])
    for i in range(3, len(datastream)):
        if len(buffer) < 14:
            buffer.append(datastream[i])

        if len(buffer) == len(set(buffer)):
            marker = i + 1
            break

        buffer.popleft()



    return marker



if __name__ == '__main__':
    print(pt_1())
    print(pt_2())