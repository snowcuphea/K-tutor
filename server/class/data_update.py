import pandas as pd
import os
from konlpy.tag import Kkma

from .models import Kw, Cs, Cpct, Cpcq, Lc


def update():
    # kw 업데이트
    path = os.getcwd()
    kw_data_frame = pd.read_pickle(path + "\data\pandas\kw.pkl")
    for i, row in kw_data_frame.iterrows():
        if not Kw.objects.filter(content=row.content).exists():
            Kw.objects.create(
                content=row['content'],
                count=row['count']
            )

    # cs 업데이트
    cs_data_frame = pd.read_pickle(path + "\data\pandas\cs.pkl")
    for i, row in cs_data_frame.iterrows():
        if not Cs.objects.filter(name=row['name']).exists():
            Cs.objects.create(
                name=row['name'],
                type=row['type'],
                level=0
            )

    # cpct 업데이트
    kkma = Kkma()
    cpct_data_frame = pd.read_pickle(path + "\data\pandas\cpct.pkl")
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
    cpcq_data_frame = pd.read_pickle(path + "\data\pandas\cpcq.pkl")
    kcq_data_frame = pd.read_pickle(path + "\data\pandas\kcq.pkl")

    for i, row in cpcq_data_frame.iterrows():
        if not Cpcq.objects.filter(kor=row.kor).exists():
            cpcq = Cpcq.objects.create(
                kor=row['kor'],
                eng=row['eng'],
            )
            kcq_list = list(kcq_data_frame.loc[kcq_data_frame['cpcq_id'] == cpcq.id]['kw_id'])
            for kcq in kcq_list:
                cpcq.kcq.add(kcq)


def create_lc():
    genres = ['drama', 'movie']
    for genre in genres:
        cs_cnt = Cs.objects.filter(type=genre).count()
        cnt_level = [
            cs_cnt // 3 if cs_cnt % 3 == 0 else cs_cnt // 3 + 1,  # end index of beginner
            cs_cnt // 3 + 1 if cs_cnt % 3 == 2 else cs_cnt // 3,  # end index of intermediate
            cs_cnt // 3  # end index of advanced
        ]
        kw_index = [
            1,
            664,
            1327
        ]
        kw_cnt = Kw.objects.all().count()
        kw_check = [0] * (kw_cnt + 1)
        index = 1
        for i in range(3):
            while index <= cnt_level[i]:
                index += 1
                cs = Cs.objects.get(pk=index)
                cs.level = i
                cpcts = list(Cpct.objects.filter(cs=cs))
                cpcts.sort(key=lambda x: x.main_kw.count)
                cpct_cnt = 0
                for k in range(kw_index[i], kw_index[i] + 663):
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

                        cpct = Cpct.objects.filter(main_kw=kw)
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
                        if len(before.kor.split()) <= 2 or len(cpct.kor.split()) <= 4 or len(after.kor.split()) <= 2:
                            continue

                        kw_check[k] = 1
                        cpct_cnt += 1

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
    # kpop
    cs_list = Cs.objects.filter(cs="kpop")
    singer_list = list(set({x.name.split(" - ")[0] for x in cs_list}))
    for singer in singer_list:
        kw_check = [0] * (kw_cnt + 1)
        song_list = Cs.objects.filter(name__contains=singer)
        for song in song_list:
            for cpct in Cpct.objects.filter(cs=song):
                k = cpct.main_kw.id
                examples = cpct.main_kw.contained_cpcq.all()
                if not examples.exists():
                    examples = Cpct.objects.filter(main_kw_id=k)
                    if not examples.exists():
                        continue

                kw_check[k] = 1
                cpct_cnt += 1
                cpct = Cpct.objects.filter(main_kw_id=k)
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

                examples = list(examples)
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

    singer_dict = dict()
    for singer in singer_list:
        song_list = Cs.objects.filter(name__contains=singer)
        cpct_list = [Cpct.objects.filter(cs=song) for song in song_list]
        level_list = [sum([cpct.main_kw.count for cpct in cpcts]) / len(cpcts) for i, cpcts in enumerate(cpct_list)]
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
        while index <= singer_level[i]:
            singer = singer_list[index]
            song_list = Cs.objects.filter(name__contains=singer)
            for song in song_list:
                song.level = i
