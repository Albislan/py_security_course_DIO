import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no formato: +551140028922:\n')

phone_number = phonenumbers.parse(phone)
print('')
print('*' * 30)
print(geocoder.description_for_number(phone_number, 'pt'))
print('*' * 30)