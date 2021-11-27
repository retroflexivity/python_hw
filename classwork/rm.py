chname = input().lower
with open('all_subtitles.txt', encoding='utf-8') as subs:
    with open('chlines.txt', 'w', encoding='utf-8') as chlines:
        for line in subs:
            if line[0:len(chname)] == chname:
                chlines.write(line)
