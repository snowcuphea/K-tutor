#from .df_frame import *
import pandas as pd
import os
import re
from google_trans_new import google_translator

def cpct_parsing():
    cpct_list = []
    cs_list = []
    translator = google_translator()

    drama_folders = os.listdir('../cpct/drama')
    for folder in drama_folders:
        drama_file_names = os.listdir('../cpct/drama/' + folder)
        for file_name in drama_file_names:
            df = pd.read_excel('../cpct/drama/' + folder + '/' + file_name, engine='openpyxl')
            cs_list.append(["movie", file_name[:-5]])
            for i, row in df.iterrows():
                subtitle = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Subtitle).split("\n"))) if x]
                #print(subtitle)
                try:
                    translation = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Translation).split("\n"))) if x]
                except:
                    translation = [translator.translate(x, lang_tgt='en') for x in subtitle]

                for s, t in zip(subtitle, translation):
                    cpct_list.append([
                        s,
                        t,
                        len(cs_list) - 1
                    ])
                    print(cpct_list[-1])

    # movie_file_names = os.listdir(u'../cpct/movie')
    # for file_name in movie_file_names:
    #     df = pd.read_excel('../cpct/movie/' + file_name, engine='openpyxl')
    #     cs_list.append(["movie", file_name[:-5]])
    #     for i, row in df.iterrows():
    #         subtitle = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Subtitle).split("\n"))) if x]
    #         #print(subtitle)
    #         try:
    #             translation = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Translation).split("\n"))) if x]
    #         except:
    #             translation = [translator.translate(x, lang_tgt='en') for x in subtitle]
    #
    #         for s, t in zip(subtitle, translation):
    #             cpct_list.append([
    #                 s,
    #                 t,
    #                 len(cs_list) - 1
    #             ])
    #             print(cpct_list[-1])

    # kpop_file_names = os.listdir(u'../cpct/kpop')
    # for file_name in kpop_file_names:
    #     df = pd.read_csv('../cpct/kpop/' + file_name)
    #     for i, row in df.iterrows():
    #         cs_list.append(['kpop', row.artist + ' - ' + row.song_name])
    #         lyric = row.lyrics[2:-2]
    #         lyrics_list = lyric.split('\', \'')
    #         for l in lyrics_list:
    #             cpct_list.append([
    #                 l,
    #                 translator.translate(l, lang_tgt='en'),
    #                 len(cs_list) - 1
    #             ])

    # cs_frame = pd.DataFrame(data=cs_list, columns=cs_columns)
    # cpct_frame = pd.DataFrame(data=cpct_list, columns=cpct_columns)
    # pd.to_pickle(cs_frame, '../data/pandas/cs.pkl')
    # pd.to_pickle(cpct_frame, '../data/pandas/cpct.pkl')


def main():
    cpct_parsing()

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
        from df_frame import *
    else:
        from .df_frame import *

    main()