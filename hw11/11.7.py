from re import sub, search, findall, MULTILINE

with open('enroncase.html', encoding='utf-8') as f:
    text = f.read()

text = search(r'<body(.*\n)*</body>', text).group(0)  # обрезаем
text = sub(r'<tbody(.*\n)*</tbody>', '', text)  # сводка о компании
text = sub(r'<.*class="thumb.*', '', text)  # картинки
text = sub(r'<div id="toc"(.*\n)*</ul>\n</div>', '', text)  # содержание
text = sub(r'<style.*', '', text)  # что-то стремное в хронологии

text = sub(r'.*noprint.*', '', text)  # материал из википедии
text = sub(r'.*mw-jump-link.*', '', text)  # ссылки

for i in findall(r'&#([0-9]*);', text):  # заменяем хтмл-коды
    text = text.replace('&#' + i + ';', chr(int(i)))

text = sub(r'<.*?>', '', text)  # хтмл-теги

text = sub(r'\[[0-9]*\]', '', text)  # референции
text = text.replace('[править | править код]', '')

text = sub(r'Примечания(.*\n)*', '', text)  # опять обрезаем
text = sub(r'(\n\t*){2,999}', '\n\n', text)

text = text.strip()

with open('enroncase.txt', 'w', encoding='utf-8') as f:
    f.write(text)
