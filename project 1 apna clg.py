import random
import string

password_len = 8
lol= string.digits + string.ascii_letters + string.punctuation
password =""

for i  in range(password_len):
  password += random.choice(lol)

print("password is =",password)
