import pdb
pdb.set_trace()
def get_user_name(name):
    user_names = {"admas": "ak",
                  "joe": "joe99",
                  "mary": "marryrocks2020"}
    print(f'The user "{user_names[name]}" is logged in.')

    return user_names[name]

user_1 = get_user_name("admas")
print("User 1: " + user_1)

user_2 = get_user_name("joe")
print("User 2: " + user_2)