#a
list_cub = []

for i in range(1,100):
   if i % 2 != 0:
       list_cub.append(i**3)

res = 0
for a in range(len(list_cub)):
    sum_cubs = 0
    cub_list = list_cub[a]
    while cub_list > 0:
        sum_cubs += cub_list % 10
        cub_list = cub_list // 10
    if sum_cubs % 7 == 0:
        res += (list_cub[a])
print(f'сумма чисел из списка {res}')

#b

res = 0
for a in range(len(list_cub)):
    list_cub[a] += 17
    sum_cubs = 0
    cub_list = list_cub[a]
    while cub_list > 0:
        sum_cubs += cub_list % 10
        cub_list = cub_list // 10
    if sum_cubs % 7 == 0:
        res += (list_cub[a])
print(f'сумма чисел увеличенных на 17: {res}')

