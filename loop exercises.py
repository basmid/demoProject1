'''
Problem 8
Given the list 'collection' print every single word in the list. The list contains another list that contains words. Print all
of the words.
'''

#for item in collection:
#    print(item)

print('\n')
print("***** Starting Problem 8 ********")

collection = ['python', 'qa', 'selenium', ['java', 'ruby', 'pearl', 'c++'], 'dell', 'toshiba' ]

for i in collection:
    if type(i) == list:
        for j in i:
            print(j)

    else:
        print("test")

