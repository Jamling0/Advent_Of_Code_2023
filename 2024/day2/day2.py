def preprocess():
    file = open("aocd2_input.txt", 'r')# open('aocd2_input.txt', 'r')
    data = file.read()

    data = [list(map(int, i.split(' '))) for i in data.split('\n')]

    return data


def day2_p1():
    data = preprocess()

    ctr = 0

    for i in data:
        safe = True
        if i[0] > i[-1]: # then decreasing
            for j in range(1, len(i)):
                calc = i[j] - i[j-1]
                if calc > -1 or calc < -3:
                    safe = False
                    break
        else:
            for j in range(1, len(i)):
                calc = i[j] - i[j - 1]
                if calc < 1 or calc > 3:
                    safe = False
                    break
        if safe:
            ctr += 1

    return ctr


def day2_p2():
    data = preprocess()

    ctr = 0
    unsafe_reports = []

    for i in data:
        safe = True
        if i[0] > i[-1]:  # then decreasing
            for j in range(1, len(i)):
                calc = i[j] - i[j - 1]
                if calc > -1 or calc < -3:
                    safe = False
                    i_copy = i[:]
                    i.pop(j-1)
                    i_copy.pop(j)
                    unsafe_reports.append(i)
                    unsafe_reports.append(i_copy)
                    break
        else:
            for j in range(1, len(i)):
                calc = i[j] - i[j - 1]
                if calc < 1 or calc > 3:
                    safe = False
                    i_copy = i[:]
                    i.pop(j - 1)
                    i_copy.pop(j)
                    unsafe_reports.append(i)
                    unsafe_reports.append(i_copy)
                    break
        if safe:
            ctr += 1

    skip = False

    for i in range(len(unsafe_reports)):
        if not skip:
            safe = True
            if unsafe_reports[i][0] > unsafe_reports[i][-1]:  # then decreasing
                for j in range(1, len(unsafe_reports[i])):
                    calc = unsafe_reports[i][j] - unsafe_reports[i][j - 1]
                    if calc > -1 or calc < -3:
                        safe = False
                        break
            else:
                for j in range(1, len(unsafe_reports[i])):
                    calc = unsafe_reports[i][j] - unsafe_reports[i][j - 1]
                    if calc < 1 or calc > 3:
                        safe = False
                        break
            if safe:
                if i % 2 == 0:
                    skip = True
                ctr += 1
        else:
            skip = False

    return ctr

if __name__ == "__main__":
    preprocess()
    print(day2_p1())
    print(day2_p2())
