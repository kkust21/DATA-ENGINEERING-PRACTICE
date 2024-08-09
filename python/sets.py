drw = set()
print(type(drw),drw)
drw_o={10,11,12,13,4,2,10}
drw_s={3,6,7,10,11,45}
drw_o.add(45)#will add at any random pos
print(drw_o)
drw_s.discard(6)#del ele
print(drw_o)
print(drw_s)
print("len of ele", len(drw_o))
print("union",drw_o | drw_s )
print("intersection", drw_o & drw_s)
print("difference", drw_o - drw_s )
print("difference", drw_s - drw_o)

set1={"banana","apple","gaurav"}
set2={"banana","gaurav","apple"}
print(set1==set2) #return true or false
#it returns true irespective of position


