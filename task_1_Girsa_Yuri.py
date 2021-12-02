res = []
with open('ngin_log.txt', 'r', encoding='utf-8') as f:
    for el in f:
        ln = el.split()
        res.append((ln[0], ln[5].strip('"'), ln[6]))
print(res)