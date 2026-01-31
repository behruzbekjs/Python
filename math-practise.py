
# # 1
# import math
# x = float(input("1-sonni kiriting: "))
# y = float(input("2-sonni kiriting: ")) 
# a = x + y
# b = math.pow(y, 2)
# c = b + 2
# d = x + math.pow(x, 3) / 5
# e = math.exp(y + 2)
# c1 = a / (b + math.fabs(c / d)) + e
# print("Natija:", c1)


# import math
# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = math.pow(a, 2) + math.pow(b, 2) + 2
# d = b * (a + b) / (2 * b + a * b)
# t = math.pow(a, 1 / 5) + math.pow(d, 1 / 4) * c 
# print("%2f" % t)


# import math

# # Foydalanuvchidan qiymatlarni olish
# print("Iltimos, quyidagi qiymatlarni kiriting:")
# a = float(input("a ni kiriting (misol uchun 3): "))
# b = float(input("b ni kiriting (misol uchun 1): "))
# c = float(input("c ni kiriting (misol uchun 3): "))
# d = float(input("d ni kiriting (misol uchun 2): "))
# x = float(input("x ni kiriting (misol uchun 0.88): "))
# m = a * math.pow(x, 2) + b * x + c
# f = x * math.pow(a, 3) + math.pow(a, 2) + math.pow(a, b-c)
# h = math.cos(math.fabs((a * x + b) / (c * x + d + math.pow(2, c))))
# w = m / f + h
# print("Natija:", w)

import math
a = int(input("1 - sonni kiriting: "))
x = float(input("2 - sonni kiriting: "))
b = math.sqrt(x - 1)
c = math.sqrt(x + 2)
d = math.log10(math.sqrt(a * math.pow(x, 2)) + 2)
e = c + math.sqrt(x + 24) + math.pow(x, 5)
tt = (b + c + d ) / e
print("%.2f" % tt)