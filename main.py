# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
#
# class CurrencyConverter:
#     def __init__(self, exchange_rate):
#         if not isinstance(exchange_rate, Decimal):
#             raise ValueError("Ayirboshlash kursi o'nlik tipda bo'lishi kerak.")
#         self.exchange_rate = exchange_rate
#     def convert(self, amount):
#         if not isinstance(amount, (int, Decimal)):
#             raise ValueError("Miqdor butun yoki o'nlik bo'lishi kerak.")
#         converted_amount = amount * self.exchange_rate
#         day_offset = random.randint(-30, 30)
#         conversion_date = datetime.now() + timedelta(days=day_offset)
#         return converted_amount, conversion_date.strftime("%Y-%m-%d")
# if __name__ == "__main__":
#     exchange_rate = Decimal('12820')
#     converter = CurrencyConverter(exchange_rate)
#     try:
#         user_input = input("USD miqdorini kiriting: ")
#         amount_to_convert = Decimal(user_input)
#         result, date = converter.convert(amount_to_convert)
#         print(f"{amount_to_convert} USD = {result} UZS (Sana: {date})")
#     except ValueError as e:
#         print(f"Xato: {e}")

# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
#
# class Mahsulot:
#     def __init__(self, narx: Decimal):
#         if narx < 0:
#             raise ValueError("Narx manfiy bo'lishi mumkin emas.")
#
#         self.narx = narx
#         self.chegirma = random.randint(1, 50)
#         self.xarid_sana = self.generate_random_date()
#
#     def generate_random_date(self):
#         days_offset = random.randint(-30, 0)
#         return datetime.now() + timedelta(days=days_offset)
#
#     def yangi_narx(self):
#         if self.chegirma < 1 or self.chegirma > 50:
#             raise ValueError("Chegirma noto'g'ri hisoblangan.")
#
#         chegirma_miqdori = (Decimal(self.chegirma) / Decimal(100)) * self.narx
#         yangi_narx = self.narx - chegirma_miqdori
#         return yangi_narx
#
#     def __str__(self):
#         return (f"Mahsulot narxi: {self.narx} UZS, "
#                 f"Chegirma: {self.chegirma}%, "
#                 f"Yangi narx: {self.yangi_narx()} UZS (Sana: {self.xarid_sana.strftime('%Y-%m-%d')})")
#
# try:
#     mahsulot = Mahsulot(Decimal('100000'))
#     print(mahsulot)
# except ValueError as e:
#     print(f"Xato: {e}")