
import re
import pickle
import pandas as pd
from unidecode import unidecode
from itertools import chain
import sklearn

def word2ngrams(text, n=3):
    """ Convert word into character ngrams. """
    return [text[i:i+n] for i in range(len(text)-n+1)]


def sent2ngrams(text, n=3):
    return list(chain(*[word2ngrams(i,n) for i in text.lower().split()]))

def char_decode(text):
    return text.replace("ä","ae").replace("ö","oe").replace("ü","ue")

def standardize_regex_word(text):
    return re.sub('[^a-z0-9]+', ' ', text)

def standardize_regex_2gram(text):
    return ' '.join(sent2ngrams(re.sub('[^a-z0-9]+', '', text),2))

def standardize_regex_3gram(text):
    return ' '.join(sent2ngrams(re.sub('[^a-z0-9]+', '', text),3))

def standardize_regex_3_4gram(text):
    return standardize_regex_3gram(text) + standardize_regex_4gram(text)

def standardize_regex_4gram(text):
    return ' '.join(sent2ngrams(re.sub('[^a-z0-9]+', '', text),4))


def standardize_text(df, text_field, tokenizer):
    df[text_field] = df[text_field].str.lower()
    df[text_field] = df[text_field].apply(char_decode)
    df[text_field] = df[text_field].apply(unidecode)
    if tokenizer == "word":
        df[text_field] = df[text_field].apply(standardize_regex_word)
    if tokenizer == "2-gram":
        df[text_field] = df[text_field].apply(standardize_regex_2gram)
    if tokenizer == "3-gram":
        df[text_field] = df[text_field].apply(standardize_regex_3gram)
    if tokenizer == "3&4-gram":
        df[text_field] = df[text_field].apply(standardize_regex_3_4gram)
    if tokenizer == "4-gram":
        df[text_field] = df[text_field].apply(standardize_regex_4gram)
    return df


def classify_article(article, tokenizer, mod_clsfr, mod_vect):
    
    d = {'Article': [article]}

    test_rec = pd.DataFrame(data=d)

    clean_test_X = test_rec.copy()
    clean_test_X = standardize_text(clean_test_X, "Article", tokenizer)

    test_corpus = clean_test_X["Article"]

    vect = pickle.load(open(mod_vect, 'rb'))
    emb = dict()
    emb["test_X"] = (vect.transform(test_corpus))


    clsfr = pickle.load(open(mod_clsfr, 'rb'))
    pred = clsfr.predict(emb['test_X']).tolist()
    prob = clsfr.predict_proba(emb['test_X'])

    return pred[0]
    