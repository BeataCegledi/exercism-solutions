"""Count word frequencies in a sentence."""

import re
from collections import Counter


def count_words(sentence):
    """Count word frequencies, ignoring case and treating non-alphanumerics as separators."""

    words = re.findall(r"[^\W_]+(?:'[^\W_]+)*", sentence.lower())
    return dict(Counter(words))