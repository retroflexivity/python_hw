def parse(string):
    commas = []
    inquotes = False
    for i in range(len(string)):
        if string[i] == '"':
            inquotes = not inquotes
        elif not inquotes:
            if string[i] == ',':
                commas.append(i)
    return(commas)


def cleanset(string):
    separators = [i for i in range(len(string)) if (string[i] == '(' or string[i] == "," or string[i] == '}')]
    if separators:
        items = [string[separators[i - 1] + 3:separators[i] - 1] for i in range(1, len(separators))]
        return(', '.join(items))
    else:
        return('"пустота"')


def subjectempty(subject):
    if subject:
        return('с заголовком ' + subject)
    else:
        return('без заголовка')


linenum = 1
with open('enron_3000.csv', encoding='utf-8') as csv:
    lines = csv.readlines()
    width = len(parse(lines[0]))

    while linenum < len(lines):
        line = lines[linenum]
        commas = parse(line)
        while len(commas) < width:
            linenum += 1
            line = line[:-1] + lines[linenum]
            commas = parse(line)
        print('Письмо от', cleanset(line[commas[2] + 1:commas[3]]), 'по адресу', cleanset(line[commas[3] + 1:commas[4]]), subjectempty(line[commas[4] + 1:commas[5]]), 'отправлено', line[commas[1] + 1: commas[2]])

        linenum += 1
