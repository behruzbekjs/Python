# age = int(input("Yoshingizni kiriting: "))
# if age > 18:
#     print("Kirish huquqiga egasiz")
# else:
#     print("Siz hali yoshsiz")

# ball = int(input("Balingizni kiriting: "))
# if ball < 56:
#     print("Siz imtihondan o'ta olmadingiz")
# elif ball >= 56 and ball < 70:
#     print("Tabriklayman siz imtihondan 3 baho oldingiz")
# elif ball >= 70 and ball < 85:
#     print("Tabriklayman siz imtihondan 4 baho oldingiz")
# elif ball >= 85 and ball < 100:
#     print("Tabriklayman siz imtihondan 5 baho oldingiz")
# else:
#     print("Iltimos 0 dan 100 gacha bo'lgan ball kiriting")


# # Pasport olish
# age = int(input("Yoshingizni kiriting: "))
# if age >= 16:
#     print("Siz pasport olishingiz mumkin")
# else:
#     print("Siz hali pasport olishingiz mumkin emas")

# # Sonning musbat yoki manfiyligini aniqlash
# son = float(input("Istalgan son kiriting: "))
# if son > 0:
#     print("Siz kiritgan son musbat")
# else:
#     print("Siz kiritgan son manfiy")


# # Juft yoki toqligini aniqlash
# son = int(input("Istalgan son kiriting: "))
# if son % 2 == 0:
#     print("Siz kiritgan son juft")
# else:
#     print("Siz kiritgan son toq")

# a = int(input("Uchburchakning 1-tomonini kiriting : "))
# b = int(input("Uchburchakning 2-tomonini kiriting : "))
# c = int(input("Uchburchakning 3-tomonini kiriting : "))
# if a + b > c or a + c > b or b + c > a:
#     print("Uchburchak yasash mumkin")
# else:
#     print("Uchburchak yasash mumkin emas")

# a = 7
# b = 2
# print(a ** b % 5)

# # 2-mashq 
# a = int(input("Uchburchakning Birinchi tomonni kiriting: "))
# b = int(input("Uchburchakning Ikkinchi tomonni kiriting: "))
# c = int(input("Uchburchakning Uchinchi tomonni kiriting: "))
# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasash mumkin")
# else:
#     print("Uchburchak yasash mumkin emas")

# # 3-mashq
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# if a < b < c:
#     print("Yes")
# else:
#     print("No")





# # 36-mashq
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a < b:
#     print(a)
# else:
#     print(b)

# # 37
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a <= b:
#     print(0, b)
# else:
#     print(a, b)

#  print(f"{4 * x * y:.1f}",  f"{(x + y) / 2:.1f}")
# else:
#     print(f"{(x + y) / 2:.1f}", f"{4 * x * y:.1f}")

# # 35
# import math
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# if a >= b >= c :
#     print(a * 2, b * 2, c * 2)
# else:
#     print(math.fabs(a), math.fabs(b), math.fabs(c))
# # 39
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# a = 2 * x * 2 * y
# b = (x + y) / 2
# if x > y :
#  x = a
#  y = b
# else:
#     x = b
#     y = a
# print(f"{x:.1f}", f"{y:.1f}")
# # 40

# # 43
# import math
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x < 0 and y < 0:
#     print(math.fabs(x), math.fabs(y))
# elif x > 0 and y > 0:
#     print(x, y)
# else:
#     print(x + 0.5, y + 0.5)

# # 45
# import math

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# c = int(input("Uchinchi sonni kiriting: "))
# D = b ** 2 - 4 * a * c
# if D < 0:
#     print("NO")
# else:wd 
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(f"{x1:.2f}", f"{x2:.2f}")

# # 38
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# z = float(input("Uchinchi sonni kiriting: "))
# if 1 <= x <= 3:
#     print(x)
# if 1 <= y <= 3:
#     print(y)
# if 1 <= z <= 3:
#     print(z)




# # 40
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# z = int(input("Uchinchi sonni kiriting: "))
# if x > 0:
#     x = x ** 2
# if y > 0:
#     y = y ** 2
# if z > 0:
#     z = z ** 2
# print(x, y, z)

# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# print(max(x, y), min(x, y))

# # 33
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# z = int(input("Uchinchi sonni kiriting: "))
# print(max(x + y + z , x , y , z), min(x + y / 2 , x , y , z) ** 2)

# # 42
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = float(input("Uchinchi sonni kiriting: "))
# d = float(input("To'rtinchi sonni kiriting: "))
# if a <= b <= c <= d:
#     max = max(a, b, c, d)
#     print(max, max, max, max)
# else:
#     min = min(a, b, c, d)
#     print(min, min, min, min)

# import math
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x < y:
#     a = (x + y) / 2
#     b = 2 * x * y
#     x = a
#     y = b
# elif x > y:
#     a = (x + y) / 2
#     b = 2 * x * y
#     x = b
#     y = a
# print(x, y)


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
z = float(input("Uchinchi sonni kiriting: "))
min_value = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if min_value == x:
        x = (y + z) / 2
    elif min_value == y:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
else:
    x = x
    y = y
    z = z
    print( x , y , z)