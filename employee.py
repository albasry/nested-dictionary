employees = {
    'Accounting': {
        101: 'Elon Musk',
        102: 'Steve Jobs',
        103: 'Mark Zuckerberg'
    },
    'Marketing': {
        201: 'Bill Gates',
        202: 'Tim Cook',
        203: 'Jeff Bezos'
    }
}

enter = int(input('Enter ID Number: '))
department = list(employees)
if 101 <= enter <= 103:
    print(f'=== {department[0]} department.')
    print(f'=== {employees["Accounting"][enter]}.')
elif 201 <= enter <= 203:
    print(f'=== {department[1]} department.')
    print(f'=== {employees["Marketing"][enter]}.')
else:
    print('== Invalid ID Number ==')
