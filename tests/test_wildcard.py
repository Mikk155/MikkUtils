from MikkUtils.__init__ import wildcard

dic = {
    "match_0": "match_0",
    "match_1": "*atch_1",
    "match_2": "match_*",
    "match_3": "ma*ch_3",
    "match_4": "ma*ch_*",
    "match_5": "*a*ch_5",
    "match_6": "*a*ch_*",
    "match_7": "*a*c*_*",
}

for k, v in dic.items():
    print(f'{k} -> {v} == {str(wildcard(k, v))}')
