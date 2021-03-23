#from .df_frame import *
import pandas as pd
import os
import re
import time
from google_trans_new import google_translator

def cpct_parsing():
    cpct_list = []
    cs_list = []
    translator = google_translator()

    print('drama start')
    drama_folders = os.listdir('../cpct/drama')
    for folder in drama_folders:
        drama_file_names = os.listdir('../cpct/drama/' + folder)
        for file_name in drama_file_names:
            df = pd.read_excel('../cpct/drama/' + folder + '/' + file_name, engine='openpyxl')
            cs_list.append(["movie", file_name[:-5]])
            for i, row in df.iterrows():
                subtitle = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Subtitle).split("\n"))) if x]
                translation = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Translation).split("\n"))) if x]
                for s, t in zip(subtitle, translation):
                    cpct_list.append([
                        s,
                        t,
                        len(cs_list) - 1
                    ])
                    #print(cpct_list[-1])

    print('drama end')

    print('movie start')
    movie_file_names = os.listdir(u'../cpct/movie')
    for file_name in movie_file_names:
        df = pd.read_excel('../cpct/movie/' + file_name, engine='openpyxl')
        cs_list.append(["movie", file_name[:-5]])
        for i, row in df.iterrows():
            subtitle = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Subtitle).split("\n"))) if x]
            translation = [x for x in list(map(str.strip, re.sub(r'\([^)]*\)|\[[^)]*\]|-', '', row.Translation).split("\n"))) if x]
            for s, t in zip(subtitle, translation):
                cpct_list.append([
                    s,
                    t,
                    len(cs_list) - 1
                ])
                #print(cpct_list[-1])
    print('movie end')

    print('kpop start')
    kpop_file_names = os.listdir(u'../cpct/kpop')
    for file_name in kpop_file_names:
        #df = pd.read_csv('../cpct/kpop/' + file_name)
        df = pd.read_excel('../cpct/kpop/' + file_name, engine='openpyxl')
        print(df)
        for i, row in df.iterrows():
            cs_list.append(['kpop', str(row.artist) + ' - ' + str(row.song_name)])
            #print(str(row.artist) + ' - ' + str(row.song_name))
            lyric = row.lyrics[2:-2]
            lyrics_list = lyric.split('\', \'')
            start = 0
            end = -1
            translation = row.Translation
            while not translation[start].isalpha():
                start = start + 1
            while not translation[end].isalpha():
                end = end - 1
            translation_list = translation[start:end].split('\', \'')

            for l, t in zip(lyrics_list, translation_list):
                cpct_list.append([
                    l,
                    t,
                    len(cs_list) - 1
                ])

    cs_frame = pd.DataFrame(data=cs_list, columns=cs_columns)
    cpct_frame = pd.DataFrame(data=cpct_list, columns=cpct_columns)
    pd.to_pickle(cs_frame, '../data/pandas/cs.pkl')
    pd.to_pickle(cpct_frame, '../data/pandas/cpct.pkl')


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