

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Assumes string in form '3A 2B'
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

    try:
        for sku in skus.split():
            if sku in special_offers:
                total += special_offers[sku]
            elif sku[1] in prices:
                total += (prices[sku[1]] * sku[0])
            else:
                return -1
    except Exception:
        return -1
    else:
        return total

