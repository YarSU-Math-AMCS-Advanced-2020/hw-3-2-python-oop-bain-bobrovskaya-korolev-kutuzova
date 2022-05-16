from Display import Display
from Product import Product, create_product
from Customer import Customer, create_customer
from Seller import Seller, create_seller
from ProductDBRequests import ProductDBRequests
from SellerDBRequests import SellerDBRequests
from CustomerDBRequests import CustomerDBRequests
from AddresDBRequests import AddresDBRequests
from Addres import Addres, create_addres
from Order import Order
from DeliveryStrategy import YandexDelivery, SberDelivery, PostDelivery, \
    yandex_price, sber_price, post_price, choose_delivery


class UserInterface:
    def __init__(self, display: Display, product_db: ProductDBRequests,
                 seller_db: SellerDBRequests,
                 customer_db: CustomerDBRequests,
                 addres_db: AddresDBRequests):
        self.__display = display
        self.__cur_category = ''
        self.__product_db = product_db
        self.__seller_db = seller_db
        self.__customer_db = customer_db
        self.__addres_db = addres_db
        self.__is_sign_in = False
        self.__customer = None
        self.__seller = None
        self.__product_list = list()
        self.__order_list = list()

    def create_order(self):
        if self.__customer is None:
            print('You must be logged in as a customer')
            if len(self.__product_list) == 0:
                print('Cart is empty')
        if self.__customer is not None and len(self.__product_list) != 0:
            payment_method = input('Input payment method: ')
            print('Yandex, price: ', yandex_price)
            print('Sber, price: ', sber_price)
            print('Post, price: ', post_price)
            delivery_name = input('Input delivery name: ')
            delivery = choose_delivery(delivery_name)
            self.__order_list.append(
                self.__customer.make_order(self.__product_list.copy(),
                                           payment_method, delivery))

    def create_product_by_raw(self, product):
        if self.__customer is not None:
            seller_raw = self.__seller_db.get_note_by_login(product[0])
            seller = Seller(*seller_raw[:5], str(seller_raw[6]),
                            *seller_raw[7:-1],
                            self.__addres_db,
                            self.__seller_db,
                            seller_raw[-1])
        return Product(seller, *product[1:-1], db=self.__product_db,
                       idx=product[-1])

    def product_in_cart(self, product_idx: str):
        product_raw = self.__display.product(product_idx)
        if self.__customer is not None:
            product = self.create_product_by_raw(product_raw)
            if product.total_quantity > 0:
                product.set_total_quantity(product.total_quantity - 1,
                                           self.__product_db)
                self.__product_list.append(product)
            else:
                print('Product is out of stock')

    def add_product_assessment(self, product_idx: str):
        product_raw = self.__display.product(product_idx)
        if self.__customer is not None:
            product = self.create_product_by_raw(product_raw)
            assessment = int(input('Input assessment(int): '))
            product.add_assessment(assessment, self.__product_db,
                                   self.__seller_db)

    def product_seller(self, product_idx: str):
        self.__display.seller_by_product(product_idx)

    def process_product_case(self, product_idx: str):
        self.__display.product(product_idx)
        choose_type = input('Choose "add" to add product in cart, '
                            '"assessment" to add product assessment,'
                            '"seller" to see product seller: ')
        if choose_type == 'add':
            self.product_in_cart(product_idx)
        elif choose_type == 'assessment':
            self.add_product_assessment(product_idx)
        elif choose_type == 'seller':
            self.product_seller(product_idx)

    def menu(self):
        cur_key = ''
        while cur_key != 'exit':
            print('\nEnter: "home" to return to the main page, \n'
                  '"sign in" to sign in,\n'
                  '"sign out" to sign out, \n'
                  '"create" to create an account, \n'
                  '"categories" to list all categories, \n'
                  '"products" to list all products, \n'
                  '"exit" to exit\n'
                  '"make order" to make order\n'
                  '"create product" to create product\n'
                  '"order list" to see a list of your orders\n'
                  '"cart" to see current cart')
            if cur_key == '' or cur_key == 'home':
                cur_key = input()
            if cur_key == 'sign in':
                user_type = input('Input user type- customer or seller: ')
                login = input('Input login: ')
                password = input('Input password: ')
                if user_type == 'customer':
                    customer = self.__customer_db.get_note_by_login(login)
                    if self.__customer_db.check_similar_login(login):
                        self.__customer = Customer(*customer[:5],
                                                   str(customer[6]),
                                                   self.__addres_db,
                                                   self.__customer_db,
                                                   customer[-1])
                        if self.__customer is not None:
                            self.__is_sign_in = True
                elif user_type == 'seller':
                    seller = self.__seller_db.get_note_by_login(login)
                    if self.__seller_db.check_similar_login(login):
                        #print(*seller[:5], str(seller[6]), seller[-1])
                        self.__seller = Seller(*seller[:5], str(seller[6]),
                                               *seller[7:-1],
                                               self.__addres_db,
                                               self.__seller_db,
                                               seller[-1])
                        if self.__seller is not None:
                            self.__is_sign_in = True
                        #print(1)
            if cur_key == 'create' and not self.__is_sign_in:
                user_type = input('Input user type- customer or seller: ')
                addres = create_addres(self.__addres_db)
                if user_type == 'customer' and not self.__is_sign_in:
                    self.__customer = create_customer(
                        str(self.__addres_db.get_last_note()[-1]),
                        self.__addres_db, self.__customer_db)
                    if self.__customer is not None:
                        self.__is_sign_in = True
                elif user_type == 'seller' and not self.__is_sign_in:
                    self.__seller = create_seller(
                        str(self.__addres_db.get_last_note()[-1]),
                        self.__addres_db, self.__seller_db
                    )
                    if self.__seller is not None:
                        self.__is_sign_in = True
               # print(1)
            if cur_key == 'categories':
                categories = self.__display.categories()
                self.__cur_category = input('Choose a category: ')
                if self.__cur_category in categories:
                    products_idx_by_category = \
                        self.__display.products_by_category(
                            self.__cur_category)
                    product_idx = input('Choose a product index: ')
                    if product_idx in products_idx_by_category:
                        self.process_product_case(product_idx)
                        print(1)
            if cur_key == 'products':
                products_idx = self.__display.all_products()
                product_idx = input('Choose a product index: ')
                if product_idx in products_idx:
                    self.process_product_case(product_idx)
                    print(1)
            if cur_key == 'make order':
                self.create_order()
                self.__product_list.clear()
                print(1)
            if cur_key == 'create product':
                if self.__seller is not None:
                    create_product(self.__seller, self.__product_db)
                    print(1)
                else:
                    print('You must be logged in as a seller')
            if cur_key == 'sign out':
                if not self.__is_sign_in:
                    print('You are not authorized')
                else:
                    self.__customer = None
                    self.__seller = None
                    self.__is_sign_in = False
                    self.__product_list.clear()
                    self.__order_list.clear()
            if cur_key == 'order list':
                if len(self.__order_list) == 0:
                    print('Your order list is empty')
                else:
                    order_cnt = 1
                    for order in self.__order_list:
                        print('Order number ', order_cnt)
                        print('Payment method: ', order.payment_method)
                        print('Status: ', order.status)
                        print('Total price: ', order.total_price)
                        self.__display.product_from_list(order.composition)
                        order_cnt += 1
            if cur_key == 'cart':
                self.__display.product_from_list(self.__product_list)
            if cur_key == 'exit':
                break
            cur_key = ''
