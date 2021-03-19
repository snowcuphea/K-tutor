from gensim.models import Word2Vec as w2v
from konlpy.tag import Kkma

from corpus_morpheme_analysis import load_corpus_morph
import pandas as pd

from df_frame import *


def kw_parsing():
    model = w2v.load('model')

    # test
    # print(sorted(model.wv.vocab.items(), key=lambda x: -x[1].count)[10][1].count)

    # mean
    # print(sum([x.count for x in model.wv.vocab.values()])/len(model.wv.vocab.values()))

    # middle
    # print(sorted(model.wv.vocab.items(), key=lambda  x: -x[1].count)[len(model.wv.vocab.items())//2][1].count)

    # count가 평균값 이상인 kw의 개수
    # print(len([x for x in model.wv.vocab.values() if x.count > 216]))

    # 평균값 이상인 kw만 남기고 내림차순 정렬
    kw_list = [x for x in model.wv.vocab.items() if x[1].count > 216]
    kw_list.sort(key=lambda x: -x[1].count)
    kw_list = [[i, x[0], x[1].count] for i, x in enumerate(kw_list)]

    kw_frame = pd.DataFrame(data=kw_list, columns=kw_columns)
    pd.to_pickle(kw_frame, "../data/pandas/kw.pkl")
    print(kw_frame)


def find_kw_in_cpcq():
    kkma = Kkma()

    kw_frame = pd.read_pickle("../data/pandas/kw.pkl")
    cpcq_frame = pd.read_pickle("../data/pandas/cpcq.pkl")
    index = 0
    kcq_list = []


    for i, cpcq in cpcq_frame.iterrows():
        for word in kkma.pos(cpcq.kor):
            word = "+".join(word)
            if not kw_frame.loc[kw_frame["content"] == word].empty:
                kcq_list.append([
                    index,
                    int(kw_frame.loc[kw_frame["content"] == word].id),
                    cpcq.id
                ])
                index += 1

    kcq_frame = pd.DataFrame(data=kcq_list, columns=kcq_columns)
    pd.to_pickle(kcq_frame, "../data/pandas/kcq.pkl")

def cleaning_kw_list():
    """
    필요없는 로우 제거
    """
    kw_frame = pd.read_pickle("../data/pandas/kw.pkl")
    clear_list = [
        '전+NNG', '제가+NNG', '내가+NNG', '난+NNG', "그+VV",
        "나도+NNG", "저+VV", "느+VV", "바+NNG", "해지+VV", "누+NNG",
        "대+NNG", "리+NNG", "매력적+NNG", "중이+NNG", "홀+NNG",
        "순+NNG", "야+NNG", "곡+NNG", "군+NNG", "진+NNG", "한잔+NNG",
        "현+NNG", "카+VV", "널+NNG", "들+NNG", "재+NNG", "민+NNG"
    ]
    kw_frame.drop(list(kw_frame.loc[kw_frame['content'].isin(clear_list)].id), 0,
                  inplace=True)
    pd.to_pickle(kw_frame, "../data/pandas/kw.pkl")


def main():
    return


if __name__ == "__main__":
    find_kw_in_cpcq()
    # cleaning_kw_list()