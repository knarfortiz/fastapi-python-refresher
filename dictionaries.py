"""
Dictionaries
"""

user_dictionary = {
    'username': 'coding',
    'name': 'frank',
    'age': 29
}

user_dictionary['married'] = False
print(user_dictionary)
print(user_dictionary.get('username'))
print(user_dictionary['username'])
user_dictionary.pop('age')
print(user_dictionary)
del user_dictionary
# user_dictionary.clear()
