# Домашнее задание по теме "Режимы открытия файлов"

class Product:
    def __init__(self, name, weight, category):
        self.name = name  # название продукта (строка)
        self.weight = weight  # общий вес товара (дробное число) (5.4, 52.8 и т.п.)
        self.category = category  # категория товара (строка)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, "r")
            string = file.read()
            file.close()
        except FileNotFoundError:
            string = ""
        return string

    def add(self, *products):
        for prod in products:
            if not str(prod) in self.get_products():  # проверить есть ли в магазине
                file = open(self.__file_name, "a")
                string = file.write(f"{prod}\n")
                file.close()
            else:
                print(f"Продукт {prod} уже есть в магазине")


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
