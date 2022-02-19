# Сгенерируйте "надёжный" пароль

import random

characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^()}{/<>'
print('Password Length: 10')
passwordLength = 10
password = ''

for i in range(passwordLength):
    password += random.choice(characters)
print(password)