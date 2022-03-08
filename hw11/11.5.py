from csv import DictReader
from re import findall, search
from json import dumps

emails = {}

csv = DictReader(open('enron_3000.csv', encoding='utf-8'))
for line in csv:
    sender = search(r"[a-zA-Z0-9!#$%&'*+/=?^_`|~-]*@[a-zA-Z0-9.-]*", line['From']).group(0)
    receivers = findall(r"[a-zA-Z0-9!#$%&'*+/=?^_`|~-]*@[a-zA-Z0-9.-]*", line['To'])

    if emails.get(sender):
        emails[sender].update(receivers)
    else:
        emails[sender] = set(receivers)

print(emails, sep='\n')
