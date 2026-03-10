
#1
davlatlar = ["O'zbekiston", "AQSh", "Rossiya",  "Qozog'iston",  ]
print(davlatlar)

#2
print(len(davlatlar))

#3
print(sorted(davlatlar))

#4
print(sorted(davlatlar, reverse=True))

#5
print(davlatlar)

#6
davlatlar.reverse()
print(davlatlar)

#7
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8
sonlar = list(range(120,1200,2))

#9
print(sum(sonlar))

#10
print(max(sonlar)-min(sonlar))

#11
print(len(sonlar))

#12
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

#13 o'rtasidan 20 elementni chop eting
length = len(sonlar)
start_index = length // 2 - 10
end_index = length // 2 + 10
print(sonlar[start_index:end_index])



