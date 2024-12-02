def preprocess():
	file = open('aocd1_input.txt', 'r')
	data = file.read()

	data = data.split()

	list1 = []
	list2 = []
	ctr = 0

	for i in data:
		if ctr % 2 == 0:
			list1.append(int(i))
		else:
			list2.append(int(i))
		ctr += 1

	return list1, list2


def day1_p1():
	list1, list2 = preprocess()

	list1.sort()
	list2.sort()

	sum_of_list_diffs = 0

	for i in range(len(list1)):
		sum_of_list_diffs += abs(list1[i] - list2[i])

	return sum_of_list_diffs


def day1_p2():
	list1, list2 = preprocess()

	list1.sort()
	list2.sort()

	sum_of_sim_score = 0

	for i in list1:
		sum_of_sim_score += i * list2.count(i)

	return sum_of_sim_score


if __name__ == '__main__':
	print(day1_p1())
	print(day1_p2())
