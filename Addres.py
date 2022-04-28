class Addres():
    def __init__(self, country: str, region: str, locality: str, street: str,
                 index: int, house: int, flat: int):
        self.__country = country
        self.__region = region
        self.__locality = locality
        self.__street = street
        self.__index = index
        self.__house = house
        self.__flat = flat

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region: str):
        self.__region = region

    @property
    def locality(self):
        return self.__locality

    @locality.setter
    def locality(self, locality: str):
        self.__locality = locality

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, house: str):
        self.__house = house

    @property
    def flat(self):
        return self.__flat

    @flat.setter
    def flat(self, flat: str):
        self.__flat = flat
