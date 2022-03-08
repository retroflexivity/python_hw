from csv import DictReader, DictWriter
from re import findall, search
from random import sample, choices


def censor(address):
    censored = ''
    for i in sample(address, len(address)):
        censored += ''.join((choices([i, '*', '#'], weights=[8, 1, 1])))
    return censored


csv = DictReader(open('enron_3000.csv', encoding='utf-8'))
with open('enron_3000.csv', 'w', encoding='utf-8') as f:
    writer = DictWriter(f, fieldnames=csv.fieldnames)
    writer.writeheader()

    for line in csv:
        mail = line
        sender = search(r"[a-zA-Z0-9!#$%&'*+/=?^_`|~-]*@[a-zA-Z0-9.-]*", mail['From']).group(0)
        if not sender.endswith('@enron.com'):
            mail['From'] = mail['From'].replace(sender, censor(sender))
        writer.writerow(line)


csv = DictReader(open('enron_3001.csv', encoding='utf-8'))
for line in csv:
    if not line['From'].endswith("@enron.com'})"):
        print(line['From'])
