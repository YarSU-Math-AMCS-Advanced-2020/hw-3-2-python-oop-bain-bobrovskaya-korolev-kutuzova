from ProductDBRequests import ProductDBRequests
from Display import Display
from UserInterface import UserInterface
from AddressDBRequests import AddressDBRequests
from SellerDBRequests import SellerDBRequests
from CustomerDBRequests import CustomerDBRequests

product_db = ProductDBRequests()
address_db = AddressDBRequests()
seller_db = SellerDBRequests()
customer_db = CustomerDBRequests()
display = Display(product_db, seller_db)
i = UserInterface(display, product_db, seller_db, customer_db, address_db)
i.menu()
