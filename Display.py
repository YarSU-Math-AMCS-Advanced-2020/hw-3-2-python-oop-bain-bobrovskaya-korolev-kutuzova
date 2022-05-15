from ProductDBRequests import ProductDBRequests


class Display:
    def __init__(self, __products_db: ProductDBRequests):
        self.__products_db = __products_db

    def all_products(self):
        products_idx = list()
        # Print idx, name, price
        print(self.__products_db.db_cols[9], self.__products_db.db_cols[1],
              self.__products_db.db_cols[2])
        for note in self.__products_db.get_all():
            products_idx.append(note[9])
            # Print idx, name, price, is index from
            # ProductDBRequests.__db_cols
            print(note[9], note[1], note[2])
        return products_idx

    def categories(self):
        uniq_category = set()
        for note in self.__products_db.get_all():
            # Added category, is index from ProductDBRequests.__db_cols
            uniq_category.add(note[5])
        print('Categories:')
        for category in uniq_category:
            print(category)
        return uniq_category

    def products_by_category(self, category: str):
        products_idx_by_category = list()
        # Print idx, name, price
        print(self.__products_db.db_cols[9], self.__products_db.db_cols[1],
              self.__products_db.db_cols[2])
        for note in self.__products_db.get_all():
            # Print idx, name, price, is index from
            if note[5] == category:
                products_idx_by_category.append(note[9])
                print(note[9], note[1], note[2])
        return products_idx_by_category

    def product(self, idx: str):
        product = self.__products_db.get_note(idx)
        if len(product) > 0:
            print('Index: ', product[9])
            print('Name: ', product[1])
            print('Seller: ', product[0])
            print('Category: ', product[5], 'Price: ', product[2])
            print('Quantity: ', product[6])
            print('Rating: ', product[7], 'Total assessments: ', product[8])
            print('Description:\n', product[8])
            print('Characteristics:')
            for key, val in product[4]:
                print(key,' : ', val)
        return product
