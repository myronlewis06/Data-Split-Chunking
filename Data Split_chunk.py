import os
import csv

def split_csv_by_rows(input_file, output_folder, rows_per_chunk):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  

        file_number = 1
        rows_written = 0
        output_file = os.path.join(output_folder, f'chunk_{file_number}.csv')
        outfile = open(output_file, 'w', newline='', encoding='utf-8')
        writer = csv.writer(outfile)
        writer.writerow(header)

        for row in reader:
            if rows_written >= rows_per_chunk:
                outfile.close()
                file_number += 1
                output_file = os.path.join(output_folder, f'chunk_{file_number}.csv')
                outfile = open(output_file, 'w', newline='', encoding='utf-8')
                writer = csv.writer(outfile)
                writer.writerow(header)
                rows_written = 0

            writer.writerow(row)
            rows_written += 1

       
        outfile.close()

if __name__ == "__main__":
    input_file = 'C:/Study Material And Projects/CSV Divider/gsearch_jobs.csv'
    output_folder = 'C:/Study Material And Projects/CSV Divider'
    rows_per_chunk = 10000  
    split_csv_by_rows(input_file, output_folder, rows_per_chunk)
