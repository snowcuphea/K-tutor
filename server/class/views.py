import pandas as pd
import os
from konlpy.tag import Kkma

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Kw, Cs, Cpct, Cpcq


@api_view(['GET'])
def updateDB(request):
    # kw 업데이트
    path = os.getcwd()
    kw_data_frame = pd.read_pickle(path + "/data/pandas/kw.pkl")
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
            if row['cs'] < 212:
                continue
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

    return Response("OK", status=status.HTTP_200_OK)


def cs_list(request, type):
    return
