def show_price(items, show_delim = True):
    for price in items:
        price = int(round(price*100))
        rubles = price // 100
        cent = price % 100
        print(f'{rubles:02d} руб {cent:02d} коп', end=',')
    if show_delim:
        print()
price = [222, 333, 444, 555.55, 66.6, 7777]

show_price(price)
price.sort()
show_price(price)
prices_desc = sorted(price, reverse=True)
show_price(prices_desc)
show_price(prices_desc[4::-1], False)