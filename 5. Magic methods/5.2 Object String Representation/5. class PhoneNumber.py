'''
Класс PhoneNumber
Реализуйте класс PhoneNumber, описывающий телефонный номер.
При создании экземпляра класс должен принимать один аргумент:
    phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
        dddddddddd
        ddd ddd dddd
Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:
    PhoneNumber('<телефонный номер в формате dddddddddd>')
И следующее неформальное строковое представление:
    <телефонный номер в формате (ddd) ddd-dddd>
'''

# 1
phone = PhoneNumber('9173963385')
print(str(phone)) # (917) 396-3385
print(repr(phone)) # PhoneNumber('9173963385')

# 2
phone = PhoneNumber('918 396 3389')
print(str(phone)) # (918) 396-3389
print(repr(phone)) # PhoneNumber('9183963389')

# 3
phone1 = PhoneNumber('9173963385')
phone2 = PhoneNumber('918 396 3389')
phone3 = PhoneNumber('919 333 3344')
print(phone1, phone2, phone3, sep=', ') # (917) 396-3385, (918) 396-3389, (919) 333-3344
print([phone1, phone2, phone3]) # [PhoneNumber('9173963385'), PhoneNumber('9183963389'), PhoneNumber('9193333344')]