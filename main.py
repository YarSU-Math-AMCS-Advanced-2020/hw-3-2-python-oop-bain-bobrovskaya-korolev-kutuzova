from ProductDBRequests import ProductDBRequests
from UserInterface import UserInterface
from SellerDBRequests import SellerDBRequests
from CustomerDBRequests import CustomerDBRequests

product_db = ProductDBRequests()
seller_db = SellerDBRequests()
customer_db = CustomerDBRequests()
i = UserInterface(product_db, seller_db, customer_db)
i.menu()
