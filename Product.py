from Seller import Seller

class Product():
    #возможно нужно добавить id
    def __init__(self, seller: Seller, name: str, price: int, description: str,
                 characteristics: dict, category: str, total_quantity: int):
        self.__seller = seller
        self.__name = name
        self.__price = price
        self.__description = description
        self.__characteristics = characteristics
        self.__category = category
        self.__total_quantity = total_quantity
        self.__rating = 0
        self.__total_assessments = 0

    @property
    def seller(self):
        return self.__seller

    @seller.setter
    def seller(self, seller: str):
        self.__seller = seller

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def characteristics(self):
        return self.__characteristics

    @characteristics.setter
    def characteristics(self, characteristics: dict):
        self.__characteristics = characteristics

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def total_quantity(self):
        return self.__total_quantity

    @total_quantity.setter
    def total_quantity(self, total_quantity: int):
        self.__total_quantity = total_quantity

    @property
    def rating(self):
        return self.__rating

    @property
    def total_assessments(self):
        return self.__total_assessments

    def add_assessment(self, assessment: int):
        if not 0 <= assessment <= 5:
            raise ValueError("An assessment should be from zero to five")
        else:
            # Recalculation of average ratings
            self.__rating = self.__rating*(self.__total_assessments /
                                           (self.__total_assessments + 1)) + \
                            assessment/(self.__total_assessments + 1)
            self.__total_assessments += 1
