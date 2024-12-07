import random
from decimal import Decimal
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, exchange_rate):
        if not isinstance(exchange_rate, Decimal):
            raise ValueError("Ayirboshlash kursi o'nlik tipda bo'lishi kerak.")
        self.exchange_rate = exchange_rate
    def convert(self, amount):
        if not isinstance(amount, (int, Decimal)):
            raise ValueError("Miqdor butun yoki o'nlik bo'lishi kerak.")
        converted_amount = amount * self.exchange_rate
        day_offset = random.randint(-30, 30)
        conversion_date = datetime.now() + timedelta(days=day_offset)
        return converted_amount, conversion_date.strftime("%Y-%m-%d")
if __name__ == "__main__":
    exchange_rate = Decimal('12820')
    converter = CurrencyConverter(exchange_rate)
    try:
        user_input = input("USD miqdorini kiriting: ")
        amount_to_convert = Decimal(user_input)
        result, date = converter.convert(amount_to_convert)
        print(f"{amount_to_convert} USD = {result} UZS (Sana: {date})")
    except ValueError as e:
        print(f"Xato: {e}")