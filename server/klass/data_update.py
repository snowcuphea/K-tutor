import requests

import pandas as pd
import os
from gensim.models import Word2Vec as w2v
from bs4 import BeautifulSoup
from konlpy.tag import Kkma
import numpy as np

from .models import Kw, Cs, Cpct, Cpcq, Lc


def update():
    # kw 업데이트
    path = os.getcwd()
    # kw_data_frame = pd.read_pickle(path + "\data\pandas\kw.pkl")
    # for i, row in kw_data_frame.iterrows():
    #    if not Kw.objects.filter(content=row.content).exists():
    #        Kw.objects.create(
    #            content=row['content'],
    #            count=row['count']
    #        )

    # cs 업데이트
    # cs_data_frame = pd.read_pickle(path + "\data\pandas\cs.pkl")
    # for i, row in cs_data_frame.iterrows():
    #    if not Cs.objects.filter(name=row['name']).exists():
    #        Cs.objects.create(
    #            name=row['name'],
    #            type=row['type'],
    #            level=0
    #        )

    # cpct 업데이트
    kkma = Kkma()
    cpct_data_frame = pd.read_pickle(path + "/data/pandas/cpct.pkl")
    for i, row in cpct_data_frame.iterrows():
        try:
            if not Cpct.objects.filter(kor=row.kor).exists():
                temp_kor = row['kor'].strip()
                temp_word_list = kkma.pos(temp_kor)
                temp_word_list = ['+'.join(w) for w in temp_word_list if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
                kws = Kw.objects.filter(content__in=temp_word_list)
                if kws.exists():
                    main_kw = max(kws, key=lambda x: x.count)
                    cs = Cs.objects.get(id=row['cs'] + 1)
                    Cpct.objects.create(
                        kor=temp_kor,
                        eng=row['eng'],
                        cs=cs,
                        main_kw=main_kw
                    )
        except:
            print(row)

    # cpcq, kcq 업데이트
    # cpcq_data_frame = pd.read_pickle(path + "\data\pandas\cpcq.pkl")
    # kcq_data_frame = pd.read_pickle(path + "\data\pandas\kcq.pkl")

    # for i, row in cpcq_data_frame.iterrows():
    #    if not Cpcq.objects.filter(kor=row.kor).exists():
    #        cpcq = Cpcq.objects.create(
    #            kor=row['kor'],
    #            eng=row['eng'],
    #        )
    #        kcq_list = list(kcq_data_frame.loc[kcq_data_frame['cpcq_id'] == cpcq.id]['kw_id'])
    #        for kcq in kcq_list:
    #            cpcq.kcq.add(kcq)


def create_lc():
    genres = ['drama', 'movie']
    kw_index = [
        1,
        300,
        1000,
        1990
    ]
    kw_cnt = Kw.objects.all().count()
    for genre in genres:
        cs_list = Cs.objects.filter(type=genre)
        cs_cnt = cs_list.count()
        level_dict = dict()
        for cs in cs_list:
            cpct_list = list(Cpct.objects.filter(cs=cs))
            level_dict[cs.name] = sum([x.main_kw.id for x in cpct_list]) / len(cpct_list)
        cs_list = sorted(list(cs_list), key=lambda x: level_dict[x.name])

        cnt_level = [
            cs_cnt // 3 if cs_cnt % 3 == 0 else cs_cnt // 3 + 1,  # end index of beginner
            cs_cnt // 3 + 1 if cs_cnt % 3 == 2 else cs_cnt // 3,  # end index of intermediate
            cs_cnt // 3  # end index of advanced
        ]
        index = 1
        for i in range(3):
            while index <= sum(cnt_level[:i + 1]):
                kw_check = [0] * (kw_cnt + 1)
                cs = cs_list[index - 1]
                index += 1
                cs.level = i
                cs.save()
                cpcts = Cpct.objects.filter(cs=cs)
                cpct_cnt = Lc.objects.filter(cs=cs).count()
                for k in range(kw_index[i], kw_index[i + 1]):
                    kw = Kw.objects.get(pk=k)
                    if cpct_cnt == 100:
                        break

                    if not kw_check[k]:
                        # 다른 예시가 존재하지 않을때
                        examples = kw.contained_cpcq.all()
                        if not examples.exists():
                            examples = Cpct.objects.filter(main_kw=kw)
                            if not examples.exists():
                                continue

                        cpct = cpcts.filter(main_kw=kw)
                        if cpct.exists():
                            cpct = cpct[0]
                        else:
                            continue
                        if cpct.pk == 1 or cpct.cs != Cpct.objects.get(pk=cpct.pk - 1).cs:
                            continue
                        else:
                            before = Cpct.objects.get(pk=cpct.pk - 1)
                        if cpct.pk == 59490 or cpct.cs != Cpct.objects.get(pk=cpct.pk + 1).cs:
                            continue
                        else:
                            after = Cpct.objects.get(pk=cpct.pk + 1)

                        # 너무 짧을 때
                        if len(before.kor.split()) <= 1 or len(cpct.kor.split()) <= 3 or len(after.kor.split()) <= 1:
                            continue

                        examples = list(examples)
                        if cpct in examples:
                            examples.remove(cpct)
                        examples = examples[:3]

                        if not Lc.objects.filter(cpct_kor=cpct.kor).exists():
                            Lc.objects.create(
                                before_kor=before.kor,
                                before_eng=before.eng,
                                cpct_kor=cpct.kor,
                                cpct_eng=cpct.eng,
                                after_kor=after.kor,
                                after_eng=after.eng,
                                example="|".join([x.kor for x in examples]),
                                cs=cs,
                                main_kw=kw
                            )
                            kw_check[k] = 1
                            cpct_cnt += 1
                        else:
                            print(cpct.cs, cpct.kor)
    # kpop
    cs_list = Cs.objects.filter(type="kpop")
    singer_list = list(set({x.name.split(" - ")[0] for x in cs_list}))
    for singer in singer_list:
        song_list = Cs.objects.filter(name__contains=singer)
        for song in song_list:
            kw_check = [0] * (kw_cnt + 1)
            for cpct in Cpct.objects.filter(cs=song):
                k = cpct.main_kw.id
                if kw_check[k]:
                    continue
                examples = cpct.main_kw.contained_cpcq.all()
                if not examples.exists():
                    examples = Cpct.objects.filter(main_kw_id=k)
                    if not examples.exists():
                        continue

                if cpct.pk == 1 or cpct.cs != Cpct.objects.get(pk=cpct.pk - 1).cs:
                    continue
                else:
                    before = Cpct.objects.get(pk=cpct.pk - 1)
                if cpct.pk == 59490 or cpct.cs != Cpct.objects.get(pk=cpct.pk + 1).cs:
                    continue
                else:
                    after = Cpct.objects.get(pk=cpct.pk + 1)

                examples = list(examples)
                if cpct in examples:
                    examples.remove(cpct)
                examples = examples[:3]

                if not Lc.objects.filter(cpct_kor=cpct.kor).exists():
                    Lc.objects.create(
                        before_kor=before.kor,
                        before_eng=before.eng,
                        cpct_kor=cpct.kor,
                        cpct_eng=cpct.eng,
                        after_kor=after.kor,
                        after_eng=after.eng,
                        example="|".join([x.kor for x in examples]),
                        cs=song,
                        main_kw=cpct.main_kw
                    )
                    kw_check[k] = 1

    singer_dict = dict()
    for singer in singer_list:
        song_list = Cs.objects.filter(name__contains=singer)
        cpct_list = [Cpct.objects.filter(cs=song) for song in song_list if Cpct.objects.filter(cs=song).exists()]
        level_list = [0] * len(cpct_list)
        for i, cpcts in enumerate(cpct_list):
            level_list[i] = sum([cpct.main_kw.id for cpct in cpcts]) / len(cpcts)
        singer_dict[singer] = sum(level_list) / len(level_list)
    singer_list.sort(key=lambda x: singer_dict[x])
    singer_cnt = len(singer_list)
    singer_level = [
        singer_cnt // 3 if singer_cnt % 3 == 0 else singer_cnt // 3 + 1,  # end index of beginner
        singer_cnt // 3 + 1 if singer_cnt % 3 == 2 else singer_cnt // 3,  # end index of intermediate
        singer_cnt // 3  # end index of advanced
    ]
    index = 1
    for i in range(3):
        while index <= sum(singer_level[:i + 1]):
            singer = singer_list[index]
            index += 1
            song_list = Cs.objects.filter(name__contains=singer)
            for song in song_list:
                song.level = i
                song.save()


def add_meaning_to_lc():
    path = os.getcwd()
    lcs = Lc.objects.all()
    model = w2v.load(path + "/data/pandas/model")
    kkma = Kkma()
    for i, lc in enumerate(lcs):
        if lc.meaning:
            continue
        meanings = request_dict(lc.main_kw.content_kor)
        if not meanings:
            lc.delete()
            continue

        similarity = []
        main_sentence = [w for w in kkma.pos(lc.cpct_kor) if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
        main_sentence = ["+".join(w) for w in main_sentence]
        for j, meaning in enumerate(meanings):
            definitions_morph = [w for w in kkma.pos(meaning[1]) if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
            definitions_morph = ["+".join(w) for w in definitions_morph]
            temp_similarity = []
            for w1 in main_sentence:
                for w2 in definitions_morph:
                    try:
                        temp_similarity.append(model.similarity(w1, w2))
                    except:
                        continue
            if not temp_similarity:
                similarity.append((j, 0))
            else:
                similarity.append((j, np.mean(temp_similarity)))
        similarity.sort(key=lambda x:-x[1])
        meaning = "|".join([meanings[x[0]][1] for n, x in enumerate(similarity) if n <= 2])
        lc.main_kw_kor = meanings[0][0]
        lc.meaning = meaning
        main_splited = lc.cpct_kor.split()
        find = False
        for i, word in enumerate(main_splited):
            word_morph = [w for w in kkma.pos(word) if w[1] in ['NNG', 'VV', 'VA', 'MAJ', 'XR']]
            word_morph = ["+".join(w) for w in word_morph]
            if lc.main_kw.content_kor in word_morph:
                lc.main_kw_index = i
                find = True
                break
        if not find:
            lc.delete()
        else:
            lc.save()


pos_dict = {
    "NNG": 1,
    "VV": 5,
    "VA": 6,
    "MAJ": 8,
    "XR": 8
}


def request_dict(word):
    word, pos = word.split("+")
    if pos != "NNG":
        words = [word + "하다", word + "다"]
    else:
        words = [word]

    meanings = []
    for word in words:
        url = "https://opendict.korean.go.kr/api/search"
        param = {
            "key": "60846D3B408D46C3CDBC8FA261125A3E",
            "q": word,
            "sort": "popular",
            "advanced": "y",
            "pos": pos_dict[pos],
            "type4": "general"
        }
        doc = requests.get(url, param).content.decode("utf-8")
        soup = BeautifulSoup(doc, 'html.parser')
        try:
            word_con = soup.find('word').get_text()
        except:
            continue
        res = [(word_con, x.get_text()) for x in soup.findAll('definition')]
        meanings.extend(res)

    return meanings


def updateLc():
    lcs = Lc.objects.all()
    for lc in lcs:
        lc.main_kw = Cpct.objects.get(kor=lc.cpct_kor).main_kw
        lc.save()