def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path) as f:
        for line in f:
            x = line.replace('\n','').replace('\"','').split(',')
            x = [int(i) if i.isdigit() else i for i in x]
            matrix.append(x)
    return matrix

print(read_csv('test_files/dataset_2.csv'))