def pre_process():
    # pre-processing:
    file = open('adventofcode.com_2022_day_2_input.txt', 'r')
    data = file.read()
    rps = data.split('\n')

    for i in range(len(rps)):
        rps[i] = rps[i].split(' ')

    return rps


def pt_1():
    rps = pre_process()

    # scoring:
    score = 0

    for i in range(len(rps)):
        # rock
        if rps[i][1] == 'X':
            score += 1
            # tie
            if rps[i][0] == 'A':
                score += 3
            # win
            elif rps[i][0] == 'C':
                score += 6
        # paper
        elif rps[i][1] == 'Y':
            score += 2
            # tie
            if rps[i][0] == 'B':
                score += 3
            # win
            elif rps[i][0] == 'A':
                score += 6
        # scissors
        else:
            score += 3
            # tie
            if rps[i][0] == 'C':
                score += 3
            elif rps[i][0] == 'B':
                score += 6

    return score


def pt_2():
    test_rps = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]

    rps = pre_process()

    possible_actions = {
        "['A', 'X']": 3,
        "['A', 'Y']": 4,
        "['A', 'Z']": 8,
        "['B', 'X']": 1,
        "['B', 'Y']": 5,
        "['B', 'Z']": 9,
        "['C', 'X']": 2,
        "['C', 'Y']": 6,
        "['C', 'Z']": 7
    }

    score = 0
    for i in rps:
        score += possible_actions.get(str(i))

    return score


if __name__ == '__main__':
    print(pt_1())

    print(pt_2())
