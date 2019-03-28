
a = input("Enter value of a!\n")
b = input("Enter value of b\n")

print(type(a))
print(int(a) + int(b))

=============================================================

l1 = range(1,10)
l1 = list(l1)

for i in l1:
    print(i)

d1 = {"name":"Manas", "email":"manas@gmail.com"}
for k,v in d1.items():
    print(k,v)
=========================================================
labmda

a = 100
b = 20

large = lambda a,b,c:"a is largest" if a>b else "b is largest"  if b > c else "c is largest"
print(large(100,20,30))

==============================================================
map and filter

l1 = [1,2,3,4,5]

l1 = filter(lambda i:i%2==0, l1)
print(list(l1))

==============================================================

l1 = [1,2,3,4,5]

l2 = [ i*i for i in l1 if i%2==0]
print(l2


l1 = [1,2,3,4,5]

l2 = (i*i for i in l1 if i%2==0)
print(tuple(l2))


==============================================================
l1 = [1,2,3,4,5]

l2 = {i: i*i for i in l1 if i%2==0}
print(l2)

===============================================================
Generator

def gen():

    yield "Umakant"
    yield "Mane"

temp = gen()

#print(list(temp))

# for i in temp:
#     print(i)

#print(list(temp))

# print(temp.__next__())
# print(temp.__next__())

while True:

    try:
        print(temp.__next__())
    except:
        break
