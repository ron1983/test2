print("ddddd")
print("你好啊")
a=12
b=13
c=a+b
print(c)
str222= 'ni hao a xiao pengyou '
len = len(str222)
print(len)
def pp():
    print("ni zhen shuai")
pp()
def g_tokg(g1):
    kg1= g1/1000
    print(kg1)
g_tokg(2000)
import math
def tri(a1,b1):
    c2 = a1*a1+b1*b1
    c1= math.sqrt(c2)
    print(c1)

tri(3,4)


file = open("/Users/gongjie/desktop/t.txt",'w')
file.write("你好啊，abc ,1111")


i= 0
path ='/Users/gongjie/desktop/'
while i<11:
    i = i+1
    str1 = path + str(i) +'.txt'
    file1=open(str1,'w')
    file1.close()

j = 0
for j in range(1,100):
    if j%2 == 0:
        print(j)

periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])

num_list = [6, 2, 7, 4, 1, 3, 5]
print(sorted(num_list))
print(num_list)

a1 = [i**2 for i in range(1,10)]
c1 = [j+1 for j in range(1,10)]
k1 = [n for n in range(1,10) if n % 2 ==0]
z1 = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
print(a1)
print(c1)
print(k1)
print(z1)

#print（c)


path1 = '/Users/gongjie/desktop/Walden.txt'
with open(path1,'r') as text:
    words = text.read().split()
    print(words)
 #   for word in words:
 #       print('{}-{} times'.format(word,words.count(word)))

class CocaCola:
    calories    = 140
    sodium      = 45
    total_carb  = 39
    caffeine    = 34
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
'Caffeine' ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink1(self):
        print('You got {} cal energy!'.format(self.calories))

        cola = CocaCola('我最帅')
        cola.local_logo
        cola.drink1(self)

class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA()
print(obj_a.attr)



