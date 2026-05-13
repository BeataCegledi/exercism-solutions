"""Pig Latin translator."""


def translate(text):
    """Translate text into Pig Latin.

    Rules:
    - Words starting with a vowel (a, e, i, o, u) or with 'xr'/'yt' → just add 'ay'.
    - Words starting with consonant(s) → move the consonant cluster to the end,
      then add 'ay'.
    - 'qu' is treated as a single consonant cluster (moved together).
    - 'y' acts as a vowel except when it is the original first letter of the word.
    """
    result = []
    for word in text.lower().split():
        if word[0] in 'aeiou' or word[:2] in {'xr', 'yt'}:
            result.append(word + 'ay')
            continue
        current = word
        if current[0] == 'y':
            current = current[1:] + current[0]
        while current[0] not in 'aeiouy':
            if current[:2] == 'qu':
                current = current[2:] + current[:2]
            else:
                current = current[1:] + current[0]
        result.append(current + 'ay')
    return ' '.join(result)
        