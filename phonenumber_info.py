import phonenumbers
from phonenumbers import geocoder, carrier, timezone

phone_number = phonenumbers.parse("enter mobile number")

#this will print the country name
print(geocoder.description_for_number(phone_number, 'en'))

#this will print the service provider
print(carrier.name_for_number(phone_number, 'en'))

#this will print the timezone
print(timezone.time_zones_for_number(phone_number))