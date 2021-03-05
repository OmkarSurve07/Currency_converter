from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("Enter the Amount :"))
from_currency = input("from Currency :").upper()
to_currency = input("to Currency").upper()

print(from_currency,"To",to_Currency,amount)
result = c.convert(from_currency,to_currency,amount)

print(result)
