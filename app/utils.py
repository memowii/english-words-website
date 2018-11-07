diphthongs = ['ju', 'ɔɪ', 'eɪ', 'aɪ', 'aʊ', 'oʊ']


def is_diphthong(ipa):
    return ipa in diphthongs


def get_possible_diphthongs(ipa):
    possible_diphthongs = []
    for diphthong in diphthongs:
        if ipa in diphthong:
            possible_diphthongs.append(diphthong)
    return possible_diphthongs


def get_occurrences(string, searched_char):
    return [counter for counter, char in enumerate(string) if char == searched_char]


def get_diphthong(pronunciation, ipa, ipa_pos):
    if ipa == 'j':
        return pronunciation[ipa_pos] + pronunciation[ipa_pos+1]
    if ipa == 'u':
        return pronunciation[ipa_pos-1] + pronunciation[ipa_pos]
    if ipa == 'ɔ':
        return pronunciation[ipa_pos] + pronunciation[ipa_pos+1]
    if ipa == 'ɪ':
        return pronunciation[ipa_pos-1] + pronunciation[ipa_pos]
    if ipa == 'e':
        return pronunciation[ipa_pos] + pronunciation[ipa_pos+1]
    if ipa == 'a':
        return pronunciation[ipa_pos] + pronunciation[ipa_pos+1]
    if ipa == 'ʊ':
        return pronunciation[ipa_pos-1] + pronunciation[ipa_pos]


def has_diphthong(ipa, pronunciation):
    ipa_occurrences = get_occurrences(pronunciation, ipa)
    possible_diphthongs = get_possible_diphthongs(ipa)

    for occurrence in ipa_occurrences:
        for possible_diphthong in possible_diphthongs:
            if possible_diphthong == get_diphthong(pronunciation, ipa, occurrence):
                return True
    return False