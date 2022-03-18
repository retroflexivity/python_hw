def clean(str):  # избавляемся от тегов
    if str[0] == ' ':
        return(clean(str[1:]))
    if (start := str.find('<')) > -1:
        return(clean(str[:start] + str[str.find('>') + 1:]))
    return(str)


def checksubj(line):  # проверка на релевантность
    subjlist = ['русск', 'математик', 'информатик', 'литератур', 'физик', 'иностранн', 'хими', 'географи', 'обществознани', 'биологи', 'истори', 'творческ', 'собеседовани']
    for subj in subjlist:
        if line.lower().find(subj) > -1:
            return(line)
    return(False)


# работает в 99.9999999% случаев!
found = False
with open('ba.txt', encoding='utf-8') as file:
    html = file.readlines()

with open('exams.txt', 'w', encoding='utf-8') as output:
    for line in html:  # метод один — минимальные баллы (большая часть оп)
        if (line.find('инимальный балл') > -1):
            output.write(clean(line))
            found = True

    if not(found):
        inlist = False
        subjfound = []
        for line in html:  # метод два — названия предметов (напр. oriental)
            if (line[:-1] == '<ul>') or (line[:-1] == '<ol>'):  # входим в список
                inlist = True
            elif inlist:
                if (line[:-1] == '</ul>') or (line[:-1] == '</ol>'):  # проверяем, что получилось, и выходим из списка
                    inlist = False
                    if len(subjfound) == 3:
                        for subjl in subjfound:
                            output.write(clean(subjl))
                        found = True
                        break
                    subjfound = []
                elif clean(line).split():  # ищем в строке хтмл-списка предметы
                    if (found := checksubj(line)):
                        subjfound.append(found)
                    else:
                        inlist = False  # не судьба
                        subjfound = []

    if not(found):
        for line in html:  # метод три — просто строка с упоминанием егэ (напр. compds)
            if (line.find('ЕГЭ') > -1) or (line.find('Экзамен') > -1):
                output.write(clean(line))
