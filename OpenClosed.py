# open closed principle
class PaymentMethod:
    def make_payment(self, pay_type, amount):
        if pay_type == 'UPI':
            print(f"Payment {amount} done on UPI")
        elif pay_type == 'Net Banking':
            print(f"Payment {amount} done on Net Banking")
        elif pay_type == 'Credit Card':
            print(f"Payment {amount} done on Credit Card")
        else:
            print(f"Unsupported Payment Method")

if __name__ == "__main__":
    payment_obj = PaymentMethod()
    payment_obj.make_payment("Credit Card", 10000)