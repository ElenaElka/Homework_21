from abc import abstractmethod


class Storage:

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass



class Store(Storage):
    def __init__(self, capacity=100):
        self.items = {}
        self.capacity = capacity

    """Увеличивает запас items"""
    def add(self, name, quantity):
        availability = False
        if self.get_free_space() > quantity:
            for item in self.items.item():
                if name == item:
                    self.items[item] = self.items[item] + quantity
                    availability = True
            if not availability:
                self.items[item] = quantity
            print("Товар добавлен")
        else:
            print ("Товар не может быть добавлен. Cвободное место закончилось")



    """Уменьшает запас items"""
    def remove(self, name, quantity):
        for item in self.items.item():
            if name == item:
                if self.items[item] - quantity >= 0:
                    self.items[item] = self.items[item] - quantity
                else:
                    print(f"{name} не достаточно на складе")
            else:
                print(f"{name} на складе не найден")

    """Возвращает количество свободных мест"""
    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    """Возвращает содержание склада в словаре {товар: количество}"""
    def get_items(self):
        return self.items

    """Возвращает количество уникальных товаров"""
    def get_unique_items_count(self):
        return len(self.items.item())



class Shop(Store):
    def __init__(self, capacity=20, limit=5):
        super().__init__()
        self.capacity = capacity
        self.limit = limit

    """Увеличивает запас items"""
    def add(self, name, quantity):
       if self.get_unique_items_count() < self.limit:
           super().add(name, quantity)
       else:
          print ("Товар не может быть добавлен, cвободное место закончилось!")



class Request:
    def __init__(self, from_:str, to:str, amount=0):
        self.from_ = from_
        self.to = to
        self.amount = amount
        self.product = ""

    #@set_amount.setter
    #def set_amount(self, amount):
    #    self.amount == amount

    @property
    def get_amount(self):
        return self.amount

   # @set_product.setter
   # def set_product(self, product):
   #     return self._product = product

    @property
    def get_product(self):
        return self.product

    def __repr__(self):
        return f"Доставить {self.get_amount} {self.get_product} из {self.get_from_} в {self.get_to}"