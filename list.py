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
# ismlar = ["Abror", "Mahmud", "Hasan" , "Husan"]
# print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
# print(ismlar[1] + " bugun choyxonaga boramizmi?")
# print(f"{ismlar[2]} va {ismlar[3]} egizaklar")

historical_people = ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", "Marie Curie"]
modern_people = ["Elon Musk", "Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Jeff Bezos"]
f" Men tarixiy shaxslardan {historical_people[0]} \n va {historical_people[3]} bilan, zamonaviy shaxslardan esa {modern_people[0]} \n va {modern_people[2]} bilan suhbatlashishni istardim. "

friends = ['mahliyo', 'nodira', 'dilmira', 'lobar']
friends.append('yulduz')
friends.insert(0 , 'maftuna')
print(friends)
element = friends.pop(1)
print(element)
print(friends)

# list.sort()  
friends.sort()  # alfavit tartibida sortirovka qiladi
print(friends)
friends.sort(reverse=True)  # teskari alfavit tartibida sortirovka qiladi
print(friends)
# sorted() - bu funksiyadir, list.sort() esa metoddir
sorted_list = sorted(friends)  # alfavit tartibida yangi ro'yxat yaratadi
print(sorted_list)

nums = [5, 2, 9, 1, 5, 6]
print(sorted(nums))  # alfavit tartibida yangi ro'yxat yaratadi

# sonlar ro'yxat ustida sodda amallar
narxlar = [12000 , 22500 , 23456 , 9800 , 5600 , 9934 , 32874]
eng_arzoni = min(narxlar)
eng_qimmati = max(narxlar)
yigindi = sum(narxlar)
print(eng_arzoni , eng_qimmati , yigindi)
# Ro'yxatni kesib olish
students = ["Ali", "Vali", "Sami", "Dani", "Olim", "Gulnora"]

# Ro'yxatdan nusxa olish
# 1. Shallow (sayoz) copy
sonlar = [1, 2, 3, 4, 5]
sonlar2 = sonlar
sonlar2.append(77)
sonlar.insert(2 , -8)
print(sonlar2)
# 2. Deep (chuqur) copy
sonlar3 = sonlar.copy()
sonlar3.append(99)

# Tupple-o'zgarmas qiymat

