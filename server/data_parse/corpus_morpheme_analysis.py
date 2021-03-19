import pandas as pd
import json
from konlpy.tag import Kkma

from df_frame import *


def load_corpus_morph():
    """
    @return List: 형태소 분석 말뭉치를 리스트로
    """
    json_file = open("../data/pandas/corpus_morpheme_analysis.json", encoding='UTF8')
    return json.load(json_file)


def kw_cpcq_parse():
    """
    kw와 cpcq를 pkl로 save
    """
    # konlpy의 kkma 형태소 분석기 사용
    kkma = Kkma()
    kkma_list = []
    cpcq_list = []

    file_names = [
        "../data/excel/구어체_1.xlsx",
        "../data/excel/구어체_2.xlsx",
        "../data/excel/대화체.xlsx"
    ]
    index = 0

    for file_name in file_names:
        df = pd.read_excel(file_name, engine="openpyxl")

        # 형태소 분석 후 의미 있는 형태소의 분류만 추출하여 문장별로 json-array 저장
        for i, c in df.iterrows():
            temp_word_list = kkma.pos(c.원문)
            temp_word_list = [w for w in temp_word_list if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
            if temp_word_list:
                kkma_list.append({
                    "id": index,
                    "words": temp_word_list
                })
                index += 1

                cpcq_list.append([
                    index,
                    c.원문,
                    c.번역문
                ])
                index += 1
                print(cpcq_list[-1])

    with open("../data/pandas/corpus_morpheme_analysis.json", "w", encoding='utf-8') as json_file:
        json.dump(kkma_list, json_file, indent=4, ensure_ascii=False)

    cpcq_frame = pd.DataFrame(data=cpcq_list, columns=cpcq_columns)
    pd.to_pickle(cpcq_frame, "../data/pandas/cpcq.pkl")

def main():
    return

if __name__ == "__main__":
    main()
