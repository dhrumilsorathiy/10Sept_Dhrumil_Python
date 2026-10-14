def mask_phone_number(phone):
    return "*" * 6 + phone[-4:]

number = "9876541234"
print(mask_phone_number(number))