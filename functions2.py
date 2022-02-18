'''
def get_full_name(f_name, l_name="James"):
    if not l_name:
        l_name = ""

    full_name = f_name + " " + l_name
    return full_name

full_n = get_full_name("Bart","Jansen")
print(full_n)

full_n = get_full_name("Bart",l_name="bob")
print(full_n)

full_n = get_full_name(f_name="Bart",l_name="bob")
print(full_n)
'''

#Example 2
def calculate_area(width=0, height=0):
    if not width or not height:
        raise ValueError("Width and height can not be 0")
    area = width * height

    return area

print(calculate_area(4,2))
print(calculate_area(4))