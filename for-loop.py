# # Takrorlanish operatorlari
# # loop sikl
# # 1.for loop
# # 2.while loop
# students = ["Elbek", "Maftuna", "G'ulomjon", "Mahliyo", "Dilbek"]
# print(students[0])
# print(students[1]) 
# print(students[2])
# print(students[3])
# print(students[4])
# for students in students:
#     print(students)

# for guest in students:
#     print(f"Salom, {guest}!")

# print(f"Salom, {guest}!")

# # sonlar ro'yxatida for loop
# sonlar = list(range(1, 51))  #2 dan 50gacha bo'lgan sonlar ro'yxati
# for number in sonlar:
#     print(number)

# print("Dastur tugadi")

numbers = list(range(20, 0, -1))  #20 dan 1 gacha bo'lgan sonlar ro'yxati
# start_default_value = 0
# stop = 20
# step_default_value = 1
print(numbers)

people = ["Ali", "Vali", "Otabek", "G'ulomjon", "Mahliyo"]
for person in people:
    print(f"Salom, {person}!")
print(f"Salom, {person}!")

# 2 - usul
for i in range(len(people)):
    print(f"Salom, {people[i]}!")

# 1 - iteratsiya index = 0, element = "Ali"
# 2 - iteratsiya index = 1, element = "Vali"
# 3 - iteratsiya index = 2, element = "Otabek"
# 4 - iteratsiya index = 3, element = "G'ulomjon"
# 5 - iteratsiya index = 4, element = "Mahliyo"

# 1 dan 100 gacha chiqarish
# sonlar2 = list(range(1, 100))
# for son in sonlar2:
#     print(son)

# for son in range(1, 100):
#     print(son)

# # 2- usul
# for index in range(1, 100):
#     print(index)
#     print(sonlar2[index])

# 1 - marta : index = 0, sonlar[0] = 1
# 2 - marta : index = 1, sonlar[1] = 2
# ....
# 99 - marta : index = 98, sonlar[98] = 99

# Amaliyot
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)