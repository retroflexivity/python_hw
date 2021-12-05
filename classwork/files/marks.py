with open('marks.txt', encoding='utf-8') as marks:
    with open('failed.txt', 'w', encoding='utf-8') as failed:
        for student in marks:
            if int(student.split(',')[2]) < 4:
                failed.write(student.split(',')[1] + '\n')
