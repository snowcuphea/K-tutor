from gensim.models import Word2Vec as w2v

from corpus_morpheme_analysis import load_corpus_morph


def modeling():
    """
    형태소 분석 말뭉치를 가져와 "형태소+타입"형태로 학습시킴
    Word2Vec을 사용했고 model을 저장
    """
    corpus_morph = load_corpus_morph()
    corpus_morph = [['+'.join(y) for y in x['words']] for x in corpus_morph]
    print(corpus_morph[:3])

    model = w2v(sentences=corpus_morph, size=100, window=5, min_count=10, iter=20, sg=1)
    model.save('model')


def main():
    model = w2v.load('model')
    # print(model.wv.vocab.keys())




if __name__ == "__main__":
    main()
