from collections import defaultdict, OrderedDict


columns = defaultdict(lambda: defaultdict(int))


def record_character(column, character):
    columns[column][character] += 1


def parse(data):
    """
    Parse the input data.

    @rtype: L{list} of L{str}
    """
    return data.split('\n')[:-1]


def frequent(column):
    """
    Return the most frequently recorded character
    """
    return sorted(column.items(), key=lambda i: i[1], reverse=True)[0][0]


def solve_a(data):
    """
    Solve the first part of the challenge
    """
    for line in data:
        for column, char in enumerate(line):
            record_character(column, char)

    output = [frequent(column) for k, column in columns.items()]
    return ''.join(output)


if __name__ == '__main__':
    with open('day_6.txt') as f:
        _input = f.read()
    data = parse(_input)

    print solve_a(data)
