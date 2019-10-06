

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
    total = 0

    basket = {}

    for sku in list(skus):
        if sku in prices:
            basket['sku'] += 1

        elif sku[1] in prices:
            total += (prices[sku[1]] * sku[0])
        else:
            return -1

        return total


