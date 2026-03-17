# Data types (Malumot turlari)
# 1. integer; 2.float; 3.string; 4.boolean; 5.list; 6.tuple; 7.dictionary
cars = ['BMW', 'Mercedes', 'Audi' , 'Lexus', 'Porsche']

# Dictionary (Lug'at)
car = {
    'brand': 'BMW',
    'color': 'qora',
    'year': 2020,
    'price': 50000
}
print(car)
print(type(car))

student = {
    'fullname': 'Ali Valiyev',
    'age': 20,
    'course': 3,
    'favourite_books': ["Atomic habits", "The 7 Habits of Highly Effective People", "The Power of Now"],
    'is_completed': False,
    'is_married': True
}   
print(student)
print(type(student))

# 1.Qiymatlarni olish
print(student['fullname'])
print(student['age'])
print(student['favourite_books'])

for book in student['favourite_books']:
    print(book)

# 2.Qiymatlarni olish
student['age'] = 21
student['course'] = 4
print(student)

# Yangi key-value qo'shish
student = ['hobbies'] = ['Reading a book' , 'Watching a football match' , 'Learning knowledges']
print(student)

# 4. Key-valueni o'chirish
del student['is_married']
print(student)

# 5.Empty dictionary
talaba_1 = {}
talaba_1['fullname'] = 'Vali Aliyev'
talaba_1['age'] = 22
talaba_1['course'] = 4
print(talaba_1)
print(f"Talaba {talaba_1['fullname'].title()} {talaba_1['age']} yoshda va {talaba_1['course']} - kursda o'qiydi.")

# get metodi()
telefonlar ={'ali': '99890123456', 'vali': '99890123457', 'gani': '99890123458'}
print(telefonlar.get('ali'))

