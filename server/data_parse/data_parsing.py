from gensim.models import Word2Vec as w2v
from corpus_morpheme_analysis import load_corpus_morph
import pandas as pd

from df_frame import *


def main():
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


if __name__ == "__main__":
    main()
