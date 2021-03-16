from gensim.models import Word2Vec as w2v

from corpus_morpheme_analysis import load_corpus_morph


def modeling():
    corpus_morph = load_corpus_morph()
    corpus_morph = [['+'.join(y) for y in x['words']] for x in corpus_morph]
    print(corpus_morph[:3])

    model = w2v(sentences=corpus_morph, size=100, window=5, min_count=10, iter=20, sg=1)
    model.save('model')


def main():
    model = w2v.load('model')
    print(model.wv.most_similar('부르+VV'))

if __name__ == "__main__":
    main()
