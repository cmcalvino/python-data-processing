import csv

def clean_data(file_name):
    cleaned = []
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                cleaned.append(row)
    
    return cleaned
