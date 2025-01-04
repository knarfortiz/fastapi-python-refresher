"""
String formatting
"""

first_name = 'John'
print('Hi, ' + first_name)
print(f'Hi, {first_name}')

sentence = 'Hi, {} {}'
last_name = 'Doe'
print(sentence.format(first_name, last_name))
