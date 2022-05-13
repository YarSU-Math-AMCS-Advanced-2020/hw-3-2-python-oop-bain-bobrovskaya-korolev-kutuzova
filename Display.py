from ProductDBRequests import ProductDBRequests


class Display:
    def __init__(self, products_db: ProductDBRequests):
        self.products_db = products_db

    def products(self):
        # Print idx, name, price
        print(self.products_db.db_cols[9], self.products_db.db_cols[1],
              self.products_db.db_cols[2])
        for note in self.products_db.get_all():
            # Print idx, name, price, is index from
            # ProductDBRequests.__db_cols
            print(note[9], note[1], note[2])

    def categories(self):
        uniq_category = set()
        for note in self.products_db.get_all():
            # Added category, is index from ProductDBRequests.__db_cols
            uniq_category.add(note[5])
        print('Categories:')
        for category in uniq_category:
            print(category)
