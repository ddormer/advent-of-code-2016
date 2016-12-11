from collections import defaultdict



def parse(data):
    """
    Parse the input data.

    @rtype: L{list} of L{str}
    """
    return data.split('\n')[:-1]


def record_characters(data):
    """
    Record the frequency of characters in each column.
    """
    columns = defaultdict(lambda: defaultdict(int))
    for line in data:
        for column, char in enumerate(line):
            columns[column][char] += 1
    return columns


def most_frequent(column):
    """
    Return the most frequently recorded character
    """
    return sorted(column.items(), key=lambda i: i[1], reverse=True)[0][0]


def least_frequent(column):
    """
    Return the least frequently recorded character
    """
    return sorted(column.items(), key=lambda i: i[1], reverse=False)[0][0]


def solve_a(data):
    """
    Solve the first part of the challenge
    """
    columns = record_characters(data)
    output = [most_frequent(column) for k, column in columns.items()]
    return ''.join(output)


def solve_b(data):
    """
    Solve the second part of the challenge
    """
    columns = record_characters(data)
    output = [least_frequent(column) for k, column in columns.items()]
    return ''.join(output)


if __name__ == '__main__':
    with open('day_6.txt') as f:
        _input = f.read()
    data = parse(_input)
    print solve_a(data)
    print solve_b(data)
