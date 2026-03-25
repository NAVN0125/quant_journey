def data_loader(file_path):
    data = []
    with open(file_path, 'r') as f:
        next(f)
        for line in f:
            data.append(line.strip().split(',')[4])

    return data
            
        