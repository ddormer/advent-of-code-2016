from hashlib import md5



input_data = 'cxdnnyjw'



def solve_a():
    generated = []
    index = 0
    while True:
        m = md5(input_data + str(index))
        number = m.hexdigest()
        if number[0:5] == '00000':
            generated.append(number[5])
        if len(generated) >= 8:
            break
        index += 1
    return ''.join(generated)



def solve_b():
    generated = {}
    index = 0
    while len(generated) < 8:
        digest = md5(input_data + str(index)).hexdigest()
        pointer = digest[5]
        key = digest[6]
        if digest[0:5] == '00000':
            if pointer in map(str, range(0, 8)):
                if generated.get(pointer, None) is None:
                    generated[pointer] = key
        index += 1
    return ''.join([v for _, v in sorted(generated.items(), key=lambda x: x[0])])


print solve_a()
print solve_b()
