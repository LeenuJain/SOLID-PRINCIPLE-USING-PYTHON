class CurrencyConvert:
    def __init__(self, rupees, curr_type):
        self.rupees = rupees
        self.currency_type = curr_type
        self.rates = {
            'Doller': 94.03,
            'Yuro': 83.00,
            'Yen': 45.67
        }

    def currency_convertor(self):
        converted = self.rupees / self.rates[self.currency_type]
        return converted, self.currency_type


class DisplayCurrency:
    @staticmethod
    def display_currency(convert_object):
        # Access the instance method of CurrencyConvert
        converted, curr_type = convert_object.currency_convertor()
        print(f"Converted INR to {curr_type}, amount is {converted}")


# Test the code
convert_object = CurrencyConvert(10000, 'Doller')
DisplayCurrency.display_currency(convert_object)
