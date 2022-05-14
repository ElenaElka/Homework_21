from classes import Store, Shop, Request

if __name__== '__main__':
    request = Request()
    request.from_ = 'склад'
    request.to = 'магазин'
    print(f"Доставить {request.get_amount} {request.get_product} из {request.from_} в {request.to}")



    #store = Store()
    #print(store.get_unique_items_count)



    #shop = Shop()
    #print(shop.limit)
    #print(shop.get_limit)





