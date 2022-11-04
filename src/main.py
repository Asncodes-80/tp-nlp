#!/usr/bin/env python3
#
"""Text Processing practice.

autor: Alireza Soltani Neshan
Date: Fri 4 Nov, 2022
"""

import os

from nltk.corpus import stopwords
import nltk.stem as stemmer
from nltk import tokenize

import lemm_words

c_path: str = os.getcwd()

# Data
beanstalk_text: str = os.path.join(c_path, "data/Beanstalk.txt")
short_sample_en: str = os.path.join(c_path, "data/ShortSampleEnglish.txt")
short_sample_fa: str = os.path.join(c_path, "data/ShortSamplePersian.txt")
zahak_text: str = os.path.join(c_path, "data/zahak.txt")


def rm_whitespace(file_path: str = "", lang="en") -> str:
    """WhiteSpace Removal in text.

    Read `txt` file and remove all white space from text and convert strings to
    lower case. main problem is punctuations.

    :param file_name
    :param lang
    """
    wst = tokenize.WhitespaceTokenizer()
    with open(file_path, "r", encoding="utf-8") as file:
        file: str = file.read()
        sk_result: list = wst.tokenize(file)
        result: str = ""
        for word in sk_result:
            result += f"{word.lower()} " if lang == "en" else f"{word}"
        return result.strip(" ")


def rm_punctuations(data: str = "") -> list:
    """Punctuation removal by regex pattern."""
    regex_tokenizer = tokenize.RegexpTokenizer(r"\w+")
    return regex_tokenizer.tokenize(data)


def rm_stopwords(data: str = "") -> list:
    """Stopwords removal.

    Stopwords is a, an, the, in, and etc, in a simple text.
    """
    remove_word_lang = set(stopwords.words("english"))
    modified_words: list = [
        word for word in tokenize.word_tokenize(data) if word not in remove_word_lang
    ]
    return modified_words


def word_stemmer(data: str = "", method: any = stemmer.PorterStemmer()) -> list:
    """Find word stemmer with two method."""
    data_tokenize: list = tokenize.word_tokenize(data)
    return [method.stem(i) for i in data_tokenize]


def special_words_lemmatizer(words: list[dict] = None):
    """Lemmatize custom words in specific structure."""
    if words is None:
        words = [{"word": "were", "type": "a"}]

    lemmatizer = stemmer.WordNetLemmatizer()
    for word in words:
        main_stem: str = lemmatizer.lemmatize(word["word"], word["type"])
        print(f"{word['word']} -> {main_stem}")


# WhiteSpace remove as requirement variables
result_en = rm_whitespace(file_path=short_sample_en)
beanstalk: str = rm_whitespace(file_path=beanstalk_text)
result_fa = rm_whitespace(file_path=short_sample_fa)
