import random

lower = "qwertyuioplkjhgfdsazxcvbnm"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
number = "1234567890"
symbols = "!@#$%\^&*?_=+-/"
all = lower + upper + number + symbols
length = 8
password = "".join(random.sample(all,length))
print("Password is:",password)

