import requests
import re
import collections


def get_source(url):
    url = requests.get(url)
    return url.text


def strict_search(s, text):
    words = re.findall('(?<!\S)\w+|\w+(?<!\S)', text)
    return collections.Counter(words)[s]


def flex_search(s, reg, text):
    words = re.findall(
        "(?<!\w)({reg}){s}|{s}({reg})(?<!\w)"
        .format(reg="|".join(reg), s=s),
        text
    )
    return len(words)
