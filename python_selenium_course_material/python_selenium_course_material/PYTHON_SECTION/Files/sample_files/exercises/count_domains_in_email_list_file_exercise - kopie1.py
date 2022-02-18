"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""


# input_file = "count_domains_in_email_list_file_exercise_input.csv"
# output_file = "count_domains_in_email_list_file_exercise_output.json"

import csv
yahoo_count = 0
gmail_count = 0
msn_count = 0
supersqa_count = 0
outlook_count = 0

with open('count_domains_in_email_list_file_exercise_input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        random_email = (row[0])
        domain = random_email.partition("@")[2]
        print(domain)
        if (domain == "yahoo.com"):
            yahoo_count = yahoo_count + 1
        elif (domain == "gmail.com"):
            gmail_count = gmail_count + 1
        elif (domain == "msn.com"):
            msn_count = msn_count + 1
        elif (domain == "supersqa.com"):
            supersqa_count = supersqa_count + 1
        elif (domain == "outlook.com"):
            outlook_count = outlook_count + 1

print(yahoo_count)
print(gmail_count)
print(msn_count)
print(supersqa_count)
print(outlook_count)

{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}
