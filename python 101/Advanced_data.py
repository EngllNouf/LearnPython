list = [1 ,1 ,11 ,1 ,12,34,5,6,8,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list)  # Output: [11, 1, 12]
list[2] = 68
print(type(list))
print(list)
#appedd wile add the value at the end of the list
list.append(348)
print(list)
# insert will add the value at the specified index
list.insert(2, 100)
print(list)
#delete will remove the value at the specified index
list.remove(100) # هنا يحذف العنصر الي يكون قيمته 100 مو بالانديكس
print(list)
# .clear delete all the values in the list
list.clear()
print(list)
#.pop delete the last value in the list

#tuple is immutable 
New_list = ('Nouf' , 'Hala' , 'Reem')
print(type(New_list))

list_forkey = {'name': 'Nouf' , 'age': 25, 'city': 'Riyadh'}
print(type(list_forkey))
print(list_forkey['name'])
print(list_forkey.values())
print(list_forkey.keys())



