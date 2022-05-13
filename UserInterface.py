from ProductDBRequests import ProductDBRequests


class UserInterface:
    def __init__(self, products_db: ProductDBRequests):
        self.products_db = products_db

    def display_products(self):
        # Print idx, name, price
        print(self.products_db.db_cols[9], self.products_db.db_cols[1],
              self.products_db.db_cols[2])
        for note in self.products_db.get_all():
            # Print idx, name, price
            print(note[9], note[1], note[2])
