d={}
d[1]=10
d[2]=20
d.update({3:30,4:40})
d.update({1:100})
print(d)
d.setdefault(4,40)
print(d)
d.setdefault(5,50)
print(d)
print(d.keys())
print(d.values())
print(d.items())

print(d.get(1))
print(d.get(6))