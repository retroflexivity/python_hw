with open('лог-беседы.txt', 'a', encoding='utf-8') as log:
    while True:
        if (inp := input('Как дела?\n')):
            log.write(inp + '\n')
        else:
            break
