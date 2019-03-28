#LIST

l1 = []
l1.append()
l1.extend()
l1.insert()

l1.remove(item)
l1.pop()
l1.clear()

l1.index(item)
l1.count()
l1.sort(reverse=True)
l1.reverse()
l1.copy()

=====================================================
#TUPLE
count()
index()

=====================================================
#DICT


d1 = {}

d1['name'] = "Manas"
d1.update({"email":"manas@gmail.com", "address":"BTM"})
d1.copy()
d1.clear()
d1.popitem()
d1.pop(key)
d1.values()
d1.keys()
d1.get(key)
print(d1)

=================================================================
#SETS
s1 = {1}
s1.add(1)
s1.clear()
s1.remove(value)
s1.copy()

s1= {1,2,3,4,6}
s2 = {1,2,3,4,5}
temp = s1.difference(s2)#s1-s2

s1.difference_update(s2)
s1.intersection(s2)
s1.intersection_update(s2)

print(temp)

