
# # example 1
sample_file = './sample_files/list_of_cities_with_tab.txt'

with open(sample_file, 'r') as f:
    cities = f.readlines()
    cities_without_tab = cities.rstrip('\t')
print(cities_without_tab)

# with open(sample_file, 'r') as f:
#     cities = f.read()
#     cities_without_tab = cities.split('\t')
# print(cities_without_tab)

