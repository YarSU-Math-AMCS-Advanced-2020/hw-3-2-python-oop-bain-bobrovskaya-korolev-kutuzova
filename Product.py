from Utils import str2dict


class Product:
    def __init__(self, seller: str, name: str, price: float,
                 description: str, characteristics: dict, category: str,
                 total_quantity: int, rating: float = 0,
                 total_assessments: int = 0, idx=None):
        # Suppose that parameters were given as db columns
        self.seller = seller
        self.name = name
        self.price = price
        self.description = description
        if isinstance(characteristics, str):
            self.characteristics = str2dict(characteristics)
        else:
            self.characteristics = characteristics
        self.category = category
        self.total_quantity = total_quantity
        self.rating = rating
        self.total_assessments = total_assessments
        self.idx = idx
