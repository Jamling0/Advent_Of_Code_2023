def preprocess():
    file = open('adventofcode.com_2022_day_3_input.txt', 'r')

    data = file.read()

    return data.split('\n')


def pt_1():
    # a = 97
    # A = 65

    rucks = preprocess()
    # rucks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
    #          'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    #          'PmmdzqPrVvPwwTWBwg',
    #          'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    #          'ttgJtRGJQctTZtZT',
    #          'CrZsJsPPZsGzwwsLwLmpwMDw']

    shared_items = []

    for i in range(len(rucks)):
        len_ruck = len(rucks[i])
        comp1 = rucks[i][0:len_ruck//2]
        comp2 = rucks[i][len_ruck//2::]

        for j in comp1:
            if j in comp2:
                shared_items.append(j)
                break

    priorities = 0

    for k in shared_items:
        if k.isupper():
            priorities += ord(k) - 38
        else:
            priorities += ord(k) - 96

    return priorities

def pt_2():
    rucks = preprocess()
    # rucks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
    #          'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    #          'PmmdzqPrVvPwwTWBwg',
    #          'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    #          'ttgJtRGJQctTZtZT',
    #          'CrZsJsPPZsGzwwsLwLmpwMDw']

    elves = []
    elf = []
    for i in range(len(rucks)):
        if (i+1) % 3 == 0:
            elf.append(rucks[i])
            elves.append(elf)
            elf = []
        else:
            elf.append(rucks[i])

    badges = []

    for i in range(len(elves)):
        for j in elves[i][0]:
            if j in elves[i][1] and j in elves[i][2]:
                badges.append(j)
                break

    priorities = 0

    for k in badges:
        if k.isupper():
            priorities += ord(k) - 38
        else:
            priorities += ord(k) - 96

    return priorities


if __name__ == '__main__':
    # print(pt_1())

    print(pt_2())
