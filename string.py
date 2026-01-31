# ism = 'Anvar'
# shahar = 'Urganch'
# viloyat = 'Xorazm'
# matn = "Men yangi 📱 oldim"
# print(matn)
# smaylik = "😊"
# print(smaylik)

# #String ustida amallar

# ism = "Anvar"
# print("Mening ismim " + ism)
# print("Mening ismim", ism)
# ism = 'Ahad'
# familiya = 'Qayum'
# print("Mening ismim " + ism + " " + familiya)
# print("Mening ismim", ism, familiya)

# #f-String

# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {familiya}, {ism}, {familiya}!")


# #Maxsus Belgilar

# print("Hello World!")
# print("Hello \tWorld!")
# print("Hello \nWorld!")

# #String Metodlar

# ism = 'james'
# familiya = 'bond'
# ism_sharif = f"{ism}  {familiya}"
# print(ism_sharif.upper())  #Upper bu hamma harflarni kattalashtiradi
# ism_sharif = ism_sharif.upper()
# print(ism_sharif.lower()) #hamma harf kichkina bo'ladi
# print(ism_sharif.title()) # Faqatgina Bosh harfi katta bo'ladi
# print(ism_sharif.capitalize()) # faqatgina birinchi harfi katta bo'ladi

# meva = "       olma       "
# print("Men" + meva.lstrip() + "yaxshi ko'raman")  # Chap tomondagi spaceni olib tashlaydi
# print("Men" + meva.rstrip() + "yaxshi ko'raman")  # O'ng tomondagi spaceni olib tashlaydi
# print("Men" + meva.strip() + "yaxshi ko'raman")  #Ikkala tomondan spaceni olib tashlaydi
# print("Men" + meva + "yaxshi ko'raman")

#  # INPUT Funksiyasi

# ism = 'Behruzbek'
# ism = input("Ismingiz nima?")
# print("Assalomu alaykum," + ism.title())
# ism = input("Ismingiz nima?\n>>>")  #Foydalanuvchi ismini yangi qatordan kiritadi
# print("Assalomu alaykum" + " " + ism.title())  # Foydalanuvchi malumotni kichik harfda kiritsa ham bosh harfi katta bo'ladi

# # Amaliyot
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
# tuman + " tumani, " + viloyat + " viloyati")
# print("Iltimos, quyidagi ma'lumotlarni kiriting:")
# kocha.title() = input("Ko'changiz: ")
# mahalla.title() = input("Mahallangiz: ")
# tuman.title() = input("Tumaningiz: ")
# viloyat.title() = input("Viloyatingiz: ")
# print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
# tuman + " tumani, " + viloyat + " viloyati")   
# print(kocha.title() + " ko'chasi,\n" + mahalla.title() + " mahallasi,\n" + \
# tuman.title() + " tumani,\n" + viloyat + " viloyati")
# manzil = f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyati"
# print(manzil)
# # Topshiriq
# a = 4
# b = 8
# c = 2
# orta_arifmetik = (a + b + c) / 3
# print(f"Uch sonning o'rtacha arifmetigi: {orta_arifmetik}")
# orta_geometrik = (a * b * c) ** (1/3)
# print(f"Uch sonning o'rtacha geometrigi: {orta_geometrik}")
