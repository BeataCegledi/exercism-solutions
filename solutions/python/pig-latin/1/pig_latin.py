def translate(text):
    """Pig Latin translator.
    Rules:
    - Words starting with a vowel (a, e, i, o, u) or with 'xr'/'yt' → just add 'ay'.
    - Words starting with consonant(s) → move the consonant cluster to the end,
      then add 'ay'.
    - 'qu' is treated as a single consonant cluster (moved together).
    - 'y' acts as a vowel except when it is the original first letter of the word.
    """
    result = []
    for word in text.lower().split():
        if word[0] in 'aeiou' or word[:2] in ('xr', 'yt'):
            result.append(word + 'ay')
            continue
        if word[0] == 'y':
            word = word[1:] + word[0]
        while word[0] not in 'aeiouy':
            if word[:2] == 'qu':
                word = word[2:] + word[:2]
            else:
                word = word[1:] + word[0]
        result.append(word + 'ay')
    return ' '.join(result)
        