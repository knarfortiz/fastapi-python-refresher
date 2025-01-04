"""
Flow control: If Else ElIf
"""

GRADE = 60

if GRADE >= 90:
    LETTER = 'A'
elif 80 <= GRADE < 90:
    LETTER = 'B'
elif 70 <= GRADE < 80:
    LETTER = 'C'
elif 60 <= GRADE < 70:
    LETTER = 'D'
else:
    LETTER = 'F'


print(f'You got a {LETTER}')



