def sort_dictionary(myDictionary):

    mod_lst2 = []

    lst1 = [lis for lis in myDictionary]
    print (lst1)

    length = len(myDictionary)
    i = 0
    
    minimum = myDictionary[lst1[0]][1]
    minKey = lst1[0]
    for j in range(length):
        for i in range(i+1, len(myDictionary)):
            if minimum < myDictionary[lst1[i]][1]:
               minimum = myDictionary[lst1[i]][1]
               minKey = lst1[i]
            print(mod_lst2)  
    myTuple = (lst1[i], myDictionary[lst1[i]][0])
    myDictionary.pop[lst1[i]]
    mod_lst2.append(myTuple)
                 

sort_dictionary({'Bella' : (9999938, 5), 'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)})


