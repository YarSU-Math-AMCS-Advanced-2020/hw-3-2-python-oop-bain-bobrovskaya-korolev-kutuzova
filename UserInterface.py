from Product import Product
from Customer import Customer
from Seller import Seller
from ProductDBRequests import ProductDBRequests
from SellerDBRequests import SellerDBRequests
from CustomerDBRequests import CustomerDBRequests
from Address import Address
from Order import Order, OrderStatus
from DeliveryStrategy import choose_delivery, DELIVERY
from typing import List


class UserInterface:
    def __init__(self, product_db: ProductDBRequests,
                 seller_db: SellerDBRequests,
                 customer_db: CustomerDBRequests):

        # data bases
        self.product_db = product_db
        self.seller_db = seller_db
        self.customer_db = customer_db

        # current state
        self.is_sign_in = False
        self.user = None
        self.cur_category = ''
        self.cart_list = list()
        self.order_list = list()

    def home(self):
        """
        Print list of commands that user can type
        """
        commands = ['register', 'sign in', 'sign out', 'create product',
                    'show products', 'select product', 'show cart', 'make order', 'show orders', 'exit']

        print('Available commands: \n\t', end='')
        print(*commands, sep='\n\t')

    def input_address(self) -> Address:
        country = input('Input country for address: ')
        region = input('Input region for address: ')
        locality = input('Input locality for address: ')
        street = input('Input street for address: ')
        index = int(input('Input index for address(int): '))
        house = int(input('Input house for address(int): '))
        flat = int(input('Input flat for address(int): '))

        return Address(country=country,
                       region=region,
                       locality=locality,
                       street=street,
                       index=index,
                       house=house,
                       flat=flat)

    def register(self):
        """
        Ask for user type and then call self.register_customer() or self.register_seller()
        """
        user_type = input('Input user type (customer or seller): ')
        if user_type == 'customer':
            self.register_customer()
        elif user_type == 'seller':
            self.register_seller()
        else:
            print('User type must be customer or seller')

    def register_customer(self):
        """
        Ask for customer info and add new customer to the database
        """
        login = input('Input login for account: ')
        while self.customer_db.is_there_by('login', login):
            print('Customer user with this login already exists')
            login = input('Input login for account: ')

        password = input('Input password for account: ')
        name = input('Input name for account: ')
        email = input('Input email for account: ')
        phone_number = input('Input phone number for account: ')
        address = self.input_address()

        self.customer_db.add_note(Customer(login=login, password=password, name=name,
                                           email=email, phone_number=phone_number,
                                           address=address, idx=login))

    def register_seller(self):
        """
        Ask for seller info and add new seller to the database
        """
        login = input('Input login for account: ')
        while self.seller_db.is_there_by('login', login):
            print('Seller user with this login already exists')
            login = input('Input login for account: ')

        password = input('Input password for account: ')
        name = input('Input name for account: ')
        email = input('Input email for account: ')
        phone_number = input('Input phone number for account: ')
        address = self.input_address()

        self.seller_db.add_note(Seller(login=login, password=password, name=name,
                                       email=email, phone_number=phone_number,
                                       address=address,
                                       main_category="main_category",
                                       rating=0, total_assessments=0, idx=login))

    def sign_in(self):
        """
        Ask user for login/password and set ``self.user`` if this is correct login/password pair
        """
        if self.is_sign_in:
            print('You are already signed in. To sign in in different account sign out first.')
            return

        user_type = input('Input user type (customer or seller): ')
        if user_type not in ['customer', 'seller']:
            print('Wrong user type.')
            return

        login = input('Input login: ')
        password = input('Input password: ')

        if user_type == 'customer' and self.customer_db.is_there_by('login', login):
            self.user = Customer(*self.customer_db.get_note_by_login(login))
        elif user_type == 'seller' and self.seller_db.is_there_by('login', login):
            self.user = Seller(*self.seller_db.get_note_by_login(login))
        else:
            print('User with this login is not registered')
            return

        if self.user.password != password:
            self.user = None
            print('Wrong password. Try again')
            return

        self.is_sign_in = True

    def sign_out(self):
        """
        Sign out of account so user can sign in another account
        """
        if not self.is_sign_in:
            print('You are already signed out.')
            return

        print('You signed out from the account', self.user)
        self.user = None
        self.is_sign_in = False

    def create_product(self):
        """
        (for sellers only) Ask for product info and add it to the database
        """
        if not isinstance(self.user, Seller):
            print("You must be logged as a seller to create a product.")
            return

        name = input("Input the name of your product:")
        price = float(input("Input the price of your product:"))
        description = input("Input the description of your product:")
        characteristics = dict()
        print("Input characteristics of your product (just enter to continue):")
        while 1:
            key = input("Characteristic name:")
            if not key:
                break
            value = input("Characteristic value:")
            characteristics[key] = value

        category = input("Input the category of your product:")
        total_quantity = int(input("Input the total_quantity of your product:"))

        idx = input("Input unique identifier of your product:")
        if self.product_db.is_there_by('idx', idx):
            print('Product with this unique identifier already exists')
            idx = input("Input unique identifier of your product:")

        self.product_db.add_note(
            Product(seller=self.user.login, name=name, price=price,
                    description=description, characteristics=characteristics,
                    category=category, total_quantity=total_quantity,
                    rating=0, total_assessments=0,
                    idx=idx))

    def show_products(self):

        categories = ['All'] + self.product_db.unique('category')
        print('Categories: ', *categories, sep='\n\t', end='\n')

        category = input("Select category: ")

        # select attributes to print
        indexes = [self.product_db.attribute_index('idx'),
                   self.product_db.attribute_index('name'),
                   self.product_db.attribute_index('price'),
                   self.product_db.attribute_index('category'),
                   self.product_db.attribute_index('rating'),
                   self.product_db.attribute_index('total_assessments')]

        # get all notes
        product_notes = self.product_db.get_all_notes()

        # remove notes of other categories
        if category != 'All':
            product_notes = list(filter(lambda x: x[indexes[3]] == category, product_notes))

        # add head of our table
        product_notes = [self.product_db.db_cols] + product_notes

        # select attributes of interest
        product_notes = [[note[i] for i in indexes] for note in product_notes]

        # print everything, applying ljust(18)
        for note in product_notes:
            print(*list(map(lambda x: str(x).ljust(18), note)), sep='')

    def select_product(self):
        product_idx = input("Select product identifier: ")
        product_note = self.product_db.get_note(product_idx)
        if product_note is None:
            print("There is no product with this identifier")
            return

        product = Product(*product_note)
        self.product_info(product)

        choose_type = input('Type \n\t'
                            '"cart" to add the product in cart,\n\t'
                            '"assessment" to add product assessment,\n\t'
                            '"seller" to see the product seller details,\n\t'
                            '"back" to go back: \n\t')
        if choose_type == 'cart':
            self.add_product_in_cart(product)
        elif choose_type == 'assessment':
            self.add_product_assessment(product)
        elif choose_type == 'seller':
            self.seller_info(product.seller)
        else:
            pass

    def seller_info(self, seller: str or Seller):
        if isinstance(seller, str):
            seller = Seller(*self.seller_db.get_note_by_login(seller))

        print('Name: ', seller.name)
        print('Email: ', seller.email)
        print('Phone_number: ', seller.phone_number)
        print('Main category: ', seller.main_category)
        print('Rating: ', seller.rating, 'Total assessments: ', seller.total_assessments)

    def product_info(self, product: str or Product):
        if isinstance(product, str):
            product = Product(*self.product_db.get_note(product))

        print('-----------------------------')
        print('Index: ', product.idx)
        print('Name: ', product.name)
        print('Seller: ', product.seller)
        print('Category: ', product.category)
        print('Price: ', product.price)
        print('Quantity: ', product.total_quantity)
        print('Rating: ', product.rating, 'Total assessments: ', product.total_assessments)
        print('Description:\n', product.description)
        print('Characteristics:')
        for key, value in product.characteristics.items():
            print('\t', key, ":", value)
        print('-----------------------------')

    def add_product_assessment(self, product: str or Product):
        if isinstance(product, str):
            product = Product(*self.product_db.get_note(product))

        if not isinstance(self.user, Customer):
            print("Only logged in customers can add assessments")
            return

        assessment = float(input('Input assessment(from 0 to 5.0): '))

        if not 0. <= assessment <= 5.:
            print("An assessment should be from zero to five")
            return

        product.rating = (product.rating * product.total_assessments + assessment) / (product.total_assessments + 1)
        product.total_assessments += 1

        self.product_db.update(product)

        seller = Seller(*self.seller_db.get_note_by_login(product.seller))
        seller.rating = (seller.rating * seller.total_assessments + assessment) / (seller.total_assessments + 1)
        seller.total_assessments += 1

        self.seller_db.update(seller)

    def add_product_in_cart(self, product: str or Product):
        if isinstance(product, str):
            product = Product(*self.product_db.get_note(product))

        if not isinstance(self.user, Customer):
            print("Only singed in customers can add products in cart.")
            return

        for p, q, a in self.cart_list:
            if p.idx == product.idx:
                print("You have already added this product to the cart")
                return

        quantity = int(input(f"There are {product.total_quantity} items in stock. "
                             f"Select number of items to add in card: "))

        if quantity > product.total_quantity:
            print("You can't add to the cart more product than we have.")
            return

        seller = Seller(*self.seller_db.get_note_by_login(product.seller))
        address = seller.address

        if quantity != 0:
            self.cart_list.append((product, quantity, address))

    def print_order_list(self, order_list: List[Order]):
        print("<Product>".ljust(18), "<Quantity>".ljust(18), "<Total price>".ljust(18), sep='')
        total_price = 0;
        for product, quantity, address in order_list:
            print(product.name.ljust(18), str(quantity).ljust(18),
                  str(product.price * quantity).ljust(18), sep='')
            total_price += product.price * quantity
        print("-" * (18 * 3))
        print("Total (without delivery):".ljust(18 * 2), str(total_price).ljust(18))

    def show_cart(self):
        if len(self.cart_list) == 0:
            print("Your cart is empty.")
            return

        self.print_order_list(self.cart_list)

    def make_order(self):
        if not isinstance(self.user, Customer):
            print('You must be logged in as a customer to create an order')
            return

        if len(self.cart_list) == 0:
            print('To create an order you need to add something to cart.')
            return

        payment_method = input('Input payment method: ')
        destination = self.user.address

        print('Delivery offers:')
        for i in DELIVERY:
            print(f"{i.value}. {i.name.title()} price: "
                  f"{choose_delivery(i)(self.cart_list, destination).price()}")
        delivery_option = int(input('Choose delivery option (input number): '))

        delivery = choose_delivery(DELIVERY(delivery_option))

        for product, quantity, address in self.cart_list:
            if quantity > product.total_quantity:
                print(f"Cannot make order: there are {product.total_quantity} "
                      f"items of {product.name} but the order requires {quantity}.")
                return
        for product, quantity, address in self.cart_list:
            product.total_quantity -= quantity
            self.product_db.update(product)

        self.order_list.append(
            Order(customer=self.user.login, composition=self.cart_list,
                  destination=destination, payment_method=payment_method,
                  delivery=delivery, status=OrderStatus.IN_PROGRESS))

        self.cart_list.clear()

    def show_orders(self):
        if len(self.order_list) == 0:
            print('Your order list is empty')
            return

        order_cnt = 1
        for order in self.order_list:
            print('-' * (18 * 3))
            print('Order number ', order_cnt)
            print('Payment method: ', order.payment_method)
            print('Status: ', order.status)
            print('Total price: ', order.total_price)
            print('Products:\n')
            self.print_order_list(order.composition)

    def menu(self):
        cur_key = 'home'
        while cur_key != 'exit':
            self.home()
            if cur_key == 'home':
                cur_key = input()
            if cur_key == 'register':
                self.register()
            if cur_key == 'sign in':
                self.sign_in()
            if cur_key == 'sign out':
                self.sign_out()
            if cur_key == 'create product':
                self.create_product()
            if cur_key == 'show products':
                self.show_products()
            if cur_key == 'select product':
                self.select_product()
            if cur_key == 'make order':
                self.make_order()
            if cur_key == 'show cart':
                self.show_cart()
            if cur_key == 'show orders':
                self.show_orders()
            if cur_key == 'exit':
                break
            cur_key = 'home'
