

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    special_offers = {
        '3A': 130,
        '2B': 45
    }
    total = 0
    # Assumes string in form '3A 2B'
    for sku in skus.split():
        if sku in special_offers:
            total += special_offers[sku]
        else
