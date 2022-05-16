from ProductDBRequests import ProductDBRequests
from Display import Display
from UserInterface import UserInterface
from AddresDBRequests import AddresDBRequests
from SellerDBRequests import SellerDBRequests
from CustomerDBRequests import CustomerDBRequests

product_db = ProductDBRequests()
addres_db = AddresDBRequests()
seller_db = SellerDBRequests()
customer_db = CustomerDBRequests()
display = Display(product_db, seller_db)
i = UserInterface(display, product_db, seller_db, customer_db, addres_db)
i.menu()
