

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    special_offers = {
        '3A': 130,
        '2B': 45
    }
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
        if f'{str(count)}{item}' in special_offers:
            total += special_offers[f'{str(count)}{item}']
        else:
            total += prices[item] * count

    return total
