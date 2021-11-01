# задание 1.
duration = 1731429
#a
if duration // 60 == 0:
    print(duration, 'сек')
#b
elif duration // 3600 == 0:
    min = duration // 60
    sek = duration % 60
    print(min, 'минут', sek, 'секунды')
#с
elif duration // 86400 == 0:
    hour = duration // 3600
    min = (duration // 60) % 60
    sek = duration % 60
    print(hour, 'часов', min, 'минут', sek, 'секунды')
#d
else:
    if duration // 2629743 == 0:
        days = duration // 86400
        hour = (duration // 3600) % 24
        min = (duration // 60) % 60
        sek = duration % 60
        print(days, 'дней', hour, 'часов', min, 'минут', sek, 'секунды')
