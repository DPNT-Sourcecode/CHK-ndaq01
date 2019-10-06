
BASE_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}

def _get_special_price(count, deal_count, deal_price, base_price):
    divisions, remainder = divmod(count, deal_count)
    return divisions * deal_price + remainder * base_price


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
    }
    total = 0

    for sku in list(skus):
        if sku in BASE_PRICES:
            basket[sku] += 1
        else:
            return -1

    for item, count in basket.items():
        if item == 'E':
            divisions, remainder = divmod(count, 2)
            if divisions >= basket['B']:
                basket['B'] = 0
            else:
                basket['B'] -= divisions
        if item == 'A':
            price_1 = _get_special_price(count, 3, 130, BASE_PRICES[item])
            price_2 = _get_special_price(count, 5, 200, BASE_PRICES[item])
            total += min(price_1, price_2)
        elif item == 'B':
            divisions, remainder = divmod(count, 2)
            total += (divisions * 45 + remainder * BASE_PRICES[item])
        else:
            total += BASE_PRICES[item] * count

    return total



