from collections import namedtuple, deque, Counter,ChainMap,defaultdict

courses = namedtuple('course', ['name', 'tech'])
print(courses)
clist = courses(name='data science', tech='python')
print(clist)
print(getattr(clist,"tech"))
#print(getattr(clist.name))
print(clist[0])
courselist = ["web","Angular"]
print(courses._make(courselist))#convert list to named tuple

tmodule_1= {1:"Angular",2:"Python"}
tmodule_2= {4:"cloud",5:"pyspark"}
mlist=ChainMap(tmodule_1,tmodule_2)
print(mlist)
tmodule_3= {5:"Golang",2:"React"}
nlist=mlist.new_child(tmodule_3)
print(nlist)
print(nlist.maps)
print(list(nlist.keys()))
print(list(nlist.values()))
print("*")
t_list =["1","2","3","4","5"]
tqueu = deque(t_list)
print(tqueu)
tqueu.appendleft("8")
print(tqueu)
tqueu.popleft()
print(tqueu)

Fruits=["apple","Banana","orange","pine","apple","orage"]
count = Counter(Fruits)
print(count)
print(count.keys())
print(count.values())
print(count.items())






