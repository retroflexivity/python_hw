verbs = []
with open('sah_yktdt-ud-test.conllu.txt', encoding='utf-8') as conllu:
    with open(input('Введите название файла для вывода ') + '.txt', 'w', encoding='utf-8') as output:

        for line in conllu:
            if line[0].isnumeric():
                words = line.split()
                if(words[3] == 'VERB' and not(words[2] in verbs)):
                    verbs.append(words[2])

        for verb in verbs:
            output.write(verb + '\n')
