from typing import Dict


class Product:
    """
    Container class for products

    Attributes
    ----------
    seller : str
        seller login
    name : str
        name of the product
    price : float
        price of the product
    description : str
        full description of the product
    characteristics : Dict[str, str]
        each key is characteristic name, corresponding value is characteristic itself
    category : str
    total_quantity : int
    rating : float
    total_assessments : int
    idx : str
        unique identifier of the product
    """

    def __init__(self, seller: str, name: str, price: float,
                 description: str, characteristics: Dict[str, str], category: str,
                 total_quantity: int, rating: float = 0,
                 total_assessments: int = 0, idx: str = None):
        """
        Parameters
        ----------
        seller : str
            seller login
        name : str
            name of the product
        price : float
            price of the product
        description : str
            full description of the product
        characteristics : Dict[str, str]
            each key is characteristic name, corresponding value is characteristic itself
        category : str
        total_quantity : int
        rating : float
        total_assessments : int
        idx : str
            unique identifier of the product
        """
        # Suppose that parameters were given as db columns
        self.seller = seller
        self.name = name
        self.price = price
        self.description = description
        if isinstance(characteristics, str):
            self.characteristics = eval(characteristics)
        else:
            self.characteristics = characteristics
        self.category = category
        self.total_quantity = total_quantity
        self.rating = rating
        self.total_assessments = total_assessments
        self.idx = idx
