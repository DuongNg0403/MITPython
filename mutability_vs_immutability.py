l1 = ["Hello",]
l2 = [1,2,3,4]
l3 = [l1,l2]
l4 = [["Hello",],[1,2,3,4]]

print(l3 == l4)
print(id(l3)==id(l4))
print(id(l3))
print(id(l4))