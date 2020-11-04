import re
from collections import Counter


def _all_apostr(text):
    c = Counter(text)
    return "'" in c and len(c) == 1


def top_3_words(text):
    r = re.findall(r"[a-zA-Z']+", text.lower(), flags=re.ASCII)
    c = Counter(r)
    c.pop("'", None)
    print(c)
    e = sorted(c.items(), key=lambda i: i[1], reverse=True)[:3]
    return [i[0] for i in e if not _all_apostr(i[0])]



