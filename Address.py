class Address:
    """
    Container class for addresses

    Attributes
    ----------
    country : str
    region : str
    locality : str
    street : str
    index : str
    house : str
    flat : str
    """

    def __init__(self, country: str, region: str, locality: str, street: str,
                 index: int, house: int, flat: int):
        self.country = country
        self.region = region
        self.locality = locality
        self.street = street
        self.index = index
        self.house = house
        self.flat = flat
