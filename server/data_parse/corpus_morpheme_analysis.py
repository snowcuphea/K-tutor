import pandas as pd
from konlpy.tag import Kkma
import json

kkma = Kkma()
kkma_list = []

file_names = [
    "../data/excel/구어체_1.xlsx",
    "../data/excel/구어체_2.xlsx",
    "../data/excel/대화체.xlsx"
]
index = 0

for file_name in file_names:
    df = pd.read_excel(file_name, engine="openpyxl")

    for i, c in df.iterrows():
        temp_word_list = kkma.pos(c.원문)
        temp_word_list = [w for w in temp_word_list if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
        if temp_word_list:
            kkma_list.append({
                "id": index,
                "words": temp_word_list
            })
            index += 1

with open("../data/pandas/corpus_morpheme_analysis.json", "w", encoding='utf-8') as json_file:
    json.dump(kkma_list, json_file, indent=4, ensure_ascii=False)