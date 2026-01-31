# x = 8
# y = 2
# print(x % y)
# print(3 % 8)
# print( 4 // 2, 12 // 5)
# # Comparison (solishtirish Operators => Boolean values(true, false)
# # ==
# print(3 == 4) # false
# print(3 == 3) # true
# print(3 != 4) # true
# print(3 != 3) # false
# # >
# print(3 > 4) # false
# print(4 > 3) # true
# print(5 >= 3, 5 <= 5)
# print(5 <= 3, 5 >= 5)
# # Logical Operators
# # and, or, not
# print(3 > 4 and 5 < 6) # false and true => false
# print(3 > 4 or 5 < 6) # false or true => true
# print(not(3 > 4)) # not false => true
# print(not(5 < 6)) # not true => false
# print((3 > 4 or 5 < 6) and not(10 > 5)) # (false or true) and not true => true and false => false
# print((3 < 4 or 5 < 6) and not(10 > 5)) # (true or true) and not true => true and false => false
# print((3 < 4 or 5 < 6) and not(10 < 5)) # (true or true) and not false => true and true => true
# # Membership Operators
# # in, not in
# s = "Hello world"
# print("H" in s) # true
# print("h" in s) # false
# print("H" not in s) # false
# print("h" not in s) # true
# lst = [1, 2, 3, 4, 5]
# print(3 in lst) # true
# print(6 in lst) # false
# print(3 not in lst) # false
# print(6 not in lst) # true
# # Identity Operators
# # is, is not
# a = [1, 2, 3]
# b = a
# print(a is b) # true
# c = [1, 2, 3]
# print(a is c) # false
# print(a is not c) # true
# print(a is not b) # false
# d = a
# print(a is d) # true    
# print(b is d) # true
# print(c is d) # false

z = 12
print(z > 10 and z < 5 or z > 8) #True and false or True => false or True => True
z += 3