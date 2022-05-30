from ProductDBRequests import ProductDBRequests
from SellerDBRequests import SellerDBRequests
from Product import Product


class Display:
    def __init__(self, products_db: ProductDBRequests,
                 seller_db: SellerDBRequests):
        self.products_db = products_db
        self.seller_db = seller_db
        
    def all_products(self):
        products_idx = list()
        # Print idx, name, price, category, rating, total assessments
        print(self.products_db.db_cols[9], self.products_db.db_cols[1],
              self.products_db.db_cols[2], self.products_db.db_cols[5],
              self.products_db.db_cols[7], self.products_db.db_cols[8])
        for note in self.products_db.get_all_notes():
            products_idx.append(note[9])
            # Print idx, name, price, category, rating, total assessments
            # (index from ProductDBRequests.__db_cols)
            print(note[9], note[1], note[2], note[5], note[7], note[8])
        return products_idx

    def categories(self):
        uniq_category = set()
        for note in self.products_db.get_all_notes():
            # Added category, is index from ProductDBRequests.__db_cols
            uniq_category.add(note[5])
        print('Categories:')
        for category in uniq_category:
            print(category)
        return uniq_category

    def products_by_category(self, category: str):
        products_idx_by_category = list()
        # Print idx, name, price, rating, total assessments
        print(self.products_db.db_cols[9], self.products_db.db_cols[1],
              self.products_db.db_cols[2], self.products_db.db_cols[7],
              self.products_db.db_cols[8])
        for note in self.products_db.get_all_notes():
            # Print idx, name, price, rating, total assessments,(index from
            # ProductDBRequests.__db_cols)
            if note[5] == category:
                products_idx_by_category.append(note[9])
                print(note[9], note[1], note[2], note[7], note[8])
        return products_idx_by_category

    def product_from_list(self, product_list):
        if len(product_list) == 0:
            print('Cart is empty')
        else:
            product_cnt = 1
            for product in product_list:
                print('\nProduct number ', product_cnt)
                self.product(product.idx)
                product_cnt += 1

    def seller_by_product(self, product_idx: str):
        product = self.products_db.get_note(str(product_idx))
        seller = self.seller_db.get_note_by_login(str(product[0]))
        if len(seller) > 0:
            print('Name: ', seller[2])
            print('Email: ', seller[3])
            print('Phone_number: ', seller[4])
            print('Main category: ', seller[7])
            print('Rating: ', seller[8], 'Total assessments: ', seller[9])
        return seller
