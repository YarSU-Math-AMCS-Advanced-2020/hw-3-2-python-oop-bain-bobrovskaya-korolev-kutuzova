class PaymentStrategy:
    def __init__(self):
        pass


class PaymentInCash(PaymentStrategy):
    def __init__(self):
        super().__init__()


class PaymentByCardUponReceipt(PaymentStrategy):
    def __init__(self):
        super().__init__()


class PaymentByCardWhenOrdering(PaymentStrategy):
    def __init__(self):
        super().__init__()
