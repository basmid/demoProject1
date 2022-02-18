# import csv

#header = ['name', 'area', 'country_code2', 'country_code3']
#data = ['Afghanistan', 652090, 'AF', 'AFG']
# string = "Londen","Parijs","Praag","Madrid"
#
# with open('cities.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

    # write the string
    # writer.writerow(string)

import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in month {row[2]}, in year {row[3]}.')
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')