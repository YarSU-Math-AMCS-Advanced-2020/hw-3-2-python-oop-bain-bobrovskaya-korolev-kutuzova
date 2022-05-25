from AddressDBRequests import AddressDBRequests


class Address:
    def __init__(self, country: str, region: str, locality: str, street: str,
                 index: int, house: int, flat: int, db: AddressDBRequests,
                 idx=None):
        self.country = country
        self.region = region
        self.locality = locality
        self.street = street
        self.index = index
        self.house = house
        self.flat = flat
        self.idx = idx
        if idx is None:
            db.add_note(self)


def create_address(db: AddressDBRequests):
    country = input('Input country for address: ')
    region = input('Input region for address: ')
    locality = input('Input locality for address: ')
    street = input('Input street for address: ')
    index = int(input('Input index for address(int): '))
    house = int(input('Input house for address(int): '))
    flat = int(input('Input flat for address(int): '))
    return Address(country, region, locality, street, index, house, flat, db)
