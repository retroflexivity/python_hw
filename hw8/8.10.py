from tqdm import tqdm
from time import sleep

pcount = 0
filename = 'euskara.conllu'
with open(filename, encoding='utf-8') as f:
    for line in tqdm(f.readlines()):
        sleep(0.0005)
        if 'PUNT' in line:
            pcount += 1

print(pcount)
