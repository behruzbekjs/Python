# Function - malum vazifani bajaruvchi kod bloklari
# Funksiyalar - kodni qayta ishlatish va tartibga solish uchun
# Funksiyalarni yaratish uchun def kalit so'zidan foydalanamiz
# Pythondagi tayyor funksiyalar - print(), input(), len() va boshqalar
# O'z funksiyalarimizni yaratish uchun def kalit so'zidan foydalanamiz
print("Hello, World!") # print() - matnni ekranga chiqarish uchun tayyor funksiya
name = input("Ismingiz nima? ") # input() - foydalanuvchidan ma'lumot olish uchun tayyor funksiya
print(f"Salom, {name}!") # f-string - matn ichida o'zgaruvchilarni qo'shish uchun qulay usul
# Funksiya yaratish
def salom_ber(name):
    """Foydalanuvchiga salom beruvchi funksiya"""
    print(f"Salom, {name}!")

# Funksiyani chaqirish
salom_ber("Ali") # Salom, Ali!

# Funksiyada parametrlar va argumentlar
def salom_ber(ism):
    print(f"Salom, {ism}!")

salom_ber("Vali") # Salom, Vali!
salom_ber("Olim") # Salom, Olim!
salom_ber("Orif") # Salom, Orif!

# Deafault parametrlar
def calculate_age(birth_year = 1995 , name = "Olim"):
    age = 2026 - birth_year
    print(f"{name}ning yoshi {age} da.")

calculate_age(2005 , "Ismoil")
calculate_age(2010 , "Sardor")
calculate_age()
def yosh_hisobla(tugilgan_yil, joriy_yil = 2026):
    print(f"Sizning yoshingiz {joriy_yil - tugilgan_yil} da.")