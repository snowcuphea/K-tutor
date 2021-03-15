import pandas as pd
from df_frame import *
import os
from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()
kw_list = []
kw = dict()
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
        for word in temp_word_list:
            # 한글자 제외
            if len(word[0]) == 1:
                continue

            # 영어, 숫자를 포함하고 있는 단어 제외
            is_kor = True
            for letter in word[0]:
                if letter.encode().isalpha() or letter.isdigit():
                    is_kor = False
                    break
            if not is_kor:
                continue

            # 마침표와 따옴표 제거
            result = [word[0].strip(".").strip("?").strip("\"").strip("\'"), word[1]]
            kkma_list.append('+'.join(result))

        if i == 10:
            break

for word in kkma_list:
    if word in kw:
        kw[word] += 1
    else:
        kw[word] = 1

for key, value in kw.items():
    if value >= 2:
        kw_list.append([
            index,
            key,
            value
        ])
        index += 1
print(kw_list)

# kw_list.sort(key=lambda x: -x[2])
# kw_frame = pd.DataFrame(data=kw_list, columns=kw_columns)
# pd.to_pickle(kw_frame, "../data/pandas/kw.pkl")
# print(kw_frame)
#
# xlxs_dir = os.path.join("../data/pandas", "kw.xlsx")
# kw_frame.to_excel(xlxs_dir, # directory and file name to write
#             sheet_name = 'Sheet1',
#             na_rep = 'NaN',
#             float_format = "%.2f",
#             header = True,
#             index = True,
#             index_label = "id",
#             startrow = 1,
#             startcol = 1,
#             #engine = 'xlsxwriter',
#             freeze_panes = (2, 0)
#             )
