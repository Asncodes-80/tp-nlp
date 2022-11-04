""" Lemmatize word data table

|    words    | types |
|+-----------+|+-----+|
|     went    |   v   |
|    better   |   a   |
|     was     |   v   |
|    eaten    |   v   |
| bufferfiles |   n   |
|   fishing   |   n   |
|  signaling  |   s   |

"""
# You should specify a word with that type, type is in range (v: verb | n:
# nouns | r: adverbs | a: adjective | s: satelliteAdjective)
words = [
    {
        "word": "went",
        "type": "v",
    },
    {
        "word": "better",
        "type": "a",
    },
    {
        "word": "was",
        "type": "v",
    },
    {
        "word": "eaten",
        "type": "v",
    },
    {
        "word": "bufferfiles",
        "type": "n",
    },
    {
        "word": "fishing",
        "type": "n",
    },
    {
        "word": "signaling",
        "type": "s",
    },
]
