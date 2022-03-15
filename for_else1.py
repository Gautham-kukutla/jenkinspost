student_name = input("Please enter student Name:")

marks = {'arjun': 90, 'kiran': 55, 'raju': 77}

for student in marks:

    if student == student_name:
        print(marks[student])
        break
else:

    print('No entry with that name found.')
