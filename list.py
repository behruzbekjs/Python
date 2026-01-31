# # List -ro'yxat
# user1 = "Behruzbek"
# user2 = "Maftuna"
# users = [ "Gulyora", "G'ulomjon", "John" , "Margaritta"]
# # List elementlari indekslanadi
# # Dasturlashda indekslash 0 dan boshlanadi
# # List elementini olish(element indeks orqali olinadi)
# first_element = users[0]
# third_element = users[2]
# print(first_element, third_element , users[3])
# print(type(users)) # list
# mixed_data = ['test' , 12 , True , -45.6]
# # 1.del operator yordamida list elementini o'chirish
# del users[4]
# print(users)
# # 2.remove() metodi yordamida list elementini o'chirish
# users.remove("John")
# print(users)
# # Listdan element sug'urib olish(pop)
# # list.pop(index?)
# deletedElement = users.pop(1)
# print( deletedElement)
# print( users)
ismlar = ["Abror", "Mahmud", "Hasan" , "Husan"]
print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(ismlar[1] + " bugun choyxonaga boramizmi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")