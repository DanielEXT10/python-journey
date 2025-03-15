user = {
    'name': 'Daniel',
    'age':'29',
    'address':'yuridia valenzuela'
}

print(user['name'])

# Add an element to the dictionary key, value
user['cellphone'] = 'Iphone'
print(user)

empty_dictionary = {}

#wipe an existing dictionary
#user = {}

print(user)

#loop through dictionaries

for key in user:
    print(key)
    print(user[key])