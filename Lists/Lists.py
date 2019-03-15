'''
lists is a sequence of values
list is a collection of homogeneous and heterogeneous elements
lists are used to work on the homogeneous

all types of values
lists can be accessed by index ,farward and backward index
lists allows duplicate values
+,* : are only opertores can be used on lists
sort is used to display in decending order
sort(reverse=True) is used to display in decending order
remove() remover the given value from list
pop(index)remover and retuns the values related to that index

'''

l=[71,1,89,6]

print(type(l))


l1=l+[5]
print(l1)

l2 = l*5
print(l2)

l3= l.sort()

print(l)

l4=l.sort(reverse=True)
print(l)

print(l)
l.remove(71)
print(l)

l.remove([3])
print(l)





