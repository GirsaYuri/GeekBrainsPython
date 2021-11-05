list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_iter = iter(list)

count = 0

for i in list_iter:
     if i.isdigit():
        list.remove(i)
        i = f'{int(i):02d}'
        list.insert(count, '"')
        list.insert(count+1, i)
        list.insert(count + 2, '"')
        count += 2
        next(list_iter)
     elif i.strip('+-').isdigit():
        list.remove(i)
        i = i[0] + f'{int(i):02d}'
        list.insert(count, '"')
        list.insert(count+1, i)
        list.insert(count + 2, '"')
        count += 2
        next(list_iter)
     else:
        count += 1
print(' '.join(list))


