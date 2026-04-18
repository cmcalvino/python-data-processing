import csv

def clean_data(file_name):
    cleaned = []
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if any(cell.strip() for cell in row):
                cleaned.append(row)
    
    return cleaned
