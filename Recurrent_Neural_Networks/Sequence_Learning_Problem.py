from numpy import array


def generate_sequence(length):
    return array([i/float(length)for i in range(length)])


if __name__ == '__main__':
    print(generate_sequence(10))