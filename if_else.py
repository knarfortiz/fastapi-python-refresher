"""
Flow control: If Else ElIf
"""

GRADE = 60

if GRADE >= 90:
    LETTER = 'A'
elif GRADE >= 80:
    LETTER = 'B'
elif GRADE >= 70:
    LETTER = 'C'
elif GRADE >= 60:
    LETTER = 'D'
else:
    LETTER = 'F'


print(f'You got a {LETTER}')



