def conjugate(verb):
    inf = verb[-2:]
    rad = verb[:-2]
    ret = {}
    ar = ['o', 'as', 'a', 'amos', 'ais', 'an']
    er = ['o', 'es', 'e', 'emos', 'eis', 'en']
    ir = ['o', 'es', 'e', 'imos', 'is', 'en']
    choice = ar if inf == 'ar' else er if inf == 'er' else ir if inf == 'ir' else ''
    ret[verb] = list(map(lambda x: rad + x, choice))
    return ret






