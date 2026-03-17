# Dictionary elemetlari bilan ishlash
phone = {
    'brand': 'Apple',
    'model': 'iPhone 17 Pro Max',
    'year' : 2025 ,
    'color': 'space gray',
    'price': 1500
}
# 1.get() metodi
print(phone.get('model'))
print(phone.get('price'))
print(phone.get('battery')) # mavjud bo'lmagan kalit uchun None qaytaradi
print(phone.get('battery', 'Battery information not available')) # mavjud bo'lmagan kalit uchun maxsus xabar qaytaradi

# 2.items() metodi
print(phone.items()) # kalit-qiymat juftlarini ko'rsatadi
for key , value in phone.items():
    print(f"{key}: {value}")

telefonlar = {
    'ali' : 'iPhone 17 Pro Max',
    'vali' : 'Samsung Galaxy S30 Ultra',
    'olim' : 'Google Pixel 8 Pro',
    'orif' : 'nokia 3310'
}
for k , q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

# 3.keys() metodi
print(phone.keys()) # faqat kalitlarni ko'rsatadi
print(telefonlar.keys())

mahsulotlar = {
    'olma' : 10000,
    'anor' : 15000,
    'uzum' : 20000,
    'shaftoli' : 12000
}
# print(mahsulotlar.keys())
print("Do\'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4.in operatori
# 1. listda in operatori element mavjudligini tekshiradi
# fruits = ['olma', 'anor', 'uzum', 'shaftoli']
# print('olma' in fruits) # True
# print('banan' in fruits) # False

# fruit = input("Qaysi meva yoqadi?")
# if fruit in fruits:
#     print(f"{fruit.title()} do'konimizda bor.")
# else:
#     print(f"{fruit.title()} do'konimizda yo'q.")

bozorlik = ['olma', 'anor', 'banan', 'shaftoli']

for mahsulot in mahsulotlar:
    print(mahsulotlar)

for mahsulot in bozorlik:
    if mahsulot in mahsulotlar:
        print(f"{mahsulot.title()} narxi {mahsulotlar[mahsulot]} so'm.")

print(sorted(mahsulotlar.keys())) # kalitlarni alifbo tartibida chiqaradi
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar.keys()):
    print(mahsulot.title())

# 5.values() metodi - lug'atning barcha qiymatlarini olish
print(phone.values()) # faqat qiymatlarni ko'rsatadi
print(telefonlar.values())

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)