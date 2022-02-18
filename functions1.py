def is_free_shipping(user_state):
    approved_states = ['CA','FL','TX','NY','AZ','NV','WA','OR']

    if user_state in approved_states:
        return True
    else:
        return False

my_state = 'DD'
if is_free_shipping(my_state):
    print('Ship it for free')
else:
    print('charge for shipping')
