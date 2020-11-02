print("welcome")
a = 100
b = 75
if a > b:
    print(a)
    for count in range(6):
       triangle()

digits = [0,1,2,3,4,5,6,7,8,9]
print(digits)
window_size = 2
for i in range(len(digits)-(window_size-1)):
   print(digits[i:i+window_size])
#tuple
person1 = ['sanskriti',20 ,'varanasi']
person2 = ['saniya',19,'sangamner']
people = [person1 , person2]
for name, age, city in people:
            print(name)
            print(age)
            print(city)
           
