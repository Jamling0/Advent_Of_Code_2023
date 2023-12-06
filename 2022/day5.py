from collections import deque

def preproccess():
    # file = open('test.txt', 'r')
    file = open('adventofcode.com_2022_day_5_input.txt', 'r')
    data = file.read()
    d_list = data.split('\n')

    for i in range(len(d_list)):
        if d_list[i] == '':
            marker = i
            break

    stacks = d_list[0:(marker-1)]

    moves = d_list[(marker+1)::]

    nums = d_list[marker-1].split(' ')

    no_stacks = len([x for x in nums if x != ''])

    stack_list = [[] for _ in range(no_stacks)]

    for i in range(len(stacks)):
        ctr = 0
        stack_ctr = 0
        for j in range(len(stacks[i])):
            if stacks[i][j] == '[':
                stack_ctr = ctr // 4
            elif stacks[i][j] == ' ':
                ctr += 1
            elif stacks[i][j] == ']':
                ctr += 3
            else:
                stack_list[stack_ctr].append(stacks[i][j])

    s_moves = []
    for i in range(len(moves)):
        s_moves.append([int(s) for s in moves[i].split() if s.isdigit()])

    stack_list = [deque(stack_list[x]) for x in range(len(stack_list))]

    return stack_list, s_moves


def pt_1():
    stacks, moves = preproccess()

    for i in range(len(moves)):
        no_crates = moves[i][0]
        from_stack = moves[i][1] - 1
        to_stack = moves[i][2] - 1

        crates_to_move = deque([])
        for j in range(no_crates):
            crates_to_move.appendleft(stacks[from_stack].popleft())

        for k in crates_to_move:
            stacks[to_stack].appendleft(k)

    answer = []

    for i in stacks:
        answer.append(i.popleft())

    return answer

if __name__ == '__main__':
    preproccess()
    print(pt_1())