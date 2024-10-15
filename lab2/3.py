def del_all_e(s, e):
    if not s:
        return ''
    elif s[0] == e:
        return del_all_e(s[1:], e)
    else:
        return s[0] + del_all_e(s[1:], e)


test_strings = [
    ("мама мыла раму", "а"),
    ("hello world", "l"),
    ("абракадабра", "б"),
    ("1234567890", "5"),
    ("", "a"),
    ("aaaaa", "a")
]

for s, e in test_strings:
    result = del_all_e(s, e)
    print(f"del_all_e('{s}', '{e}') = '{result}'")

