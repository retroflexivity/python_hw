from re import sub

with open('povest.txt', encoding='utf-8') as f:
    text = f.read()

text = sub(r'(\n *){2,999}', '\n', text)
text = sub(r'\[[0-9]*\]', '', text)
text = sub(r' *([,.!?;:])(?=[А-ЯѢа-яѣ1-9«])', r'\1 ', text)

with open('povest_cleansed.txt', 'w', encoding='utf-8') as f:
    f.write(text)
