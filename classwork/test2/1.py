from re import fullmatch
from json import dumps


def correct(nick):
    if fullmatch(r'@[a-zA-Z._]{7,9}', nick):
        if not('__' in nick or '..' in nick):
            return True
    return False


messages = []
with open('gistfile1.csv', encoding='utf-8') as f:
    for line in f.readlines()[1:]:
        nick, message = line.split('\t')
        if correct(nick):
            messages.append({'nick': nick, 'emojis': message})

with open('messages.json', 'w', encoding='utf-8') as f:
    f.write(dumps(messages, indent=0, ensure_ascii=False))
