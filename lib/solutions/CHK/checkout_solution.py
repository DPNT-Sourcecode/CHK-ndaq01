

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }
    basket = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }
    total = 0

    for sku in list(skus):
        if sku in prices:
            basket[sku] += 1
        else:
            return -1

    for item, count in basket.items():
        if item == 'A':
            divisions, remainder = divmod(count, 3)
            total += (divisions * 130 + remainder * prices[item])
        elif item == 'B':
            divisions, remainder = divmod(count, 2)
            total += (divisions * 45 + remainder * prices[item])
        else:
            total += prices[item] * count

    return total
