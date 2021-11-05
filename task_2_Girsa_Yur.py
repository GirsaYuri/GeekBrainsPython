list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []

for i in list:
    if i.isdigit():
        i = f'{int(i):02d}'
        new_list.append('"')
        new_list.append(i)
        new_list.append('"')
    elif i.strip('+').isdigit():
        new_list.append('"')
        i = i[0] + f'{int(i):02d}'
        new_list.append(i)
        new_list.append('"')
    else:
        new_list.append(i)

print(' '.join(new_list))


