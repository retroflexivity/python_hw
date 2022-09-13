import json
import pandas as pd

dict = json.load(open('data.json'))
df = pd.DataFrame([[i['text'], i['src_alignment'][0]['src'], float(i['src_alignment'][0]['off_end_src']) - float(i['src_alignment'][0]['off_start_src'])] for i in dict['sentences']], columns=['text', 'src', 'len'])

for src in df['src'].unique():
    df[(df['src'] == src) & (df['len'] >= 1)]['text'].to_json(src + '.json', orient='records', force_ascii=False)
