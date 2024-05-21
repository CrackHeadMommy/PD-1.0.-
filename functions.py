def add(stock, adding):
    for item in stock:
        if item.name == adding.name:
            item.add(adding.amount)
            return stock
    stock.append(adding)
    return stock

def remove(stock, removing_name, removing_amount):
    for item in stock:
        if item.name == removing_name:
            item.amount -= int(removing_amount)
            if item.amount <= 0:
                stock.remove(item)
            return stock
    return stock
