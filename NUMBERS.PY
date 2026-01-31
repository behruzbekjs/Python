# Malumot turlari (data types) bilan ishlash
# 1. String( matn)
# 2. Number(son) => Integer (butun son) 5 -5 10; 2. Float (o'nlik son)
# 3. Boolen (mantiqiy qiymat) => True (rost) False (yolg'on)
text="lorem ipsum"
age = 28
is_student = True

# type() funksiyasi malumot turini aniqlash uchun ishlatiladi
print(type(text))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(is_student))  # <class 'bool'>
print(type(3.14))      # <class 'float'>

a = 20
b = -30
c = a + b
print(c)

pi = 3.1415
radius = 10
diametr = 2 * radius
aylana_yuzi = pi * (radius ** 2)
print("Aylana yuzi:", aylana_yuzi)


print(50 / 10)  # Float
print(50 // 10) # Integer

print(a + b)  # Qo'shish
print(a - b)  # Ayirish
print(a * b)  # Ko'paytirish
print(a / b)  # Bo'lish

aholi_soni = 7_594_000_000
print("Dunyo aholisi soni:", aholi_soni, "nafar ga yaqin odamlar yashaydi.")

PI = 3.1415
G = 9.81    
print("Pi ning qiymati:", PI)
print("Erkin tushish tezlanishi:", G)

# x = -7
# y = -5
# z = 10
x,y,z, = -7, -5, 10
print(x+ y - z)

kv_tomon = int(input("Kvadrat tomonini kiriting: "))
print(type(kv_tomon))
# int() funksiyasi malumotni butun songa aylantiradi
print(kv_tomon ** 2)

ism = "Jobir"
yosh = 36
xabar = ism + "ning yoshi " + str(yosh) + " da."
print(xabar)

print(int(5.36))  # 5
print(int(5.5))

print(int(5.76))  # 5
print(float(7))   # 7.0
print(float(3 + 7))  # 10.0

t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2025 - (t_yil)
print(yosh)

# Amaliyot
# 1-mashq

x = int(input("Istalgan son kiriting:\n>>>"))
print(x, " ning kvadrati ", x**2, " ga teng")
print(x, " ning kubi ", x**3, " ga teng")

# 2-mashq

yosh = int(input("Yoshingiz nechida? \n>>>"))
t_yil = 2025 - yosh
print("Siz ", t_yil, "- yilda tug'ilgan ekansiz.")

# 3-mashq

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)

# 2-Amaliyot
# 1-mashq