def thesaurus(*names):
    global res
    res = {}
    for name in names:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res

thesaurus('Илья', 'Иван', 'Мария', 'Петр', 'Алена', 'Саша')
print(dict(sorted(res.items(), key = lambda x : x[0])))

