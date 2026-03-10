son = 1
while son < 10:
    print(son)
    # son += 1

# Infinity loop - cheksiz sikl / abadiy sikl

# # while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting (dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ""
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#     else:
#         print("Dastur ishlashdan to'xtatildi.")

# # while va break(sindirish operatori)
# sonlar = list(range(1, 11))
# for sonlar in sonlar:
#     if sonlar == 5: # son 5 ga teng bo'lganda sikl to'xtaydi
#         break
#     print(sonlar)

# continue - davom ettirish operatori
# while son < 10:
#     print(son)
#     son += 1
#     if son %2!=0: # son toq bo'lsa, sikl to'xtaydi
#         continue
#     else:
#         print(son)

input = "Yoshingizni kiriting: "

while True:
    value = input(input)
    if value == 'exit' or value == 'quit':
        break
    age = int(value)
    
    if age < 7:
        narx = 2000
    elif 7 <= age < 18:
        narx = 3000
    elif 18 <= age < 65:
        narx = 10000
    else: narx = 0
    if narx == 0:
        print("Chipta bepul")
    else:
        print(f"Chipta {narx} so'm")