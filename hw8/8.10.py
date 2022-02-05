from string import punctuation
from tqdm import tqdm
from time import sleep

pcount = 0
filename = 'euskara.conllu'
with open(filename, encoding='utf-8') as f:
    for ch in tqdm(f.read()):
        if ch in punctuation:
            sleep(0.0001)
            pcount += 1

print(pcount)
