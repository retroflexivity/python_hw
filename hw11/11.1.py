users = []

with open('users.txt', encoding='utf-8') as f:
    for line in f:
        data = line[:-1].split(';')
        users.append({'name': data[0], 'phone': data[1], 'birthday': data[2]})

print(users)
