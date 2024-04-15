def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


file_path = 'duzy_plik.txt'
lines_generator = read_large_file(file_path)
for line in lines_generator:
    print(line)