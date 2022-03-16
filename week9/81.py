newlist = ['list1', 'list2', 'list3', 'list4', 'list5']

#print(newlist)
#print(len(newlist))

def chop(lista):
    del lista[0]
    del lista[(len(lista)-1)]
    return None

def middle(lista):
    listb = list()
    for item in lista:
        #print(item)
        if item == lista[0] or item == lista[(len(lista)-1)]:
            continue
        listb.append(item)
    return listb

newerlist = middle(newlist)
#print(newlist)
print(newerlist)
