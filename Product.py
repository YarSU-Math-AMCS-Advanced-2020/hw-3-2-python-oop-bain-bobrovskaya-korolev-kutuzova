from ProductDBRequests import ProductDBRequests
from Seller import Seller


class Product:
    def __init__(self, seller: Seller, name: str, price: int,
                 description: str, characteristics: dict, category: str,
                 total_quantity: int, rating: float = 0,
                 total_assessments: int = 0, db: ProductDBRequests = None,
                 idx=None):
        # Suppose that parameters were given as db columns
        self.__seller = seller
        self.__name = name
        self.__price = price
        self.__description = description
        self.__characteristics = characteristics
        self.__category = category
        self.__total_quantity = total_quantity
        self.__rating = rating
        self.__total_assessments = total_assessments
        self.__idx = idx
        if idx is None:
            db.add_note(self)

    @property
    def idx(self):
        return self.__idx

    # Should only be used in DBRequests
    @idx.setter
    def idx(self, idx: str):
        self.__idx = idx

    @property
    def seller(self):
        return self.__seller

    @property
    def name(self):
        return self.__name

    def set_name(self, name: str, db: ProductDBRequests):
        self.__name = name
        db.update_attribute(self.__idx, 'name', name)

    @property
    def price(self):
        return self.__price

    def set_price(self, price: int, db: ProductDBRequests):
        self.__price = price
        db.update_attribute(self.__idx, 'price', price)

    @property
    def description(self):
        return self.__description

    def set_description(self, description: str, db: ProductDBRequests):
        self.__description = description
        db.update_attribute(self.__idx, 'description', description)

    @property
    def characteristics(self):
        return self.__characteristics

    def set_characteristics(self, characteristics: dict,
                            db: ProductDBRequests):
        self.__characteristics = characteristics
        db.update_attribute(self.__idx, 'characteristics', characteristics)

    @property
    def category(self):
        return self.__category

    def set_category(self, category: str, db: ProductDBRequests):
        self.__category = category
        db.update_attribute(self.__idx, 'category', category)

    @property
    def total_quantity(self):
        return self.__total_quantity

    def set_total_quantity(self, total_quantity: int, db: ProductDBRequests):
        self.__total_quantity = total_quantity
        db.update_attribute(self.__idx, 'total_quantity', total_quantity)

    @property
    def rating(self):
        return self.__rating

    @property
    def total_assessments(self):
        return self.__total_assessments

    def add_assessment(self, assessment: int, db: ProductDBRequests):
        if not 0 <= assessment <= 5:
            raise ValueError("An assessment should be from zero to five")
        else:
            # Recalculation of average ratings
            self.__rating = self.__rating * (self.__total_assessments /
                                             (self.__total_assessments + 1)) + \
                            assessment / (self.__total_assessments + 1)
            self.__total_assessments += 1
            db.update_attribute(self.__idx, 'total_assessment',
                                self.__total_assessments)
            db.update_attribute(self.__idx, 'rating', self.__rating)
            # self.__seller.rating = (self.__seller.rating * self.__seller.total_assessments + assessment) / (
            #        self.__seller.total_assessments + 1)
            # self.__seller.total_assessments += 1
