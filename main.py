import dao


for n in dao.get_all_product():
    print(n.price)
