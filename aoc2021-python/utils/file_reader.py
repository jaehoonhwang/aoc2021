def read_file(path):
    ret = []

    with open(path, 'r') as file:
        ret = file.readlines()

    return ret
