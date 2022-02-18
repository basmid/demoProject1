"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""
# num = 0
# list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
# for i in list_of_domains:
#     print(list_of_domains[num])
#     num = num + 1
#
# import random
# import string
# letters = string.ascii_lowercase
# random_string = ''.join(random.choice(letters) for i in range(length))
# count = 0
# while count < 20:
#     random_string = ''.join(random.choice(letters) for i in range(10))
#     print(random_string)
#     count = count + 1
import random
import string
import csv
letters = string.ascii_lowercase

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
count = 0
domain_index = 0
with open('out_generate-random_email_with_list_of_domains_v1_test.csv', mode='w', newline='') as random_email_file:
    random_email_file = csv.writer(random_email_file, delimiter=',')
    while count < 20:
        random_string = ''.join(random.choice(letters) for i in range(10))
        # print(random_string + "@" + list_of_domains[domain_index])
        random_emails = random_string + "@" + list_of_domains[domain_index] + ","
        random_email_file.writerow(random_emails.split(','))
        count = count + 1
        if count == 20:
            domain_index = domain_index + 1
            count = 0
        if domain_index == 5:
            break

        #csvwriter.writerow(JD.split())
        # with open('employee_file.csv', mode='w') as employee_file:
        #     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #
        #     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        #     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])







