import json
with open('result.json', encoding='utf-8') as f:
    list = json.loads(f.read())['chats']['list']

max = 0
for chat in list:
    if len(chat['messages']) > max:
        maxname = chat['name']
        max = len(chat['messages'])

print(maxname)
