def preprocess():
    file = open('test.txt', 'r')
    data = file.read()
    d_list = data.split('\n')

    dirs = {}
    for i in range(len(d_list)):
        if d_list[i] == '$ ls':
            dirs.set()

    return d_list


if __name__ == '__main__':
    print(preprocess())
