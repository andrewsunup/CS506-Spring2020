
def read_csv(csv_file_path):
    """
    Given a path to a csv file
    Read data from csv file
    Convert data into its original data type
    return a matrix
    """
    res = []
    with open(csv_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            row = []
            for x in line.split(","):
                row.append(eval(x))
            res.append(row)

    return res

