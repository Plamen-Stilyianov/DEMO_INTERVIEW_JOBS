import datetime

store = [(10, 'hats', datetime.datetime(2021, 11, 30)),
         (20, 'socks', datetime.datetime(2021, 11, 30)),
         (30, 'shirts', datetime.datetime(2021, 11, 30)),
         (40, 'glaves', datetime.datetime(2021, 11, 30))]

orders = {item[0]: (item[1], item[2]) for item in store}


def get_perchase_item(id):
    if id in orders.keys():
        return orders[id]


print(get_perchase_item(20))
