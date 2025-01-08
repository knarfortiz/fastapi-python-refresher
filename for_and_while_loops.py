"""
For & While Loops
"""

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)


print("-"*10)
i = 0
while i < len(my_list):
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("Done")

# print('-'*10)


'''
Exercise

Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
'''

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in my_list:
    i = 0
    while i < 3:
        i += 1
        if day == "Monday":
            continue
        print(day)
    print("-"*10)